import numpy as np
from numba import jit
import sys
from time import perf_counter_ns

@jit(nopython=True)
def matmul(A, B):
    C = np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[0]):
        for k in range(A.shape[1]):
            for j in range(B.shape[1]):
                C[i,j] += A[i,k] * B[k,j]
    return C

if __name__=='__main__':

    N = int(sys.argv[1])

    matmul(np.random.rand(1,1),np.random.rand(1,1))

    start_time = perf_counter_ns()

    A = np.random.rand(N, N)
    B = np.random.rand(N, N)

    result = matmul(A, B)
    end_time = perf_counter_ns()
    
    print(f"{(end_time-start_time)/1e9:.2f} seconds")