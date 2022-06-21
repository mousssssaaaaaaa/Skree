
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from code.functions import get_point_colors as gp

import matplotlib.lines as mlines

def visualisation(chain):
    """Visualise aminoacid chain on a grid """
    
    # get input
    input = chain.folds

    x, y, z = zip(*input)
    point_color = gp.get_point_colors(chain.aminocode)
    colors = np.array(point_color)
    
    # plot 3d graph
    ax = plt.axes(projection='3d')
    plt.plot(x, y, z, c='gray')
    ax.scatter3D(x, y, z, c = colors) 
    plt.grid(True)

    # Add descriptions in legend
    blue_square = mlines.Line2D([], [], color='blue', marker='o', linestyle='None',
                            markersize=10, label='Hydrofoob')
    red_square = mlines.Line2D([], [], color='red', marker='o', linestyle='None',
                            markersize=10, label='Polair')
    Score = chain.get_score()
    Score = "Score: " + str(int(Score))
    plt.legend(handles=[blue_square, red_square], title= Score)

    plt.savefig("results/scatter.png")