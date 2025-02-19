import numpy as np
import sys
from time import perf_counter_ns

def self_matrix_multiplication(mat, p):
    new_mat = np.copy(mat)
    for _ in range(p):
        new_mat = np.matmul(new_mat, mat)
    
    return new_mat

    
def main():
    
    path = sys.argv[1]
    mat = np.load(path)
    
    p = int(sys.argv[2])
    start_time = perf_counter_ns()
    result = self_matrix_multiplication(mat, p)
    end_time = perf_counter_ns()
    time_sec = (end_time - start_time) / 1e9
    print(time_sec)
    np.save("result.npy", result)

    return None

if __name__ == "__main__":
    main()
    




