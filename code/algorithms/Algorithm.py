import random
import math
from code.functions import distance as d

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

def algorithm_greedy(chain):
    wrong_option = ()

    while len(chain.folds) < len(chain.aminocode):

        # check previous coordinates in folds
        options = chain.get_options()
        while len(options) == 0:
            wrong_option = chain.folds[-1]
            chain.remove_last_point()
            options = chain.get_options() - {wrong_option}

        score = 100
        for point in random.shuffle(options):
            # close_H berekent afstand dichtsbijzijnde H
            distance = chain.close_H(point)
            if distance < score:
                best_point = point

        chain.build(best_point)

def algorithm_greedy_gravity():
    """
    Pick random coordinate as option on grid and
    see if proposed chain elongation is valid.
    """

    options = chain.get_options()
    while options == []:
        wrong_option = chain.folds[-1]
        chain.remove_last_point()
        options = chain.get_options() - set([wrong_option])

    score = 1
    gravity_value = gravity.get_gravity()
    for point in options:
        gravity_distance = d.distance(point, gravity_value)
        if gravity_distance:
            pass

    # find next coordinate random
    next_point = random.choice(options)
    chain.build(next_point)

    # if validate_option() == False:
    #     wrong_option = chain.folds[-1]
    #     chain.remove_last_point()
    #     options = chain.get_options() - set([wrong_option])
    #     next_point = random.choice(options) # ???
    #     chain.build(next_point) # ???
