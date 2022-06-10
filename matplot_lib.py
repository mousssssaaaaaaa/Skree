# use Algorithm.py with protein folder object to create test visual. 

import numpy as np
import matplotlib.pyplot as plt
# from Algorithm import folder 

input = [(0,0), (0,1)] # folder() 

x, y = zip(*input)
# colors = np.random.rand(N)
# area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y) # s=area, , c=colors
plt.plot(x, y)
plt.show()