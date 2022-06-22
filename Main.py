
from sys import argv, exit
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out
from code.algorithms import depth_first as df
from code.algorithms import random as rnd
from code.algorithms import greedy_distance as gd
from code.algorithms import greedy_gravity as gg

def main():
    if len(argv) != 2:
        print("Error not right amount arguments")
        exit(1)

    # capitalize argument input
    aminocode = list((argv[1]).upper())

    # build protein chain
    chain = ch.Chain(aminocode)


    " ---------------------------------- Random ------------------------------------------- "
    # chain_result = rnd.algorithm_random(chain)

    " --------------------------------- Depth First ---------------------------------------- "
    # depth_first = df.DepthFirst(chain)
    # depth_first.run()
    # chain_result = depth_first.chain

    " -------------------------------- Greedy Distance ------------------------------------- "
    # greedy_distance = gd.GreedyDistance(chain)
    # greedy_distance.run()
    # chain_result = greedy_distance.chain

    " --------------------------------- Greedy Gravity --------------------------------------- "
    # greedy_gravity = gg.GreedyGravity(chain)
    # greedy_gravity.run()
    # chain_result = greedy_gravity.chain

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
