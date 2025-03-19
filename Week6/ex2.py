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
    for i in range(b, e, s * 2):
        if i + s < len(arr):
            arr[i // s] = arr[i] + arr[i + s]  # Sum adjacent elements

def full_reduction(n_processes, elemshape):
    step = 1
    size = len(arr)
    while size > 1:
        pool.map(reduce_step,
                 [(i, min(i + step * 2, size), step, elemshape) for i in range(0, size, step * 2)],
                 chunksize=1)
        size = (size + 1) // 2  # Reduce size progressively
        step *= 2

if __name__ == '__main__':
    n_processes = 4  # Increase for parallelism
    
    # Load shared array
    data = np.load(sys.argv[1])
    elemshape = data.shape[1:]
    shared_arr = mp.RawArray(ctypes.c_float, data.size)
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    del data

    # Run parallel reduction
    t = time()
    pool = mp.Pool(n_processes, initializer=init, initargs=(shared_arr,))
    full_reduction(n_processes, elemshape)
    pool.close()
    pool.join()

    # Compute mean
    final_image = arr[0] / len(arr)
    print(final_image)
    # Save output
    print(time() - t)
    
    Image.fromarray(
        (255 * final_image.astype(float)).astype('uint8')
    ).save('result.png')
