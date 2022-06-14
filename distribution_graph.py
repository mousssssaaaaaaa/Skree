import csv
import pandas as pd 
from sys import argv, exit
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out

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

        while len(chain.folds) < len(aminocode):
            chain.build()

        score_list.append(int(chain.get_score()))

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

    # create empty dataframe
    df = pd.DataFrame()
    
    # add results to dataframe/ csv 
    df['score'] = score_list

    df.to_csv('csv/graph.csv', index= True)


distribution()
