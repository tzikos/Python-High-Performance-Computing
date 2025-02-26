import numpy as np
import timeit 

SIZE = 10000
n_runs = 1000

mat = np.random.rand(SIZE, SIZE)
def double_column():
    return 2 * mat[:, 0]

def double_row():
    return 2 * mat[0, :]

# Measure execution time using timeit (10 runs for better accuracy)
row_time = timeit.timeit(double_column, number=n_runs)
col_time = timeit.timeit(double_row, number=n_runs)

print(f"Row-first (timeit, avg over {n_runs} runs): {row_time / 10:.6f} sec")
print(f"Column-first (timeit, avg over {n_runs} runs): {col_time / 10:.6f} sec")