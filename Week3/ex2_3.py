import os
import blosc
import numpy as np
import time
import sys


def write_numpy(arr, file_name):
    np.save(f"{file_name}.npy", arr)
    os.sync()


def write_blosc(arr, file_name, cname="lz4"):
    b_arr = blosc.pack_array(arr, cname=cname)
    with open(f"{file_name}.bl", "wb") as w:
        w.write(b_arr)
    os.sync()


def read_numpy(file_name):
    return np.load(f"{file_name}.npy")


def read_blosc(file_name):
    with open(f"{file_name}.bl", "rb") as r:
        b_arr = r.read()
    return blosc.unpack_array(b_arr)


def main(n):
    # Generate a 3D NumPy array of zeros with size (n, n, n) and dtype uint8
    tiled_array = np.tile(
    np.arange(256, dtype='uint8'),
    (n // 256) * n * n,
    ).reshape(n, n, n)

    array = tiled_array
    # print(f"Generated a 3D array of size ({n}, {n}, {n})")

    # Measure time to save using write_numpy
    start_time = time.time()
    write_numpy(array, "array_numpy")
    numpy_write_time = time.time() - start_time
    print(f"Time to save using write_numpy: {numpy_write_time:.4f} seconds")

    # Measure time to save using write_blosc
    start_time = time.time()
    write_blosc(array, "array_blosc")
    blosc_write_time = time.time() - start_time
    print(f"Time to save using write_blosc: {blosc_write_time:.4f} seconds")

    # Measure time to read using read_numpy
    start_time = time.time()
    read_numpy("array_numpy")
    numpy_read_time = time.time() - start_time
    print(f"Time to read using read_numpy: {numpy_read_time:.4f} seconds")

    # Measure time to read using read_blosc
    start_time = time.time()
    read_blosc("array_blosc")
    blosc_read_time = time.time() - start_time
    print(f"Time to read using read_blosc: {blosc_read_time:.4f} seconds")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <size>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n <= 0:
            raise ValueError("Size must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    main(n)