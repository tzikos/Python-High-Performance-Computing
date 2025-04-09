import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
import sys

def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if abs(z) > 2.0:
            return i
    return 100

def compute_row(x_idx, x, y_values, height):
    # Now we compute a column (fixed x, varying y)
    col = np.empty(height, dtype='int32')
    for y_idx, y in enumerate(y_values):
        c = complex(x, y)
        col[y_idx] = mandelbrot_escape_time(c)
    return x_idx, col

def generate_mandelbrot_memmap(width, height, xmin, xmax, ymin, ymax, num_processes, mmap_filename):
    x_values = np.linspace(xmin, xmax, width)
    y_values = np.linspace(ymin, ymax, height)

    # Create the memory-mapped file
    mandelbrot_mmap = np.memmap(mmap_filename, dtype='int32', mode='w+', shape=(height, width))

    # Function for multiprocessing - now we process by columns (fixed x)
    args = [(x_idx, x, y_values, height) for x_idx, x in enumerate(x_values)]

    with multiprocessing.Pool(num_processes) as pool:
        for x_idx, col in pool.starmap(compute_row, args):
            # Place each column in the appropriate position
            mandelbrot_mmap[:, x_idx] = col

    mandelbrot_mmap.flush()
    return mandelbrot_mmap

# def plot_mandelbrot(mandelbrot_data, xmin, xmax, ymin, ymax):
#     plt.imshow(mandelbrot_data, cmap='hot', extent=(xmin, xmax, ymin, ymax))
#     plt.axis('off')
#     plt.savefig('mandelbrot.png', bbox_inches='tight', pad_inches=0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <N for NxN image>")
        sys.exit(1)

    num_proc = multiprocessing.cpu_count()
    N = int(sys.argv[1])
    width = N
    height = N
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    mmap_file = f"mandelbrot_int32_{N}x{N}.raw"

    mandelbrot_mmap = generate_mandelbrot_memmap(
        width, height, xmin, xmax, ymin, ymax, num_proc, mmap_file
    )

    # Optional read-back and plot
    # mandelbrot_array = np.memmap(mmap_file, dtype='int32', mode='r', shape=(N, N))
    # plot_mandelbrot(mandelbrot_array, xmin, xmax, ymin, ymax)