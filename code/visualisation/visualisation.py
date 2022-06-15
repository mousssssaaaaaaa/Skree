
import numpy as np
import matplotlib.pyplot as plt
from code.functions import get_point_colors as gp

def visualisation(chain):
    """Visualise aminoacid chain on a grid """
    input = chain.folds
    print(len(chain.folds))
    x, y = zip(*input)

    point_color = gp.get_point_colors(chain.aminocode)

    axis = range(-10, 11)
    plt.plot(x, y,c='gray')
    plt.scatter(x, y, c=point_color)
    plt.xticks(axis)
    plt.yticks(axis)
    plt.grid(True)
    plt.savefig("scatter.pdf")

    # TODO: Score printen op grid, hydrophobe bindingen
    # Legenda H en P
    # Normaalverdeling voor 100

