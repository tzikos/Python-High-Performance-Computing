import numpy as np
import timeit
import matplotlib.pyplot as plt

# Generate logarithmically spaced sizes
sizes = np.logspace(2, 8, num=10, dtype=int)
n_runs = 10

row_perf = []
row_sizes_kb = []

for SIZE in sizes:
    mat = np.random.rand(1, SIZE)

    def double_row():
        return 2 * mat[0, :]

    # Measure execution time
    row_time = timeit.timeit(double_row, number=n_runs) / n_runs

    # Compute performance in MFLOP/s
    row_mflops = (SIZE / (row_time * 1e6))

    # Compute row vector size in KB
    row_size_kb = (SIZE * 8) / 1024  # 8 bytes per double-precision float

    # Store results
    row_perf.append(row_mflops)
    row_sizes_kb.append(row_size_kb)

    print(f"SIZE={SIZE}, Row KB={row_size_kb:.2f}, Row MFLOP/s={row_mflops:.2f}")

# Create log-log plot
plt.figure(figsize=(8, 6))
plt.loglog(row_sizes_kb, row_perf, 'o-', label="Row Doubling MFLOP/s")
plt.xlabel("Row Vector Size (KB)")
plt.ylabel("MFLOP/s")
plt.legend()
plt.grid(True, which="both", linestyle="--")
plt.title("Performance of Row Doubling Operation")

# Add vertical lines for typical cache sizes (L1, L2, L3)
L1_cache_size = 32  # Typical L1 cache size in KB
L2_cache_size = 256  # Typical L2 cache size in KB
L3_cache_size = 8192  # Typical L3 cache size in KB

plt.axvline(x=L1_cache_size, color='r', linestyle='--', label=f"L1 Cache (~{L1_cache_size} KB)")
plt.axvline(x=L2_cache_size, color='g', linestyle='--', label=f"L2 Cache (~{L2_cache_size} KB)")
plt.axvline(x=L3_cache_size, color='b', linestyle='--', label=f"L3 Cache (~{L3_cache_size} KB)")

plt.legend()
plt.savefig("row_doubling_performance.png")
plt.show()