import random
import math
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

def algorithm_greedy_gravity(chain):
    """
    Pick random coordinate as option on grid and
    see if proposed chain elongation is valid.
    """

    while len(chain.folds) < len(chain.aminocode):

        options = chain.get_options()

        if len(options) == 0:
            chain.folds = [(0, 0, 0)]

        if len(chain.folds) < 6:
            next_point = random.choice(list(options))
            chain.build(next_point)
        else:
            score = 100

            # calculate center of gravity for current protein
            gravity_value = g.get_gravity(chain.folds)

            # calculate distance (Pythagoras)
            for point in options:
                gravity_distance = d.distance(point, gravity_value)
                if gravity_distance < score:
                    score = gravity_distance
                    best_point = point
            chain.build(best_point)
    return chain
