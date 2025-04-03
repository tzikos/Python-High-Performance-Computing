from numba import cuda
import sys
import numpy as np
from time import perf_counter_ns

@cuda.jit
def matmul_kernel(A, B, C):
    j, i = cuda.grid(2)  # Grid index (row i, column j)
    
    if i < C.shape[0] and j < C.shape[1]:  # Ensure within bounds
        temp = 0.0
        for k in range(A.shape[1]):  # Loop over shared dimension
            temp += A[i, k] * B[k, j]
        C[i, j] = temp  # Store result in C

if __name__ == '__main__':
    
    N = int(sys.argv[1])  # Get matrix size from command line

    # 🚀 Pinned Memory Allocation (CPU)
    A_host = cuda.pinned_array((N, N), dtype=np.float32)
    B_host = cuda.pinned_array((N, N), dtype=np.float32)
    C_host = cuda.pinned_array((N, N), dtype=np.float32)  # Initialize result

    # ✅ Fill A & B with random values
    A_host[:] = np.random.rand(N, N).astype(np.float32)
    B_host[:] = np.random.rand(N, N).astype(np.float32)
    C_host[:] = np.zeros((N, N), dtype=np.float32)  # Ensure it's zeroed

    # 🚀 Move data to GPU
    A_device = cuda.to_device(A_host)
    B_device = cuda.to_device(B_host)
    C_device = cuda.device_array((N, N), dtype=np.float32)  # Allocate on GPU

    # 🚀 Define thread & block sizes
    threads_per_block = (16, 16)  # 16x16 block size
    blocks_per_grid_x = (N + threads_per_block[0] - 1) // threads_per_block[0]
    blocks_per_grid_y = (N + threads_per_block[1] - 1) // threads_per_block[1]
    blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)

    # ✅ Run the kernel once to trigger JIT compilation (warmup)
    matmul_kernel[blocks_per_grid, threads_per_block](A_device, B_device, C_device)
    cuda.synchronize()  # Ensure kernel completes before timing

    # ✅ Measure execution time (JIT compiled already)
    start = perf_counter_ns()
    matmul_kernel[blocks_per_grid, threads_per_block](A_device, B_device, C_device)
    cuda.synchronize()  # Ensure kernel completes
    end = perf_counter_ns()

    # ✅ Copy result back to CPU
    C_device.copy_to_host(C_host)

    print(f"Matrix multiplication completed successfully!")
    print(f"Execution Time: {(end - start)/1e9} seconds")