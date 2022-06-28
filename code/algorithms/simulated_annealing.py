import random
from code.algorithms import random as rnd
from copy import deepcopy
from code.classes import chain as ch
from code.algorithms import greedy_gravity as gg
from code.functions import gravity as g
from code.visualisation import visualisation as vis


def algorithm_simulated_annealing(chain, n_flips, N):
    """
    Simulated Annealing algorithm that starts with Greedy Gravity
    """

    # Run a random algoritm to get starting point
    greedy_gravity = gg.GreedyGravity(chain)
    greedy_gravity.run()
    chain = greedy_gravity.chain

    baseline_score = chain.get_score()
    copy_chain = deepcopy(chain)
    fails = 0

    # Introduce temperature and alpha
    temp = 1
    alpha = 0.85

    # Run until no improvements
    while fails < N:

        flips = 0

        # Choose a random point
        random_point_index = random.randint(0,len(copy_chain.folds)-1)
        random_point = copy_chain.folds[random_point_index]

        # Flip parts of chain
        for _ in range(n_flips):

            # Check if not last chain point
            if random_point_index <= (len(chain.folds) -n_flips):

                # Find next point
                next_point = copy_chain.folds[random_point_index + 2]

                # Find middle point
                middle = list(copy_chain.folds[random_point_index + 1])

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

                # Check if point in fold
                if tuple(middle) not in copy_chain.folds:
                    copy_chain.folds[random_point_index + 1] = tuple(middle)

                random_point = copy_chain.folds[random_point_index + 1]
                random_point_index += 1

        # Set score to compare to baseline
        current_score = copy_chain.get_score() 
        print(current_score)

        if temp < 0.09:
            temp = 0.09

        probability = 2 ** ((baseline_score - current_score)/ temp)
        #print(baseline_score)
        

        if baseline_score - current_score == 0:
            probability = temp

        # Accept if better or accept some bad solutions depending on the current temperature.
        if  probability > random.random():
            chain = deepcopy(copy_chain)
            baseline_score = chain.get_score()
        else:
            fails += 1
        
        # Lower temperature 
        temp = temp * alpha

    return chain