import matplotlib.pyplot as plt
import numpy as np

x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y, width=0.3) # add custom width if you want

# for horizontal use barh()
# plt.barh(x, y, color = "red") # add custom color if we want

# for setting custom bar width in horizontal mode the keyword "height" is used

plt.show()