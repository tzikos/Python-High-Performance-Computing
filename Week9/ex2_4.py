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

    x_host = cuda.pinned_array(N, dtype=np.float32)
    y_host = cuda.pinned_array(N, dtype=np.float32)
    a_host = cuda.pinned_array_like(x_host)

    # Fill with random values
    x_host[:] = np.random.rand(N).astype(np.float32)
    y_host[:] = np.random.rand(N).astype(np.float32)

    start_time = perf_counter_ns()
    
    # Allocate device memory
    x_device = cuda.to_device(x_host)
    y_device = cuda.to_device(y_host)
    a_device = cuda.device_array(N, dtype=np.float32)

    # Launch kernel
    threads_per_block = 64
    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block  # Calculate blocks per grid

    # Run the kernel once to compile it
    add_kernel[1, 64](x_device, y_device, a_device)  # Launch with a small grid

    # Run the kernel with the actual grid size
    add_kernel[blocks_per_grid, threads_per_block](x_device, y_device, a_device)

    # Wait for the kernel to finish execution
    cuda.synchronize()

    # Copy result back using pinned memory (faster transfer)
    a_device.copy_to_host(a_host)

    end_time = perf_counter_ns()

    print("First 10 elements:", a_host[:10])

    print(f"\n \n{(end_time-start_time)/1e6} ms")


if __name__ == '__main__':
    N = int(sys.argv[1])
    main(N)