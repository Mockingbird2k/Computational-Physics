import numpy as np
import matplotlib.pyplot as plt


def analytical_sol(x):
    return -1 / 300 * np.exp(-x)


def num_solve(xi, step, time):
    # find count
    count = int(time / step)

    # initializations
    x = np.zeros(count)
    x[0] = xi

    # first step is euler:
    x[1] = x[0] + step * -(x[0])

    # evolve
    for i in range(1, count - 1):
        x[i + 1] = x[i - 1] + 2 * step * -(x[i])

    return x, count

# Initial variables
xi = - 1 / 300
end = 15
step = 0.001

# integrate numerically
record, count = num_solve(xi, step, end)
print(record)

# time axis
time = np.linspace(0, end, count)

# plot both solutions in a graph
plt.plot(time, record, 'yellow', label='numerical')
plt.plot(time, analytical_sol(time), 'b', ls=':', label='analytical')
plt.xlabel('tau')
plt.ylabel('solutions')
plt.legend()
plt.show()
