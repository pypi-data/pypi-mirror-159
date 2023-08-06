#this file contains the GPU version of the various functions
#it is not always imported. The script basicFunctions determines if this is imported or not

import numpy as np
import sys, os
import dask.array as da

import cupy
import cupyx
from cupyx.scipy.fft import get_fft_plan
import cupy_backends
from cupy.cuda import cufft
import numba
from numba import vectorize, cuda, jit

from . import basicFunctions as bf

@cuda.jit("(float32[:,:], int32[:], int32, int32, float32, int32, int32, complex64[:])")
def extractTrapCuspResultsGPU(filtered, maxlocs, rise, top, percentage, shift, batchsize, out):
	i = cuda.grid(1)
	if i < batchsize:
		wave = filtered[i]
		wavelen = filtered.shape[1]
		maxloc = maxlocs[i]
		maxval = wave[maxloc]
		threshold = maxval * percentage
		#find upwards cross point
		#iterate from the max location back towards beginning
		i = maxloc
		found = False
		leftCross = None
		rightCross = None
		while i >= maxloc - rise - top and found == False and i >= 0:
			if wave[i] >= threshold and wave[i-1] <= threshold:
				found = True 
				leftCross = i
			i-= 1
		rightCross = None
		found = False
		i = maxloc
		while i <= maxloc + rise + top and found == False and i <= wavelen-1:
			if wave[i-1] >= threshold and wave[i]<= threshold:
				found = True
				rightCross = i
			i+=1
		#now use these to extract the results
		if rightCross is None or leftCross is None:
			out[i] = np.complex64(complex(np.nan, np.nan))
		else:
			midpoint = (leftCross + rightCross)/2
			out[i] = np.complex64(complex(wave[int(midpoint)+shift],  midpoint - top/2 - rise))


def gpuTrapCuspFilterImplementation(waves, method='trap', rise=625, top=100, tau=1250, percentage=0.8, pretrigger = 800, shift = 0, numStreams = 2):
	"""
	This is a GPU-based implementation of the filtering routine using either the trapezoidal filter or the cusp filter depending on what the user requests. 
	
	Parameters
	----------
	waves: np.ndarray or dask.ndarray
		Input waveforms
	
	inputFilter: np.ndarray
		The filter input to the function
	
	rise, top, tau: see Nab.bf.defineSingleTrap
	
	percentage: between 0 and 1
		threshold cross percentage used for extraction
	
	pretrigger: int
		length of window of waveform before the daq trigger expected location
	
	shift: int
		energy extraction point
	
	minBatchSize: int
		the smallest a batch can be. Based on the HDF5 chunking behavior. This is the HDF5 chunk size
	"""
	#iterate over the chunks in the dask array
	if type(waves) == np.ndarray:
		waves = da.asarray(waves, chunks = {0: 'auto', 1: -1})
	#now create the various arrays and plans
	#get chunk sizes and waveform length information
	numWaves, waveformLength = waves.shape
	if method=='trap':
		inputFilter = bf.defineSingleTrap(rise, top, tau)
	elif method=='cusp':
		inputFilter = bf.defineCuspFilter(rise, top, tau)
	filterLength = len(inputFilter)
	padLength = waveformLength + filterLength - 1
	padLength = cupyx.scipy.fft.next_fast_len(padLength) #does the clever padding trick to improve performance
	while padLength % 2 != 0:
		padLength = cupyx.scipy.fft.next_fast_len(padLength+1)
	#figure out the Dask chunk size
	blockSize = waves.blocks[0].shape[0]
	outputSize = (blockSize, padLength)
	
	#pad the filter
	paddedFilt = np.zeros(outputSize[1], dtype=np.float32)
	paddedFilt[:len(paddedFilt)] = paddedFilt[:]
	
	gpuFiltFFTBatchedStreams = []
	gpuBatchWaveformsStreams = []
	gpuBatchWaveformsPaddedStreams = []
	fftPlanStreams = []
	gpuBatchWaveformsFFTStreams = []
	fftPlanReverseStreams = []
	cudaStreams = []
	pinnedBatches = []
	meansStreams = []
	gpuResultsStreams = []
	maxlocsStreams = []
	for i in range(numStreams): #create the cuda streams and storage containers
		s = cupy.cuda.Stream()#first initialize the stream
		cudaStreams.append(s)
		with s: #set us to using that particular stream
			#move the filter to the GPU and calculate it's FFT
			gpuFilt = cupy.array(paddedFilt)
			#define the FFT plan for the filter
			filtrFFTPlan = cupy.cuda.cufft.Plan1d(outputSize[1], cupy.cuda.cufft.CUFFT_R2C, 1)
			#create the output array from this function
			gpuFiltFFT = filtrFFTPlan.get_output_array(gpuFilt)
			#now calculate the fft of this filter
			filtrFFTPlan.fft(gpuFilt, gpuFiltFFT, cupy.cuda.cufft.CUFFT_FORWARD)
			#configure this to work for batched multiplications
			gpuFiltFFTBatched = cupy.array(gpuFiltFFT)[None,]
			gpuFiltFFTBatchedStreams.append(gpuFiltFFTBatched)
			#now configure the storage spaces on the GPU
			batch = cupyx.zeros_pinned(outputSize, dtype=np.float32)#allocate pinned host memory, size of the original waveforms with padding. Also force conversion to 32-bit at this stage
			pinnedBatches.append(batch)
			#Allocate empty space for the GPU to hold the waveforms
			gpuBatchWaveforms = cupy.empty(outputSize, dtype=cupy.float32)
			gpuBatchWaveformsStreams.append(gpuBatchWaveforms)
			#define the FFT Plan that will be followed for the forward transform
			fftPlan = cupy.cuda.cufft.Plan1d(gpuBatchWaveformsPadded.shape[1], cupy.cuda.cufft.CUFFT_R2C, gpuBatchWaveforms.shape[0])
			fftPlanStreams.append(fftPlan)
			#get the space for the FFT waveforms to live in
			gpuBatchWaveformsFFT = fftPlan.get_output_array(gpuBatchWaveformsPadded)
			gpuBatchWaveformsFFTStreams.append(gpuBatchWaveformsFFT)
			#define the plan for the reverse FFT plan to be followed
			fftPlanReverse = cupy.cuda.cufft.Plan1d(gpuBatchWaveformsPadded.shape[0], cupy.cuda.cufft.CUFFT_C2R, waveforms.shape[0])
			fftPlanReverseStreams.append(fftPlanReverse)
			#storage space for the mean values
			means = cupy.empty(waves.blocks[0].shape[0], dtype=np.float32)
			meansStreams.append(means)
			maxlocs = cupy.empty(blockSize, dtype=np.int32)
			maxlocsStreams.append(maxlocs)
			gpuResults = cupy.empty(blockSize, dtype=np.csingle)
			gpuResultsStreams.append(gpuResults)
			del gpuFilt
			del filtrFFTPlan
			del gpuFiltFFT
	#now set up the cuda blocks and whatnot
	threadsperblock = 32 #set up the blocks
	blockspergrid = int(np.ceil(blockSize/threadsperblock))
	#store the current location in the process
	currLoc = 0
	leftover = len(waves.blocks) % numStreams #determine if there will be leftovers or not
	#store the overall results
	results = np.array(numWaves, np.csingle)
	for i in range(0, len(waves.blocks), numStreams):
		#grab each block of memory
		blocks = [*waves.blocks[i:i+numStreams]]
		#start up the first set of operations, then queue up the second set
		#should be able to do dumb streams here
		for j in range(len(cudaStreams)):
			with cudaStreams[j]:
				pinnedBatches[j][:,:waveformLength] = blocks[j].compute() #move to the storage in pinned memory
				gpuBatchWaveformsStreams[j].set(pinnedBatches[j]) #move to the GPU
				#calculate the means of the waveforms
				cupy.mean(gpuBatchWaveformsStreams[j][:,:pretrigger], axis = 1, out = meansStreams[j])
				#shift the waveform by the pretrigger region mean
				cupy.subtract(gpuBatchWaveformsStreams[j], means[:,None], out=gpuBatchWaveformsStreams[j])
				#reset the padding region to 0
				gpuBatchWaveformsStreams[j][:,waveformLength:] = 0
				#calculate the FFT
				fftPlanStreams[j].fft(gpuBatchWaveformsPaddedStreams[j], gpuBatchWaveformsFFTStreams[j], cupy.cuda.cufft.CUFFT_FORWARD)
				#now multiply the FFT waveform data with the FFT filter
				cupy.multiply(gpuBatchWaveformsFFTStreams[j], gpuFiltFFTBatchedStreams[j], out=gpuBatchWaveformsFFTStreams[j])
				#do the inverse FFT operation
				fftPlanReverseStreams[j].fft(gpuBatchWaveformsFFTStreams[j], gpuBatchWaveformsPaddedStreams[j], cupy.cuda.cufft.CUFFT_INVERSE)
				#now to do the extraction
				cupy.argmax(gpuBatchWaveformsFFTStreams[j], axis=1, out = maxlocsStreams[j])
				extractTrapCuspResultsGPU[blockspergrid, threadsperblock](gpuBatchWaveformsFFTStreams[j], maxlocsStreams[j], rise, top, percentage, shift, blockSize, gpuResultsStreams[j])
			#now synchronize the streams once all this has been queued up
		for j in range(len(cudaStreams)):
			cudaStreams[j].synchronize()
			results[currLoc:currLoc+blocks[j].shape[0]] = gpuResultsStreams[j].get()
			currLoc += blocks[j].shape[0]
	#now handle the leftovers
	for i in range(leftover):
		#grab each block of memory
		blocks = [*waves.blocks[i:i+numStreams]]
		#start up the first set of operations, then queue up the second set
		#should be able to do dumb streams here
		for j in range(leftover):
			with cudaStreams[j]:
				pinnedBatches[j][:blocks[j].shape[0],:waveformLength] = blocks[j].compute() #move to the storage in pinned memory
				gpuBatchWaveformsStreams[j].set(pinnedBatches[j]) #move to the GPU
				#calculate the means of the waveforms
				cupy.mean(gpuBatchWaveformsStreams[j][:,:pretrigger], axis = 1, out = meansStreams[j])
				#shift the waveform by the pretrigger region mean
				cupy.subtract(gpuBatchWaveformsStreams[j], means[:,None], out=gpuBatchWaveformsStreams[j])
				#reset the padding region to 0
				gpuBatchWaveformsStreams[j][:,waveformLength:] = 0
				#calculate the FFT
				fftPlanStreams[j].fft(gpuBatchWaveformsPaddedStreams[j], gpuBatchWaveformsFFTStreams[j], cupy.cuda.cufft.CUFFT_FORWARD)
				#now multiply the FFT waveform data with the FFT filter
				cupy.multiply(gpuBatchWaveformsFFTStreams[j], gpuFiltFFTBatchedStreams[j], out=gpuBatchWaveformsFFTStreams[j])
				#do the inverse FFT operation
				fftPlanReverseStreams[j].fft(gpuBatchWaveformsFFTStreams[j], gpuBatchWaveformsPaddedStreams[j], cupy.cuda.cufft.CUFFT_INVERSE)
				#now to do the extraction
				cupy.argmax(gpuBatchWaveformsFFTStreams[j], axis=1, out = maxlocsStreams[j])
				extractTrapCuspResultsGPU[blockspergrid, threadsperblock](gpuBatchWaveformsFFTStreams[j], maxlocsStreams[j], rise, top, percentage, shift, blockSize, gpuResultsStreams[j])
			#now synchronize the streams once all this has been queued up
		for j in range(len(cudaStreams)):
			cudaStreams[j].synchronize()
			results[currLoc:currLoc+blocks[j].shape[0]] = gpuResultsStreams[j].get()
			currLoc += blocks[j].shape[0]
	#now free up all of the memory that was allocated on CPU and GPU
	
	del paddedFilt
	del gpuFiltFFTBatchedStreams
	del gpuBatchWaveformsStreams
	del gpuBatchWaveformsPaddedStreams
	del fftPlanStreams
	del gpuBatchWaveformsFFTStreams
	del fftPlanReverseStreams
	del cudaStreams
	del pinnedBatches
	del meansStreams
	del gpuResultsStreams
	del maxlocsStreams
	return results
