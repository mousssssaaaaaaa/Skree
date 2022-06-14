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

        # while len(chain.folds) < len(aminocode):
        #     chain.build()
        
        chain_result = alg.algorithm_random(chain)

        score_list.append(int(chain_result.get_score()))

        runs +=1


    score_dict= {}

    # count scores
    for index in range(len(score_list)):
        if score_list[index] in score_dict.keys():
            score_dict[score_list[index]] +=1 
        else: 
            score_dict[score_list[index]] = 1
            pass

    print(score_dict)

    scores = list(score_dict.keys())
    N = list(score_dict.values())
    
    plt.plot(N, scores)
    plt.xlabel("N")
    plt.ylabel("scores")

    plt.savefig("graph.pdf")
    # # create empty dataframe
    # df = pd.DataFrame([score_dict])
    # # add results to dataframe/ csv 
    # # df['score'] = score_list
    # df.to_csv('csv/graph.csv', index=False)


distribution()

