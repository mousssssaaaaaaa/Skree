import math
import numpy as np
import matplotlib.pyplot as plt
from code.functions import read_scores as rs

# read score lists that were produced from main.py
scores_random = rs.read_scores('results/scores_random.csv')
scores_distance = rs.read_scores('results/scores_distance.csv')
scores_gravity = rs.read_scores('results/scores_gravity.csv')
scores_depth = rs.read_scores('results/scores_depth.csv')
scores_hill_climber = rs.read_scores('results/scores_hill_climber.csv')

# setup plot
fig, ax = plt.subplots()
plt.title("Stability score distribution of applied algorithms")
plt.xlabel("scores")
plt.ylabel("probability density")

# set arguments
kwargs = dict(histtype = 'step', density = True, alpha = 1.0)

# plot histograms of every applied algorithms with legend
l0 = ax.hist(scores_random, label = 'random', **kwargs)
l1 = ax.hist(scores_depth, label = 'depth', **kwargs)
l2 = ax.hist(scores_gravity, label = 'gravity', **kwargs)
l3 = ax.hist(scores_distance, label = 'distance', **kwargs)
l4 = ax.hist(scores_hill_climber, label = 'hill climber', **kwargs)
ax.legend(loc='upper right')

# store and present plot
plt.savefig("results/hist_all.png")
plt.show()
plt.close()
