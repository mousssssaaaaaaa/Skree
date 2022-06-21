import random
from code.functions import distance as d
from code.functions import gravity as g
from code.functions import distance_to_H as dh

def algorithm_random(chain):
    """
    Random algorithm that backtracks if aminochain gets stuck
    """
    wrong_option = ()

    while len(chain.folds) < len(chain.aminocode):

        # check previous coordinates in folds
        options = chain.get_options()
        if len(options) == 0:
            chain.folds = [(0, 0)]
        else:
            next_point = random.choice(list(options))
            chain.build(next_point)

    return chain

