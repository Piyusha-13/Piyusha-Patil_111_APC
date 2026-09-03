


def mean(values):
    if not values:
        raise ValueError("Cannot calculate the mean of an empty list.")
    return sum(values) / len(values)


def maximum(values):
    if not values:
        raise ValueError("Cannot find the maximum of an empty list.")
    return max(values)


def minimum(values):
    if not values:
        raise ValueError("Cannot find the minimum of an empty list.")
    return min(values)
