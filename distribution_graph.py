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
from code.algorithms import hill_climber as hc

def distribution():
    if len(argv) != 3:
        print("Error not right amount arguments")
        exit(1)

    # capitalize argument input
    aminocode = list((argv[1]).upper())

    # store number of runs
    n = int(argv[2])

    # create list for scores
    score_list = []

    # best chain to save
    best_chain = ch.Chain('')

    for runs in range(n):

        # build protein chain
        chain = ch.Chain(aminocode)

    #     " ---------------------------------- Random -------------------------- "
    #     chain_result = rnd.algorithm_random(chain)
    #
    #     score = int(chain_result.get_score())
    #
    #     m = max(score_list)
    #
    #     if score > m:
    #         best_chain = deepcopy(chain_result)
    #
    #     score_list.append(score)
    #     plt.title("Random")
    #
    # np.savetxt("results/scores_random.csv", score_list, delimiter =", ", fmt ='% s')

        " ---------------------------------- Random ------------------------------------------- "
        # chain_result = rnd.algorithm_random(chain)

        # score = int(chain_result.get_score())

        # m = max(score_list or [0])

        # if score > m:
        #     best_chain = deepcopy(chain_result)

        # score_list.append(score)
        # plt.title("Random")

        " --------------------------------- Depth First ---------------------------------------- "
        # depth_first = df.DepthFirst(chain)
        # depth_first.run()

        # score = int(depth_first.chain.get_score())

        # " --------------------------------- Depth First ---------------------- "
        # depth_first = df.DepthFirst(chain)
        # depth_first.run()

        # score = int(depth_first.chain.get_score())

        " -------------------------------- Greedy Distance ------------------------------------- "
        # greedy_distance = gd.GreedyDistance(chain)
        # greedy_distance.run()

        # score = int(greedy_distance.chain.get_score())

        # m = max(score_list)

    #     if score > m:
    #         best_chain = deepcopy(depth_first.chain)
    #
    #     score_list.append(score)
    #     plt.title("Depth First")
    #
    # np.savetxt("results/scores_depth.csv", score_list, delimiter =", ", fmt ='% s')


        # " -------------------------------- Greedy Distance ------------------- "
    #     greedy_distance = gd.GreedyDistance(chain)
    #     greedy_distance.run()
    #
    #     score = int(greedy_distance.chain.get_score())
    #
    #     m = max(score_list)
    #
    #     if score > m:
    #         best_chain = deepcopy(greedy_distance.chain)
    #
    #     score_list.append(score)
    #     plt.title("Greedy distance")
    #
    # np.savetxt("results/scores_distance.csv", score_list, delimiter =", ", fmt ='% s')

        # " --------------------------------- Greedy Gravity ------------------- "
    #     greedy_gravity = gg.GreedyGravity(chain)
    #     greedy_gravity.run()
    #
    #     score = int(greedy_gravity.chain.get_score())
    #
    #     m = max(score_list)
    #
    #     if score > m:
    #         best_chain = deepcopy(greedy_gravity.chain)
    #
    #     score_list.append(score)
    #     plt.title("Greedy Gravity")
    #
    # np.savetxt("results/scores_gravity.csv", score_list, delimiter =", ", fmt ='% s')


        " ---------------- Hill Climber ---------------"
        chain_result = hc.algorithm_hill_climber(chain, 5, 100) 
        plt.title("Hill Climber")
        score = int(chain_result.get_score())

        m = max(score_list or [0])

        if score > m:
            best_chain = deepcopy(chain_result)

        score_list.append(score)

        " --------------------------------- Greedy Gravity --------------------------------------- "
        # greedy_gravity = gg.GreedyGravity(chain)
        # greedy_gravity.run()

        # score = int(greedy_gravity.chain.get_score())

        # m = max(score_list or [0])

        # if score > m:
        #     best_chain = deepcopy(chain_result)
        #
        # score_list.append(score)

    # "-----------------------TODO --------------------------------------------- "

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

    # plt.show()

    # save produced image
    plt.savefig("results/graph.png")
    plt.close()

    # visualize protein chain
    vis.visualisation(best_chain)

distribution()
