import numpy as np
import sys

def np_mat_to_avgs(*args):
    
    path = sys.argv[1]
    print(path)
    mat = np.load(path)
    mat = mat.astype(np.float64)
    avg_rows = np.average(mat, axis = 1)
    avg_cols = np.average(mat, axis = 0)

    np.save('cols.npy', avg_cols)
    np.save('rows.npy', avg_rows)
    
    return None

if __name__ == '__main__':
    np_mat_to_avgs()