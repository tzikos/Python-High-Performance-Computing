import numpy as np
import sys
from time import perf_counter_ns

if __name__ == '__main__':
    
    N = int(sys.argv[1])  # Get matrix size from command line

    A = np.random.rand(N,N)
    B = np.random.rand(N,N)

    start = perf_counter_ns()

    result = A@B

    end = perf_counter_ns()

    print(f"{(end-start)/1e9} seconds")