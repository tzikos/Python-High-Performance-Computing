import numpy as np
import sys

def magnitude_cli(*args):
    args_list = list(sys.argv[1:])
    x = np.array(args_list, dtype=float)

    return np.sqrt(np.sum(x**2))


if __name__ == '__main__':
    print(magnitude_cli())