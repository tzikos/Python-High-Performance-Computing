import random
import multiprocessing
import time
import matplotlib.pyplot as plt
import numpy as np

def sample():
    """Perform a single Monte Carlo estimation for Pi."""
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    return 1 if x**2 + y**2 <= 1 else 0

def sample_multiple(samples_partial):
    """Estimate Pi using a partial sample count."""
    return sum(sample() for _ in range(samples_partial))

def run_experiment(n_proc, samples=1000000):
    """Run the Monte Carlo Pi estimation with a given number of processes."""
    chunk_size = samples // n_proc
    pool = multiprocessing.Pool(n_proc)
    
    start_time = time.perf_counter()
    results_async = [pool.apply_async(sample_multiple, (chunk_size,)) for _ in range(n_proc)]
    hits = sum(r.get() for r in results_async)
    end_time = time.perf_counter()
    
    pool.close()
    pool.join()

    pi_estimate = 4.0 * hits / samples
    elapsed_time = end_time - start_time
    return elapsed_time, pi_estimate

if __name__ == '__main__':
    max_threads = multiprocessing.cpu_count()  # Should return 20 on your system
    samples = 1000000
    times = []
    speedups = []

    # Run for n_proc from 1 to max_threads
    for n_proc in range(1, max_threads + 1):
        elapsed_time, pi_value = run_experiment(n_proc, samples)
        times.append(elapsed_time)
        print(f"Processes: {n_proc}, Time: {elapsed_time:.6f}s, Pi Estimate: {pi_value:.6f}")

    # Compute speedup relative to single-process execution
    base_time = times[0]
    speedups = [base_time / t for t in times]

    num_processes = list(range(1, len(speedups) + 1))  # Assuming 1 to max_threads

    # Estimate parallel fraction between the runs
    parallel_fractions = []

    for p, S in zip(num_processes, speedups):
        if p == 1:  # Single process case, assume fully serial (F = 0)
            F = 0.0
        else:
            F = (p * (S - 1)) / ((p - 1) * S)
        
        parallel_fractions.append(F)
    
    print(f"Estimated F: {np.average(parallel_fractions[1:])*100:.1f}% with std: {np.std(parallel_fractions[1:])*100:.1f}%")

    # Plot speedup curve
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, max_threads + 1), speedups, marker='o', linestyle='-', color='b', label="Speedup")
    plt.axhline(y=max_threads, color='r', linestyle='--', label="Ideal Speedup")
    plt.xlabel("Number of Processes")
    plt.ylabel("Speedup (T1 / Tn)")
    plt.title("Speedup vs Number of Processes (Monte Carlo Pi)")
    plt.legend()
    plt.grid()

    # Save figure instead of showing it
    plt.savefig("speedup_plot.png", dpi=300, bbox_inches="tight")
