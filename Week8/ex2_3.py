import numpy as np
import matplotlib.pyplot as plt
import sys

def downsample_mandelbrot(input_file, array_size, step):
    """
    Read a memory-mapped Mandelbrot array, downsample it, and save as PNG.
    
    Parameters:
    - input_file: Path to the raw Mandelbrot array file
    - array_size: Size N of the NxN array
    - step: Integer step length (take every nth row and column)
    """
    # Open the memory-mapped array
    mandelbrot_array = np.memmap(input_file, dtype='int32', mode='r', shape=(array_size, array_size))
    
    # Downsample by taking every nth row and column
    downsampled = mandelbrot_array[::step, ::step]
    
    # Create the plot and save as PNG
    # plt.figure(figsize=(10, 10))
    # plt.imshow(downsampled, cmap='hot', extent=(-2, 2, -2, 2))
    # plt.axis('off')
    
    # Generate output filename based on input and step size
    output_file = f"mandelbrot_downsampled_{step}.png"
    plt.imsave(output_file, arr = downsampled)
    print(f"Downsampled image saved as {output_file}")
    
    # Close the figure to free memory
    plt.close()

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 4:
        print(f"Usage: python {sys.argv[0]} <input_file> <array_size> <step_size>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    array_size = int(sys.argv[2])
    step_size = int(sys.argv[3])
    
    # Validate arguments
    if step_size < 1:
        print("Error: Step size must be positive")
        sys.exit(1)
    
    try:
        downsample_mandelbrot(input_file, array_size, step_size)
    except FileNotFoundError:
        print(f"Error: Could not find the input file {input_file}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)