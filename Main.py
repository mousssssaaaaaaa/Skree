
from sys import argv, exit
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out
from code.algorithms import Algorithm as alg
from code.algorithms import greedy_distance as algr
from code.algorithms import depth_first as algC

def main():
    if len(argv) != 2:
        print("Error not right amount arguments")
        exit(1)

    # capitalize argument input
    aminocode = list((argv[1]).upper())

    # build protein chain
    chain = ch.Chain(aminocode)
    chain_result = alg.algorithm_random(chain)

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
