import csv
import numpy as np
import matplotlib.pyplot as plt

def read_scores(file):

    results = []
    with open(file, newline='') as f:
        for row in csv.reader(f):
            results.append(int(row[0]))

    return results

scores_random = read_scores('results/scores_random.csv')
scores_distance = read_scores('results/scores_distance.csv')
scores_gravity = read_scores('results/scores_gravity.csv')
scores_depth = read_scores('results/scores_depth.csv')
scores_hill_climber = read_scores('results/scores_hill_climber.csv')
# scores_hill_climber_gravity = read_scores('results/scores_hill_climber_gravity.csv')
scores_simulated_annealing = read_scores('results/scores_simulated_annealing.csv')

fig, ax = plt.subplots()
l0 = ax.hist(scores_random, density = True, label = 'random', alpha = 0.6)
l3 = ax.hist(scores_depth, density = True, label = 'depth', alpha = 0.6)
l2 = ax.hist(scores_gravity, density = True, label = 'gravity', alpha = 0.6)
l1 = ax.hist(scores_distance, density = True, label = 'distance', alpha = 0.6)
l4 = ax.hist(scores_hill_climber, density = True, label = 'hill climber', alpha = 0.6)
# l5 = ax.hist(scores_hill_climber_gravity, density = True, label = 'hill climber gravity', alpha = 0.5)
l6 = ax.hist(scores_simulated_annealing, density = True, label = 'simulated annealing', alpha = 0.6)
ax.legend(loc='upper right')

plt.show()
