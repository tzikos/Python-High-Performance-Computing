import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
import time
from tqdm import tqdm 

def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2.0:
            return i
    return 100

def generate_mandelbrot_set(points, num_processes):
    pool = multiprocessing.Pool(num_processes)
    start_time = time.perf_counter()
    escape_times = [pool.apply_async(mandelbrot_escape_time, (points[i],)) for i in range(len(points))]
    escape_times = [elem.get() for elem in escape_times]
    end_time = time.perf_counter()
    pool.close()
    pool.join()
    return np.array(escape_times), end_time - start_time

def plot_speedup(process_counts, speedups):
    plt.figure(figsize=(8, 6))
    plt.plot(process_counts, speedups, marker='o', linestyle='-', color='b', label="Speedup")
    plt.axhline(y=max(process_counts), color='r', linestyle='--', label="Ideal Speedup")
    plt.xlabel("Number of Processes")
    plt.ylabel("Speedup (T1 / Tn)")
    plt.title("Speedup vs Number of Processes (Mandelbrot Set)")
    plt.legend()
    plt.grid()
    plt.savefig("mandelbrot_speedup.png", dpi=300, bbox_inches="tight")

if __name__ == "__main__":
    width = 800
    height = 800
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    max_threads = multiprocessing.cpu_count()
    
    # Generate points
    x_values = np.linspace(xmin, xmax, width)
    y_values = np.linspace(ymin, ymax, height)
    points = np.array([complex(x, y) for x in x_values for y in y_values])
    
    times = []
    speedups = []
    process_counts = list(range(1, max_threads + 1))
    
    for num_proc in tqdm(process_counts):
        _, elapsed_time = generate_mandelbrot_set(points, num_proc)
        times.append(elapsed_time)
        print(f"Processes: {num_proc}, Time: {elapsed_time:.6f}s")
    
    base_time = times[0]
    speedups = [base_time / t for t in times]
    
    plot_speedup(process_counts, speedups)