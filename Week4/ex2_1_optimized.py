import sys
import numpy as np

@profile
def distance_matrix(p1, p2):
    # Convert degrees to radians
    p1, p2 = np.radians(p1), np.radians(p2)
    
    # Initialize the distance matrix
    D = np.empty((len(p1), len(p2)))
    
    # Loop over the first set of points
    for i in range(len(p1)):
        # Compute differences in latitude and longitude using broadcasting
        dlat = p1[i, 0] - p2[:, 0]
        dlon = p1[i, 1] - p2[:, 1]
        
        # Haversine formula
        dsin2_lat = np.sin(0.5 * dlat) ** 2
        dsin2_lon = np.sin(0.5 * dlon) ** 2
        cosprod = np.cos(p1[i, 0]) * np.cos(p2[:, 0])
        a = dsin2_lat + cosprod * dsin2_lon
        
        # Compute the distance
        D[i, :] = 2 * np.arcsin(np.sqrt(a), np.sqrt(1 - a))
    
    # Multiply by Earth's radius to get the distance in kilometers
    D *= 6371
    
    return D


def load_points(fname):
    data = np.loadtxt(fname, delimiter=',', skiprows=1, usecols=(1, 2))
    return data


def distance_stats(D):
    # Extract upper triangular part to avoid duplicate entries
    assert D.shape[0] == D.shape[1], 'D must be square'
    idx = np.triu_indices(D.shape[0], k=1)
    distances = D[idx]
    return {
        'mean': float(distances.mean()),
        'std': float(distances.std()),
        'max': float(distances.max()),
        'min': float(distances.min()),
    }


fname = sys.argv[1]
points = load_points(fname)
D = distance_matrix(points, points)
stats = distance_stats(D)
print(stats)