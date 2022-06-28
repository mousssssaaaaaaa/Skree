import pickle as pkl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from mpl_toolkits import mplot3d
from code.functions import get_point_colors as gp

def visualisation(chain):
    """
    Visualise aminoacid chain on a grid
    """

    # Get input
    input = chain.folds

    # Assign colours to each scatter point
    x, y, z = zip(*input)
    point_color = gp.get_point_colors(chain.aminocode)
    colors = np.array(point_color)

    # Plot 3d graph with grid
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    ax.grid(True)

    # Plot amino acids
    ax.scatter(x, y, z, c = colors)

    # Plot covalent bonds
    ax.plot(x, y, z, c = 'gray')

    # Add descriptions in legend
    blue_sq = mlines.Line2D([], [], color = 'blue', marker = 'o',
                            linestyle = 'None', markersize = 10,
                            label = 'Polair')
    red_sq = mlines.Line2D([], [], color = 'red', marker = 'o',
                            linestyle = 'None', markersize = 10,
                            label = 'Hydrofoob')
    yellow_sq = mlines.Line2D([], [], color = 'yellow', marker = 'o',
                            linestyle = 'None', markersize = 10,
                            label = 'Cysteïne')
    score = "Score: " + str(int(chain.get_score()))
    ax.legend(handles = [blue_sq, red_sq, yellow_sq], title = score)

    # store static figure
    plt.savefig("results/scatter.png")

def twisting_plot(chain): 
    """
    Visualise aminoacid chain on a interactive grid
    """

    # Get input
    input = chain.folds

    # Assign colours to each scatter point
    x, y, z = zip(*input)
    point_color = gp.get_point_colors(chain.aminocode)
    colors = np.array(point_color)

    # Plot 3d graph with grid
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    ax.grid(True)

    # Plot amino acids
    ax.scatter(x, y, z, c = colors)

    # Plot covalent bonds
    ax.plot(x, y, z, c = 'gray')

    # Add descriptions in legend
    blue_sq = mlines.Line2D([], [], color = 'blue', marker = 'o',
                            linestyle = 'None', markersize = 10,
                            label = 'Polair')
    red_sq = mlines.Line2D([], [], color = 'red', marker = 'o',
                            linestyle = 'None', markersize = 10,
                            label = 'Hydrofoob')
    yellow_sq = mlines.Line2D([], [], color = 'yellow', marker = 'o',
                            linestyle = 'None', markersize = 10,
                            label = 'Cysteïne')
    score = "Score: " + str(int(chain.get_score()))
    ax.legend(handles = [blue_sq, red_sq, yellow_sq], title = score)

    # Show interactive figure
    plt.show()

