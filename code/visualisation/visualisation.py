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

    # get input
    input = chain.folds

    # assign colours to each scatter point
    x, y, z = zip(*input)
    point_color = gp.get_point_colors(chain.aminocode)
    colors = np.array(point_color)

    # plot 3d graph with grid
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    ax.grid(True)

    # plot amino acids
    ax.scatter(x, y, z, c = colors)

    # plot covalent bonds
    ax.plot(x, y, z, c = 'gray')

    # add descriptions in legend
    blue_sq = mlines.Line2D([], [], color = 'blue', marker = 'o',
                            linestyle = 'None', markersize = 10,
                            label = 'Hydrofoob')
    red_sq = mlines.Line2D([], [], color = 'red', marker = 'o',
                            linestyle = 'None', markersize = 10,
                            label = 'Polair')
    score = "Score: " + str(int(chain.get_score()))
    ax.legend(handles = [blue_sq, red_sq], title = score)

    # show interactive figure
    #plt.show()

    # store static figure
    plt.savefig("results/scatter.png")

    # store interactive figure
    pkl.dump(fig, open('results/latestFigObj.fig.pickle', 'wb'))
