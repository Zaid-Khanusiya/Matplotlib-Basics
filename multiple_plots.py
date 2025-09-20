import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x1 = np.array([0, 1, 2, 3])
y1= np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)


#plot 2:
x2 = np.array([0, 1, 2, 3])
y2= np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
plt.plot(x1,y1)
plt.plot(x2,y2)

plt.show()