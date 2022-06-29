import random
from code.algorithms import random as rnd
from copy import deepcopy
from code.classes import chain as ch
from code.algorithms import greedy_gravity as gg
from code.functions import distance as d
from code.functions import gravity as g


def algorithm_hill_climber(chain, n_flips, N):
    """
    Hill climber algorithm that starts with random
    """

    print("Initiate Hill Climber Gravity")
    # Run a random algorithm to get starting point
    chain = rnd.algorithm_random(chain)
    chain_start = deepcopy(chain)

    baseline_score = chain.get_score()
    copy_chain = deepcopy(chain)
    fails = 0

    # Run until no improvements
    while fails < N:

        flips = 0
        random_point_index = random.randint(0,len(copy_chain.folds)-1)
        random_point = copy_chain.folds[random_point_index]

        # Flip parts of chain
        for _ in range(n_flips):
            # Choose a random point


            # Check if not last chain point
            if random_point_index <= (len(chain.folds) - n_flips):

                # Find next point
                next_point = copy_chain.folds[random_point_index + 2]

                # Find middle point
                middle = list(copy_chain.folds[random_point_index + 1])
                middle_old = middle

                dif_end_x = next_point[0] - random_point[0]
                dif_end_y = next_point[1] - random_point[1]
                dif_end_z = next_point[2] - random_point[2]

                differences_end = (dif_end_x, dif_end_y, dif_end_z)

                # check which dimension to ignore
                if dif_end_x == 0:
                    dim1 = 1
                    dim2 = 2

                elif dif_end_y == 0:
                    dim1 = 0
                    dim2 = 2

                else:
                    dim1 = 0
                    dim2 = 1

                # Check if not straight line (if only one coordinate)
                if differences_end[dim1] != 0 and differences_end[dim2] != 0:

                    # Calculate coordinates new point (invert change):

                    dif_middle_dim1 = middle[dim1] - random_point[dim1]

                    if dif_middle_dim1 == differences_end[dim1]:
                        middle[dim1] = random_point[dim1]
                        middle[dim2] = random_point[dim2] + differences_end[dim2]
                    else:
                        middle[dim1] = random_point[dim1] + differences_end[dim1]
                        middle[dim2] = random_point[dim2]

                # V2: calculate center of gravity for current protein
                gravity_value = g.get_gravity(copy_chain.folds)

                # V2: Calculate distance before and after flip
                gravity_distance_old = d.distance(middle_old, gravity_value)
                gravity_distance_new = d.distance(middle, gravity_value)

                # V2: Check if point moves closer
                if (gravity_distance_old > gravity_distance_new) and (tuple(middle) not in copy_chain.folds):
                    print("I can fold!")
                    copy_chain.folds[random_point_index + 1] = tuple(middle)

                # # Check if point in fold
                # if tuple(middle) not in copy_chain.folds:
                #     copy_chain.folds[random_point_index + 1] = tuple(middle)

                random_point = copy_chain.folds[random_point_index + 1]
                random_point_index += 1

        # Compare score to baseline
        if copy_chain.get_score() > baseline_score:
            chain = deepcopy(copy_chain)
            baseline_score = chain.get_score()
        else:
            fails += 1

    return chain, chain_start
