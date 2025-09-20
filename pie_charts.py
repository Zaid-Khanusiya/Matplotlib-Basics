import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow=True) # doing this will explode the defined part of pie
# we can also set shadow to True to display shadow below pie

# we can also set custom colors if we want
# mycolors = ["black", "hotpink", "b", "#4CAF50"]
# plt.pie(y, labels = mylabels, colors = mycolors)

# this will display list & color of every element
plt.legend(title = "Four Fruits:") # also add title if we want

# plt.pie(y, labels = mylabels)
plt.show()