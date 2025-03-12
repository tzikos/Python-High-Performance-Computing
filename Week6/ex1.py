import ctypes
import multiprocessing as mp
import sys
from time import perf_counter as time
import numpy as np
from PIL import Image


def init(shared_arr_):
    global shared_arr
    shared_arr = shared_arr_


def tonumpyarray(mp_arr):
    return np.frombuffer(mp_arr, dtype='float32')


def reduce_step(args):
    b, e, s, elemshape = args
    arr = tonumpyarray(shared_arr).reshape((-1,) + elemshape)
    arr[b//s:e//s] = arr[b:e:s] + arr[b+1:e:s]  # Perform summation every two elements
    # arr[b:e:s] = arr[b:e:s] + arr[b+1:e:s]

if __name__ == '__main__':
    n_processes = 4  # Increase for parallelism
    chunk = 2

    # Load shared array
    data = np.load(sys.argv[1])
    elemshape = data.shape[1:]
    shared_arr = mp.RawArray(ctypes.c_float, data.size)
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    del data

    # Run parallel sum
    t = time()
    pool = mp.Pool(n_processes, initializer=init, initargs=(shared_arr,))

    pool.map(reduce_step,
             [(i, min(i + chunk, len(arr)), chunk, elemshape) for i in range(0, len(arr), chunk)],
             chunksize=1)

    # Write output
    print(time() - t)
    final_image = arr[0]
    # arr_min = final_image.min()
    # arr_max = final_image.max()
    # final_image /= len(arr) # For mean
    # final_image = (final_image - arr_min) / (arr_max - arr_min) * 255

    print(final_image)
    Image.fromarray(
        (255 * final_image.astype(float)).astype('uint8')
    ).save('result.png')  
