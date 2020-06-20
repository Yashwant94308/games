import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 4 * np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos')

plt.title("x,y plane")
plt.xlabel("Angles")
plt.ylabel("sin-cos value")
plt.legend()
plt.show()
# plt.savefig("plot.png")
