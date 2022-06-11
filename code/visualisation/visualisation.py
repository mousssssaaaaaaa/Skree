
import numpy as np
import matplotlib.pyplot as plt
from code.functions import get_point_colors as gp

def visualisation(chain):

    input = chain.folds
    x, y = zip(*input)
    # [(0,0), (0,1)]

    point_color = gp.get_point_colors(chain.aminocode)
    # colors = np.random.rand(N)
    # area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
    axis = range(-10, 11)
    plt.plot(x, y,c='gray')
    plt.scatter(x, y, c=point_color) # s=area, , c=colors
    plt.xticks(axis)
    plt.yticks(axis)
    plt.grid(True)
    plt.savefig("scatter.pdf")
