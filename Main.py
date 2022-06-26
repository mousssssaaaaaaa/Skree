
from sys import argv, exit
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out
from code.algorithms import depth_first as df
from code.algorithms import random as rnd
from code.algorithms import greedy_distance as gd
from code.algorithms import greedy_gravity as gg
from code.algorithms import hill_climber as hc


def main():

    # Ask user for input chain
    print("Welcome to Protein Po(w)der, fill in the following variables to get solutions")
    aminocode = input("Chain: ")

    # Ask for algorithm
    algoritm = int(input("Pick a number to choose an algoritm: (1) Random, (2) Depth First, (3) Greedy Distance, (4) Greedy Gravity, (5) Hill Climber \n"))

    # Build protein chain
    chain = ch.Chain(aminocode)

    # Perform choosen algoritm
    if algoritm == 1:
        #---------------------------------- Random ------------------------------------------- 
        chain_result = rnd.algorithm_random(chain)

    elif algoritm == 2: 
        #--------------------------------- Depth First ----------------------------------------
        depth_first = df.DepthFirst(chain)
        depth_first.run()
        chain_result = depth_first.chain

    elif algoritm == 3: 
        #-------------------------------- Greedy Distance --------------------------------------
        greedy_distance = gd.GreedyDistance(chain)
        greedy_distance.run()
        chain_result = greedy_distance.chain
    
    elif algoritm == 4: 
        #--------------------------------- Greedy Gravity ---------------------------------------
        greedy_gravity = gg.GreedyGravity(chain)
        greedy_gravity.run()
        chain_result = greedy_gravity.chain
    
    else: 
        #--------------------------------- Hill Climber -----------------------------------------
        chain_result = hc.algorithm_hill_climber(chain, 7, 1000)    

    # visualize protein chain
    vis.visualisation(chain_result)

    # store protein data into csv
    out.outputwriter(chain_result.folds, aminocode, chain_result)

if __name__ == "__main__":
    main()

"""
HHPHHHPHPHHHPH
HPHPPHHPHPPHPHHPPHPH
PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP
HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH
"""

"""
PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP

CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC

HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH

HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH
"""