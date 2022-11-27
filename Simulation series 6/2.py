import numpy as np
import matplotlib.pyplot as plt

sigma = 2
N = 200, 2000, 20000


for k in range(0, len(N)):
    x_array = np.zeros(N[k], dtype=float)
    y_array = np.zeros(N[k], dtype=float)
    for i in range(0, N[k]):
        theta = 2 * np.pi * np.random.random()
        rho = sigma * (-2 * np.log(np.random.random()))
        x = rho * np.cos(theta)
        y = rho * np.sin(theta)
        x_array[i] = x
        y_array[i] = y
    plt.scatter(x_array, y_array, s=1)
    plt.show()
