def sorttuples(arr):
    """
    Returns a list of tuples sorted by the last element of each tuple.
    """
    return sorted(arr, key=lambda x: x[-1])
