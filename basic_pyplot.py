import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

# this will plot lines
plt.plot(xpoints, ypoints)

# # this will plot graph points and not line
# plt.plot(xpoints, ypoints, 'o')


plt.show()