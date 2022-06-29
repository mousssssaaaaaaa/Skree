def get_gravity(folds):
    """
    Calculate center of gravity of current chain sequence.
    """
    fold_list = folds
    res = [sum(element) / len(fold_list) for element in zip(*fold_list)]

    return res
