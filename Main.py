
from sys import argv, exit
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out
from code.algorithms import Algorithm as alg
<<<<<<< HEAD
from code.algorithms import algorithm_greedy as algB
=======
from code.algorithms import algorithm_greedy as algr
from code.algorithms import greedy_lookahead as algC
>>>>>>> 1f93ba0739feb9f31838dc4d63d617e7492847c7

def main():
    if len(argv) != 2:
        print("Error not right amount arguments")
        exit(1)

    # capitalize argument input
    aminocode = list((argv[1]).upper())

    # build protein chain
    chain = ch.Chain(aminocode)
<<<<<<< HEAD
    chain_result = alg.algorithm_greedy_gravity(chain)
    print(chain.folds)
=======
    chain_result = algC.greedy_lookahead(chain)
>>>>>>> 1f93ba0739feb9f31838dc4d63d617e7492847c7

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
