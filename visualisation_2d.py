
import numpy as np
import matplotlib.pyplot as plt
from code.functions import get_point_colors as gp
import matplotlib.lines as mlines

def visualisation():
    """Visualise aminoacid chain on a grid """
    
    # get input
    input = [(0,0,0),(0,1,0),(1,1,0)]

    random_point = input[0]
    next_point = input[2]

    # find middle point 
    middle = input[1]
            
    # check if not straight line (if only one coordinate):
    dif_end_x = next_point[0] - random_point[0]
    dif_end_y = next_point[1] - random_point[1]

    if dif_end_x != 0 and dif_end_y != 0:
        # check which dimension to ignore:


        # calculate coordinates new point (invert change):
        dif_middle_x = middle[0] - random_point[0]
        if dif_middle_x == dif_end_x:
            input[1] = (random_point[0], random_point[1] + dif_end_y)
        else:
            input[1] = (random_point[0] + dif_end_x, random_point[1])

        # check if point in fold, do the flip

    x, y = zip(*input)




    plt.xlim([-1, 3])
    plt.ylim([-1, 3])

    # plot 2d graph
    plt.plot(x, y, c='red') 
    plt.grid(True)

    plt.savefig("scatter.pdf")

visualisation()


