
import numpy as np
import matplotlib.pyplot as plt
from code.functions import get_point_colors as gp

import matplotlib.lines as mlines

def visualisation():
    """Visualise aminoacid chain on a grid """
    
    # get input
    input = [(0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,1),(1,1)]

    x, y = zip(*input)

    plt.xlim([-1, 3])
    plt.ylim([-1, 3])

    # plot 2d graph
    plt.plot(x, y, c='red') 
    plt.grid(True)

    plt.savefig("scatter.pdf")

visualisation()


