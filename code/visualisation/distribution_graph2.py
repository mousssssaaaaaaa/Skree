import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sys import argv, exit
from copy import deepcopy
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out
from code.algorithms import depth_first as df
from code.algorithms import random as rnd
from code.algorithms import greedy_distance as gd
from code.algorithms import greedy_gravity as gg
from code.algorithms import hill_climber as hc
from code.algorithms import simulated_annealing as sa

def distribution2(aminocode, dimensions, algorithm, iterations):
    """
    The distribution functions runs the algoritms for given amount of runs and collects the results.
    """

    # Store number of runs
    n = iterations

    # Create list for scores
    score_list = []

    # Best chain to save
    best_chain = ch.Chain('', dimensions)

    # Perform choosen algoritm
    if algorithm == 1:
        for runs in range(n):

            # Build protein chain
            chain = ch.Chain(aminocode, dimensions)

            # Run Random 
            chain_result = rnd.algorithm_random(chain)
            best_chain = chain_result

            score = int(chain_result.get_score())
            m = max(score_list or [0])
            
            if score > m:
                best_chain = deepcopy(chain_result)
            
            score_list.append(score)
            plt.title("Random")

    elif algorithm == 2:
        for runs in range(n):

            # Build protein chain
            chain = ch.Chain(aminocode, dimensions)

            # Run Depth First 
            depth_first = df.DepthFirst(chain)
            depth_first.run()
            chain_result = depth_first.chain
            best_chain = chain_result
            
            score = int(depth_first.chain.get_score())
            m = max(score_list or [0])
            
            if score > m:
                best_chain = deepcopy(depth_first.chain)
            
            score_list.append(score)
            plt.title("Depth First")

    elif algorithm == 3:
        for runs in range(n):

            # Build protein chain
            chain = ch.Chain(aminocode, dimensions)

            # Run Greedy Distance 
            greedy_distance = gd.GreedyDistance(chain)
            greedy_distance.run()
            chain_result = greedy_distance.chain
            best_chain = chain_result
            
            score = int(greedy_distance.chain.get_score())
            m = max(score_list)
            
            if score > m:
                best_chain = deepcopy(greedy_distance.chain)
            
            score_list.append(score)
            plt.title("Greedy Distance")

    elif algorithm == 4:
        for runs in range(n):

            # build protein chain
            chain = ch.Chain(aminocode, dimensions)
      
            # Run Greedy Gravity 
            greedy_gravity = gg.GreedyGravity(chain)
            greedy_gravity.run()
            chain_result = greedy_gravity.chain
            best_chain = chain_result

            score = int(greedy_gravity.chain.get_score())
            
            m = max(score_list)
            
            if score > m:
                best_chain = deepcopy(greedy_gravity.chain)
            
            score_list.append(score)
            plt.title("Greedy Gravity")

    elif algorithm == 5:
        for runs in range(n):

            # build protein chain
            chain = ch.Chain(aminocode, dimensions)

            # Run Hill Climber 
            chain_result = hc.algorithm_hill_climber(chain, 7, 1000)
            best_chain = chain_result
        
            score = int(chain_result.get_score())
            m = max(score_list or [0])
            
            if score > m:
                best_chain = deepcopy(chain_result)
            
            score_list.append(score)
            plt.title("Hill Climber")

    elif algorithm == 6:
        for runs in range(n):
            print(runs)

            # Build protein chain
            chain = ch.Chain(aminocode, dimensions)

            # Run Simulated Annealing 
            chain_result = sa.algorithm_simulated_annealing(chain, 9, 100)
            score = int(chain_result.get_score())
            best_chain = chain_result
            
            m = max(score_list or [0])
            
            if score > m:
                best_chain = deepcopy(chain_result)

            score_list.append(score)
            plt.title("Simulated Annealing")

    # Save scores of every run 
    if algorithm == 1:
        np.savetxt("results/scores_random.csv", score_list, delimiter =", ", fmt ='% s')
    if algorithm == 2:
        np.savetxt("results/scores_depth.csv", score_list, delimiter =", ", fmt ='% s')
    if algorithm == 3:
        np.savetxt("results/scores_distance.csv", score_list, delimiter =", ", fmt = '% s')
    if algorithm == 4:
        np.savetxt("results/scores_gravity.csv", score_list, delimiter =", ", fmt ='% s')
    if algorithm == 5:
        np.savetxt("results/scores_hill_climber.csv", score_list, delimiter =", ", fmt ='% s')
    if algorithm == 6:
        np.savetxt("results/scores_simulated_annealing.csv", score_list, delimiter =", ", fmt ='% s')

    # Save highest scores
    highest_score = max(score_list)

    # Create histogram and assign elements separately
    bins = np.arange(highest_score + 2) - 0.5
    n, bin, patch = plt.hist(score_list, density=True)

    # Print values on top of patch
    for bin_val in patch:
        x = (bin_val.xy[0] + (bin_val.xy[0] + bin_val._width))/2 - 0.25
        y = bin_val._height + 0.005
        plt.text(x, y, bin_val._height)

    # Show labels
    plt.xticks(range(highest_score + 2))
    plt.ylabel("P")
    plt.xlabel("scores")

    # Save produced image
    plt.savefig("results/graph.png")

    # Visualize protein chain
    vis.visualisation(best_chain)

    return best_chain, highest_score

