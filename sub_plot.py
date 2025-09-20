import matplotlib.pyplot as plt
import numpy as np


x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])

x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])


plt.subplot(1, 2, 1)
plt.plot(x1,y1)

plt.subplot(1, 2, 2)
plt.plot(x2,y2)

plt.show()

"""

plt.subplot(1, 2, 1)
the figure has 1 row, 2 columns, and this plot is the first plot. 

plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.

we can add as much plots as we want by this method

"""