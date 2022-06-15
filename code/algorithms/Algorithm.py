import random

def algorithm_random(chain):
    """
    Random algorithm that backtracks if aminochain gets stuck
    """
    wrong_option = ()

    while len(chain.folds) < len(chain.aminocode):

        # check previous coordinates in folds
        options = chain.get_options()
        while len(options) == 0:
            wrong_option = chain.folds[-1]
            chain.remove_last_point()
            options = chain.get_options() - {wrong_option}

        # find next coordinate random
        next_point = random.choice(list(options))
        chain.build(next_point)

    return chain
