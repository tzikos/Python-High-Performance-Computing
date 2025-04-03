from numba import cuda 


@cuda.jit
def add_kernel(x, y, a):
    i = cuda.grid(1)  # Get thread index
    
    if i < len(a):  # Make sure we do not go out of bounds
        a[i] = x[i] + y[i]