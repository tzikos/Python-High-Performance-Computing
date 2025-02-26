import numpy as np
import timeit
import matplotlib.pyplot as plt

# Generate logarithmically spaced sizes
sizes = np.logspace(1, 4.5, num=10, dtype=int)
n_runs = 1000

row_perf = []
col_perf = []
matrix_sizes_kb = []
performance_ratios = []

for SIZE in sizes:
    mat = np.random.rand(SIZE, SIZE)

    def double_column():
        return 2 * mat[:, 0]

    def double_row():
        return 2 * mat[0, :]

    # Measure execution time
    row_time = timeit.timeit(double_row, number=n_runs) / n_runs
    col_time = timeit.timeit(double_column, number=n_runs) / n_runs

    # Compute performance in MFLOP/s
    row_mflops = (SIZE / (row_time * 1e6))
    col_mflops = (SIZE / (col_time * 1e6))

    # Compute matrix size in KB
    matrix_size_kb = (SIZE**2 * 8) / 1024

    # Compute performance ratio
    perf_ratio = row_mflops / col_mflops

    # Store results
    row_perf.append(row_mflops)
    col_perf.append(col_mflops)
    matrix_sizes_kb.append(matrix_size_kb)
    performance_ratios.append(perf_ratio)

    print(f"SIZE={SIZE}, Matrix KB={matrix_size_kb:.2f}, Row MFLOP/s={row_mflops:.2f}, Col MFLOP/s={col_mflops:.2f}, Ratio={perf_ratio:.2f}")

# Create plots
fig, ax1 = plt.subplots(figsize=(8, 6))

# Plot MFLOP/s
ax1.loglog(matrix_sizes_kb, row_perf, 'o-', label="Row-first MFLOP/s")
ax1.loglog(matrix_sizes_kb, col_perf, 's-', label="Column-first MFLOP/s")
ax1.set_xlabel("Matrix size (KB)")
ax1.set_ylabel("MFLOP/s")
ax1.legend()
ax1.grid(True, which="both", linestyle="--")
ax1.set_title("Performance of Row vs Column Operations")

# Save and show
plt.savefig("performance_plot.png")
plt.show()

# Plot ratio
plt.figure(figsize=(8, 6))
plt.loglog(matrix_sizes_kb, performance_ratios, 'o-', color='r', label="Row/Column MFLOP Ratio")
plt.axhline(y=1, color='k', linestyle='--', label="Equal Performance")
plt.xlabel("Matrix size (KB)")
plt.ylabel("Performance Ratio (Row / Column)")
plt.legend()
plt.grid(True, which="both", linestyle="--")
plt.title("Performance Ratio of Row vs Column Operations")

# Save and show
plt.savefig("performance_ratio_plot.png")
plt.show()