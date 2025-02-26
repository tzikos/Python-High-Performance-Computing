import numpy as np
import timeit

# Generate logarithmically spaced sizes (10 values from 10^2 to 10^4)
sizes = np.logspace(2, 4, num=10, dtype=int)

n_runs = 1000

# # Open file to log results
# with open("timing_results.txt", "w") as f:
#     f.write("SIZE,Row-first_time,Column-first_time\n")

for SIZE in sizes:
    mat = np.random.rand(SIZE, SIZE)

    def double_column():
        return 2 * mat[:, 0]

    def double_row():
        return 2 * mat[0, :]

    # Measure execution time
    row_time = timeit.timeit(double_column, number=n_runs) / n_runs
    col_time = timeit.timeit(double_row, number=n_runs) / n_runs

    # Log results
    # f.write(f"{SIZE},{row_time:.6e},{col_time:.6e}\n")
    print(f"SIZE={SIZE}, Row-first: {row_time:.6e} sec, Column-first: {col_time:.6e} sec")