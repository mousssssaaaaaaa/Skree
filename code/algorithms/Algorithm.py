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



        # find next coordinate random


    return chain

def algorithm_greedy(chain):
    wrong_option = ()

    # check if first aminocode is H and add
    if chain.aminocode[0] == 'H':
        chain.hydrophobe.append((0,0))


    while len(chain.folds) < len(chain.aminocode):

        # check previous coordinates in folds
        options = chain.get_options()
        while len(options) == 0:
            wrong_option = chain.folds[-1]
            chain.remove_last_point()
            options = chain.get_options() - {wrong_option}

        score = 100
        best_point = random.choice(list(options))

        #print(best_point)
        if len(chain.hydrophobe) != 0:

            list_H = chain.hydrophobe.copy()
            # remove current point from hydrophobe list
            if chain.folds[-1] in chain.hydrophobe:
                list_H.remove(chain.folds[-1])

            # check all options for best score
            index_to_check = len(chain.folds) - 1
            aminocode = chain.aminocode[index_to_check]
            if len(list_H) != 0 and aminocode != 'H':
                for point in options:
                    distance = dh.distance_to_H(point, list_H)
                    if distance < score:
                        best_point = point
                        score = distance

        chain.build(best_point)

        # add if H to list
        if chain.aminocode[index_to_check + 1] == 'H':
            chain.hydrophobe.append(best_point)

    return chain

def algorithm_greedy_gravity(chain):
    """
    Pick random coordinate as option on grid and
    see if proposed chain elongation is valid.
    """
    wrong_option = ()

    while len(chain.folds) < len(chain.aminocode):

        options = chain.get_options()

        while options == []:
            wrong_option = chain.folds[-1]
            chain.remove_last_point()
            options = chain.get_options() - set([wrong_option])

        if len(chain.folds) < 6:
            next_point = random.choice(list(options))
            chain.build(next_point)
        else:
            score = 100
            # bereken zwaartepunt van huidige eiwit
            gravity_value = g.get_gravity(chain.folds)
            # bereken afstand (Pythagoras)
            for point in options:
                gravity_distance = d.distance(point, gravity_value)
                if gravity_distance < score:
                    score = gravity_distance
                    best_point = point
            chain.build(best_point)
    return chain
