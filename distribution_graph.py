from code.algorithms import Algorithm as alg
import csv
import pandas as pd 
from sys import argv, exit
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out
from code.algorithms import greedy_lookahead as greed

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
    score_list = []

    runs = 0 
    while runs < n:
        # build protein chain
        chain = ch.Chain(aminocode)
        
        chain_result = greed.greedy_lookahead(chain)
        
        score_list.append(int(chain_result.get_score()))

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
    plt.ylabel("P(scores)")
    plt.xlabel("scores")
    plt.title('Depth first')
    plt.savefig("graph.png")

distribution()
