import numpy as np
import sys

def cli_to_numpy_mat(*args):

    x = list(sys.argv[1:])
    x = np.array(x, dtype=float)
    x = np.diag(x)
    np.save('numpy_mat.npy', x)

    return None

if __name__ == '__main__':
    cli_to_numpy_mat()
