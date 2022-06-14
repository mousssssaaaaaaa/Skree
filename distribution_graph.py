from code.algorithms import Algorithm as alg
import csv
import pandas as pd 
from sys import argv, exit
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out

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
        
        chain_result = alg.algorithm_random(chain)

        score_list.append(int(chain_result.get_score()))

        runs +=1

    highest_score = max(score_list)
    
    plt.hist(score_list)
    plt.ylabel("N")
    plt.xlabel("scores")
    plt.xticks(np.arange(0, (highest_score + 1), step=1))

    plt.savefig("graph.pdf")

distribution()

