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

fig, ax = plt.subplots()
l0 = ax.hist(scores_random, density = True, label = 'random', alpha = 1.0)
l3 = ax.hist(scores_depth, density = True, label = 'depth', alpha = 0.6)
l2 = ax.hist(scores_gravity, density = True, label = 'gravity', alpha = 0.6)
l1 = ax.hist(scores_distance, density = True, label = 'distance', alpha = 0.6)
l4 = ax.hist(scores_hill_climber, density = True, label 'hill climber', alpha = 0.5)
l5 = ax.hist(scores_hill_climber_gravity)
ax.legend(loc='upper right')

plt.show()
