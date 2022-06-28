import csv
import math
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

fig, ax = plt.subplots()
plt.title("3D50")
plt.xlabel("scores")
plt.ylabel("probability density")
kwargs = dict(histtype = 'step', density = True, alpha = 1.0, bins = 10)
l0 = ax.hist(scores_random, label = 'random', **kwargs)
l1 = ax.hist(scores_depth, label = 'depth', **kwargs)
l2 = ax.hist(scores_gravity, label = 'gravity', **kwargs)
l3 = ax.hist(scores_distance, label = 'distance', **kwargs)
l4 = ax.hist(scores_hill_climber, label = 'hill climber', **kwargs)

ax.legend(loc='upper right')
plt.show()
