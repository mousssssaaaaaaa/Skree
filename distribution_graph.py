import pickle
import csv
import pandas as pd 
from sys import argv, exit
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out
from copy import deepcopy
from code.algorithms import depth_first as df
from code.algorithms import Algorithm as alg
from code.algorithms import greedy_distance as gd

import numpy as np
import matplotlib.pyplot as plt


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

    runs = 0 
    best_chain = ch.Chain('')
    
    while runs < n:
        # build protein chain
        chain = ch.Chain(aminocode)
        
        chain_result = df.depth_first(chain)
        
        score = int(chain_result.get_score())

        m = max(score_list)

        if score >= m:
            best_chain = deepcopy(chain_result)

        score_list.append(score)
        
        runs +=1
        
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
    plt.hist(score_list, bins, density=True)
    plt.xticks(range(highest_score + 2))
    plt.ylabel("P")
    plt.xlabel("scores")

    plt.title("Depth first")

    plt.savefig("graph.png")
    plt.close()

    # visualize protein chain
    vis.visualisation(best_chain)

distribution()
