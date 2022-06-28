import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sys import argv, exit
from copy import deepcopy
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out
from code.algorithms import random as rnd
from code.algorithms import greedy_distance as gd
from code.algorithms import greedy_gravity as gg
from code.algorithms import depth_first as df
from code.algorithms import hill_climber as hc
from code.algorithms import hill_climber_gravity as hcg
from code.algorithms import simulated_annealing as sa

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
    best_chain = ch.Chain('', 3)

    for runs in range(n):

        # build protein chain
        chain = ch.Chain(aminocode, 3)

        # " ---------------------------------- Random -------------------------- "
        # chain_result = rnd.algorithm_random(chain)
        # best_chain = chain_result

        # score = int(chain_result.get_score())
        # m = max(score_list or [0])

        # if score > m:
        #     best_chain = deepcopy(chain_result)
        #     print(best_chain)

        # score_list.append(score)
        # print(score_list)
        # plt.title("Random")

        # " -------------------------------- Greedy Distance ------------------------------------- "
        # greedy_distance = gd.GreedyDistance(chain)
        # greedy_distance.run()
        # chain_result = greedy_distance.chain
        # best_chain = chain_result
        #
        # score = int(greedy_distance.chain.get_score())
        # m = max(score_list or [0])
        #
        # if score > m:
        #     best_chain = deepcopy(greedy_distance.chain)
        #
        # score_list.append(score)
        # plt.title("Greedy Distance")

        # " --------------------------------- Greedy Gravity ------------------- "
        # greedy_gravity = gg.GreedyGravity(chain)
        # greedy_gravity.run()
        #
        # score = int(greedy_gravity.chain.get_score())
        #
        # m = max(score_list or [0])
        #
        # if score > m:
        #     best_chain = deepcopy(greedy_gravity.chain)
        #
        # score_list.append(score)
        # plt.title("Greedy Gravity")

        " --------------------------------- Depth First ---------------------------------------- "
        print("Run:", runs)
        depth_first = df.DepthFirst(chain)
        depth_first.run()

        score = int(depth_first.chain.get_score())
        m = max(score_list or [0])

        if score > m:
            best_chain = deepcopy(depth_first.chain)

        score_list.append(score)
        plt.title("Depth First")

        # " --------------------------------- Hill Climber --------------------------------------- "
        # chain_result = hc.algorithm_hill_climber(chain, 7, 1000) # optional hill climber: chain_start
        # plt.title("Hill Climber")
        #
        # score = int(chain_result.get_score())
        # m = max(score_list or [0])
        #
        # if score > m:
        #     best_chain = deepcopy(chain_result)
        #
        # score_list.append(score)
        # plt.title("Hill Climber")

        # " --------------------------------- Hill Climber Gravity --------------------------------------- "
        # chain_result, chain_start = hcg.algorithm_hill_climber(chain, 7, 1000)
        # plt.title("Hill Climber Gravity")
        #
        # score = int(chain_result.get_score())
        # m = max(score_list or [0])
        #
        # if score > m:
        #     best_chain = deepcopy(chain_result)
        #
        # score_list.append(score)
        # plt.title("Hill Climber")

        # " --------------------------------- Simulated Annealing --------------------------------------- "
        # chain_result = sa.algorithm_simulated_annealing(chain, 7, 1000)
        # score = int(chain_result.get_score())
        #
        # m = max(score_list or [0])
        #
        # if score > m:
        #     best_chain = deepcopy(chain_result)
        #
        # score_list.append(score)
        # plt.title("Simulated Annealing")

    # np.savetxt("results/scores_random.csv", score_list, delimiter = ", ", fmt = '% s')
    # np.savetxt("results/scores_distance.csv", score_list, delimiter = ", ", fmt = '% s')
    # np.savetxt("results/scores_gravity.csv", score_list, delimiter = ", ", fmt = '% s')
    np.savetxt("results/scores_depth.csv", score_list, delimiter = ", ", fmt = '% s')
    # np.savetxt("results/scores_hill_climber.csv", score_list, delimiter = ", ", fmt = '% s')
    # np.savetxt("results/scores_hill_climber_gravity.csv", score_list, delimiter = ", ", fmt = '% s')
    # np.savetxt("results/scores_simulated_annealing.csv", score_list, delimiter = ", ", fmt = '% s')

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

    plt.show()

    # save produced image
    plt.savefig("results/graph.png")
    plt.close()

    # # visualize start before hill climber
    # vis.visualisation(chain_start)

    # visualize protein chain
    vis.visualisation(best_chain)


distribution()
