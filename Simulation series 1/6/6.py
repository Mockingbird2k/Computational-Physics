import matplotlib.pyplot as plt
from random import randint
import time

print('Hi Welcome to the Barnsley fern Program. '
      "Please set The resolution (choose a number which is more than 20000 otherwise you can't 'see the pattern very "
      "well)")
numb = int(input())
print("In the last plot you can zoom in to see more details. There isn't any limit for us")
print("Programmed by Mockingbird")
time.sleep(5)


# initializing the list
x = []
y = []

# setting first element to 0
x.append(0)
y.append(0)

current = 0

for i in range(1, numb):

    # generates a random integer between 1 and 100
    z = randint(1, 100)

    # the x and y coordinates of the equations are appended in the lists respectively.

    # for the probability 0.01
    if z == 1:
        x.append(0)
        y.append(0.16 * (y[current]))

    # for the probability 0.85
    if 2 <= z <= 86:
        x.append(0.85 * (x[current]) + 0.04 * (y[current]))
        y.append(-0.04 * (x[current]) + 0.85 * (y[current]) + 1.6)

    # for the probability 0.07
    if 87 <= z <= 93:
        x.append(0.2 * (x[current]) - 0.26 * (y[current]))
        y.append(0.23 * (x[current]) + 0.22 * (y[current]) + 1.6)

    # for the probability 0.07
    if 94 <= z <= 100:
        x.append(-0.15 * (x[current]) + 0.28 * (y[current]))
        y.append(0.26 * (x[current]) + 0.24 * (y[current]) + 0.44)

    current = current + 1

plt.scatter(x, y, s=0.2, edgecolor='green')

plt.show()
