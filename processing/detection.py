import numpy as np

def is_list(item):
    if isinstance(item, list) or isinstance(item, np.ndarray):
        return True
    else:
        return False

def contains_list(series):
    for item in series:
        if item is not None:
            return is_list(item)
        else:
            continue

    if series.dropna().empty:
        pass
    else:
        type(series.dropna().iloc[-1])

    return False

def all_strings(series):
    if series.dropna().empty:
        return False  # Consider an empty series after dropping NA as not all strings
    return all(isinstance(item, str) for item in series.dropna())