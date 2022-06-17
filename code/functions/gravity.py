def get_gravity(folds):
    fold_list = folds
    print("The original list:" + str(fold_list))
    res = [sum(element) / len(fold_list) for element in zip(*fold_list)]
    print("The cumulative column mean is:" + str(res))
    return res
