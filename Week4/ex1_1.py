def standardize_rows(data, mean, std):
    
    output = (data - mean) / std
    return output