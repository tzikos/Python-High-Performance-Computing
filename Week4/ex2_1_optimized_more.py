import sys
import numpy as np

@profile
def distance_matrix(p1, p2):
    # Convert degrees to radians
    p1, p2 = np.radians(p1), np.radians(p2)
    
    # Extract latitude and longitude
    lat1, lon1 = p1[:, 0], p1[:, 1]
    lat2, lon2 = p2[:, 0], p2[:, 1]
    
    # Compute the difference in longitude
    dlon = lon1[:, np.newaxis] - lon2
    
    # Haversine formula using broadcasting
    dsin2_lat = np.sin(0.5 * (lat1[:, np.newaxis] - lat2)) ** 2
    dsin2_lon = np.sin(0.5 * dlon) ** 2
    cosprod = np.cos(lat1[:, np.newaxis]) * np.cos(lat2)
    a = dsin2_lat + cosprod * dsin2_lon
    
    # Compute the distance
    D = 2 * np.arcsin(np.sqrt(a))
    
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