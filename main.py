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
    print("Welcome to Protein Po(w)der, fill in the following variables to get solutions.")
    print("Enter a chain combination, consisting of Cysteines (C), polar (P), and hydrophobic (H) amino acids.")
    aminocode = input("Chain: ").upper()

    # Ask for algorithm
    print("Pick a number to choose an algorithm: (1) Random, (2) Depth First, (3) Greedy Distance, (4) Greedy Gravity, (5) Hill Climber or (6) Simulated Annealing.")
    algorithm = int(input("Algorithm: "))

    # Ask for amount of dimensions
    print("How many dimensions can the chain occupy? Choose either 2 and 3.")
    dimensions = int(input("Dimensions: "))

    # Ask for iterations
    print("How many iterations should the algorithm run?")
    iterations = int(input("Iterations: "))

    # Use algoritm to create results
    best_chain, chain_result = his.distribution(aminocode, dimensions, algorithm,
                                                iterations)

    # Store protein data into csv for the best chain
    out.outputwriter(best_chain.folds, aminocode, chain_result)

    # Ask if user wants to see interactive plot
    print("State if an interactive plot should be shown? (1) for yes, and (0) for no.")
    interactive = int(input("Interactivity: "))
    if interactive == 1:
        dim.twisting_plot(best_chain)

    # Print end statement
    print("Program has ended, see the results folder for the results!")

if __name__ == "__main__":
    main()
