
from sys import argv, exit
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out
from code.algorithms import depth_first as df
from code.algorithms import random as rnd
from code.algorithms import greedy_distance as gd
from code.algorithms import greedy_gravity as gg
from code.algorithms import hill_climber as hc
from code.visualisation import distribution_graph as his
from code.visualisation import visualisation as dim

def main():    
    # Ask user for input chain
    print("Welcome to Protein Po(w)der, fill in the following variables to get solutions")
    aminocode = input("Chain: ").upper()

    # Ask for algorithm
    algorithm = int(input("Pick a number to choose an algoritm: (1) Random, (2) Depth First, (3) Greedy Distance, (4) Greedy Gravity, (5) Hill Climber or (6) Simulated Annealing \n"))

    # Ask for amount of dimensions
    dimensions = int(input("How many dimensions can the chain occupy (choose between 2 and 3)?\n"))

    # Ask for iterations 
    iterations = int(input("How many iterations should the algoritm run?\n"))

    # Use algoritm to create results
    best_chain, chain_result = his.distribution(aminocode, dimensions, algorithm, iterations)
    
    # Store protein data into csv for the best chain
    out.outputwriter(best_chain.folds, aminocode, chain_result)

    # Ask if user wants to see interactive plot
    interactive = int(input("State if the interactive plot should be printed? (1) for yes and  (0) for no \n"))
    if interactive == 1:
        dim.twisting_plot(best_chain)
    
    # Print end statement
    print("Program has ended, see the results folder for the results!")

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
