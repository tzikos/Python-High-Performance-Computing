from numba import cuda
import numpy as np
import sys
from time import perf_counter_ns

# Define the CUDA kernel
@cuda.jit
def add_kernel(x, y, a):
    i = cuda.grid(1)  # Get thread index
    
    if i < len(a):  # Make sure we do not go out of bounds
        a[i] = x[i] + y[i]

# Main function
def main(N):
    np.random.seed(42)

    # Create random input vectors
    x = np.random.rand(N).astype(np.float32)
    y = np.random.rand(N).astype(np.float32)
    a = np.empty_like(x)

    start_time = perf_counter_ns()

    # Allocate memory on the device
    x_device = cuda.to_device(x)
    y_device = cuda.to_device(y)
    a_device = cuda.to_device(a)

    # Launch kernel
    threads_per_block = 64
    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block  # Calculate blocks per grid

    # Run the kernel once to compile it
    add_kernel[1, 64](x_device, y_device, a_device)  # Launch with a small grid

    # Run the kernel with the actual grid size
    add_kernel[blocks_per_grid, threads_per_block](x_device, y_device, a_device)

    # Wait for the kernel to finish execution
    cuda.synchronize()


    # Copy the result back to the host
    a_device.copy_to_host(a)

    end_time = perf_counter_ns()

    # Optionally, print a small portion of the result to verify correctness
    print("First 10 elements of the result: \n", a[:10])
    print(f"\n \n{(end_time-start_time)/1e6} ms")


if __name__ == '__main__':
    N = int(sys.argv[1])
    main(N)