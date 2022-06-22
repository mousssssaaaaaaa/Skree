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


        # score = int(chain_result.get_score())

        # m = max(score_list)

        # if score > m:
        #     best_chain = deepcopy(chain_result)

        # score_list.append(score)
        # plt.title("Random")

        " --------------------------------- Depth First ---------------------------------------- "
        # depth_first = df.DepthFirst(chain)
        # depth_first.run()

        # score = int(depth_first.chain.get_score())

        # m = max(score_list)

        # if score > m:
        #     best_chain = deepcopy(depth_first.chain)

        # score_list.append(score)
        # plt.title("Depth First")

        " -------------------------------- Greedy Distance ------------------------------------- "
        greedy_distance = gd.GreedyDistance(chain)
        greedy_distance.run()

        score = int(greedy_distance.chain.get_score())

        m = max(score_list)

        if score > m:
            best_chain = deepcopy(greedy_distance.chain)

        score_list.append(score)
        plt.title("Greedy distance")

        " --------------------------------- Greedy Gravity --------------------------------------- "
        # greedy_gravity = gg.GreedyGravity(chain)
        # greedy_gravity.run()

        # score = int(greedy_gravity.chain.get_score())

        # m = max(score_list)

        # if score > m:
        #     best_chain = deepcopy(greedy_gravity.chain)

        # score_list.append(score)
        # plt.title("Greedy Gravity")

    "-----------------------TODO -------------------------------------------"

    highest_score = max(score_list)

    bins = np.arange(highest_score + 2) - 0.5

    # create histogram and assign elements separately
    n, bin, patch = plt.hist(score_list, density=True)

    # # print values on top of patch
    # for bin_val in patch:
    #     x = (bin_val._x0 + bin_val._x1)/2 - 0.25
    #     y = bin_val._y1 + 0.005
    #     plt.text(x, y, bin_val._y1)

    plt.xticks(range(highest_score + 2))
    plt.ylabel("P")
    plt.xlabel("scores")
    
    plt.show()

    # save produced image
    plt.savefig("results/graph.png")
    plt.close()

    # visualize protein chain
    vis.visualisation(best_chain)

distribution()
