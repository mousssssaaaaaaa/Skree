import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sys import argv, exit
from copy import deepcopy
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out
from code.algorithms import depth_first as df
from code.algorithms import random as rnd
from code.algorithms import greedy_distance as gd
from code.algorithms import greedy_gravity as gg

def distribution():
    if len(argv) != 3:
        print("Error not right amount arguments")
        exit(1)

    # capitalize argument input
    aminocode = list((argv[1]).upper())

    # store number of runs
    n = int(argv[2])

    # create list for scores
    score_list = [-1]

    # best chain to save
    best_chain = ch.Chain('')

    for runs in range(n):

        # build protein chain
        chain = ch.Chain(aminocode)

        " ---------------------------------- Random ------------------------------------------- "
        # chain_result = rnd.algorithm_random(chain)
<<<<<<< HEAD

        # score = int(chain_result.get_score())

        # m = max(score_list)

        # if score > m:
        #     best_chain = deepcopy(chain_result)

=======
        #
        # score = int(chain_result.get_score())
        #
        # m = max(score_list)
        #
        # if score > m:
        #     best_chain = deepcopy(chain_result)
        #
>>>>>>> 76909bb36069f0074e13b9239da6872698d2c6e8
        # score_list.append(score)

        " --------------------------------- Depth First ---------------------------------------- "
        # depth_first = df.DepthFirst(chain)
        # depth_first.run()

        # score = int(depth_first.chain.get_score())

        # m = max(score_list)

        # if score > m:
        #     best_chain = deepcopy(depth_first.chain)

        # score_list.append(score)

        " -------------------------------- Greedy Distance ------------------------------------- "
        greedy_distance = gd.GreedyDistance(chain)
        greedy_distance.run()

        score = int(greedy_distance.chain.get_score())

        m = max(score_list)

        if score > m:
            best_chain = deepcopy(greedy_distance.chain)

        score_list.append(score)

        " --------------------------------- Greedy Gravity --------------------------------------- "
        # greedy_gravity = gg.GreedyGravity(chain)
        # greedy_gravity.run()

        # score = int(greedy_gravity.chain.get_score())

        # m = max(score_list)

        # if score > m:
        #     best_chain = deepcopy(greedy_gravity.chain)

        # score_list.append(score)

    "-----------------------TODO -------------------------------------------"
    # # TODO: show max values if to small to see
    # count_score = 0
    # for i in score_list:
    #     if i > max(score_list):

    #         print("scatter")
    #         # visualize protein chain
    #         vis.visualisation(chain_result)

    #         count_score += 1


    highest_score = max(score_list)

    bins = np.arange(highest_score + 2) - 0.5

    # create histogram and assign elements separately
    n, bin, patch = plt.hist(score_list, density=True)

    # print values on top of patch
    for bin_val in patch:
        x = (bin_val.xy[0] + (bin_val.xy[0] + bin_val._width))/2 - 0.25
        y = bin_val._height + 0.005
        plt.text(x, y, bin_val._height)

    plt.xticks(range(highest_score + 2))
    plt.ylabel("P")
    plt.xlabel("scores")
    plt.title("Depth first")
    #plt.show()

    # save produced image
    plt.savefig("results/graph.png")
    plt.close()

    # visualize protein chain
    vis.visualisation(best_chain)

distribution()
