import numpy as np
import zarr
import sys
import multiprocessing
import os

def mandelbrot_escape_time(c):
    """Calculate the escape time for a complex number in the Mandelbrot set."""
    z = 0
    for i in range(100):
        z = z**2 + c
        if abs(z) > 2.0:
            return i
    return 100

def compute_chunk(chunk_coords, chunk_size, xmin, xmax, ymin, ymax, array_size, zarr_path):
    """Compute a chunk of the Mandelbrot set and write directly to the Zarr array."""
    chunk_x, chunk_y = chunk_coords
    
    # Calculate the indices range for this chunk
    x_start = chunk_x * chunk_size
    y_start = chunk_y * chunk_size
    x_end = min(x_start + chunk_size, array_size)
    y_end = min(y_start + chunk_size, array_size)
    
    # Create the output chunk array
    chunk_data = np.zeros((y_end - y_start, x_end - x_start), dtype=np.int32)
    
    # Calculate the complex coordinates for this chunk
    x_coords = np.linspace(xmin, xmax, array_size)[x_start:x_end]
    y_coords = np.linspace(ymin, ymax, array_size)[y_start:y_end]
    
    # Compute the Mandelbrot set for this chunk
    for i, y in enumerate(y_coords):
        for j, x in enumerate(x_coords):
            c = complex(x, y)
            chunk_data[i, j] = mandelbrot_escape_time(c)
    
    # Open the Zarr array and write this chunk
    mandelbrot_zarr = zarr.open(zarr_path, mode='r+')
    mandelbrot_zarr[y_start:y_end, x_start:x_end] = chunk_data
    
    return f"Processed chunk ({chunk_x}, {chunk_y})"

def generate_mandelbrot_zarr(array_size, chunk_size, num_processes=None, xmin=-2.0, xmax=2.0, ymin=-2.0, ymax=2.0):
    """Generate the Mandelbrot set and store it in a Zarr array using parallel processing."""
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()
    
    # Create the Zarr array
    zarr_path = f"mandelbrot_zarr_{array_size}x{array_size}_c{chunk_size}"
    
    # Make sure the directory exists
    os.makedirs(zarr_path, exist_ok=True)
    
    # Create the zarr array with appropriate chunks
    mandelbrot_zarr = zarr.create(
        shape=(array_size, array_size),
        chunks=(chunk_size, chunk_size),
        dtype=np.int32,
        store=zarr_path
    )
    
    # Calculate number of chunks in each dimension
    num_chunks_x = (array_size + chunk_size - 1) // chunk_size
    num_chunks_y = (array_size + chunk_size - 1) // chunk_size
    total_chunks = num_chunks_x * num_chunks_y
    
    print(f"Processing {total_chunks} chunks using {num_processes} processes...")
    
    # Set up the chunk coordinates
    chunk_coords = [(x, y) for y in range(num_chunks_y) for x in range(num_chunks_x)]
    
    # Set up the arguments for each chunk computation
    args = [(coords, chunk_size, xmin, xmax, ymin, ymax, array_size, zarr_path) 
            for coords in chunk_coords]
    
    # Process chunks in parallel
    with multiprocessing.Pool(processes=num_processes) as pool:
        # Use imap to get results as they complete
        for i, result in enumerate(pool.starmap(compute_chunk, args)):
            # Print progress
            progress = (i + 1) / total_chunks * 100
            print(f"Progress: {progress:.1f}% - {result}")
    
    print(f"Mandelbrot set calculation complete. Saved to {zarr_path}")
    return zarr_path

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <array_size> <chunk_size>")
        sys.exit(1)
    
    try:
        array_size = int(sys.argv[1])
        chunk_size = int(sys.argv[2])
        
        if array_size <= 0 or chunk_size <= 0:
            print("Error: Array size and chunk size must be positive")
            sys.exit(1)
            
        if chunk_size > array_size:
            print("Warning: Chunk size is larger than array size. Setting chunk size to array size.")
            chunk_size = array_size
        
        # Use all available CPU cores for computation
        num_processes = multiprocessing.cpu_count()
        
        # Generate the Mandelbrot set
        generate_mandelbrot_zarr(array_size, chunk_size, num_processes)
        
    except Exception as e:
        print(e)
        sys.exit(1)