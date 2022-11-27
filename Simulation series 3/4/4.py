import numpy as np
import matplotlib.pyplot as plt
import random

L = 100
plane = np.zeros(shape=(L, L))
probability = .5


def value_assign(plane, x, y):  # assign a value to a newly born cell(in 2D array 'plane')
    plane[x, y] = 1
    return None


def mother(plane, x, y, probability):  # checks if a random number is less than probability,turns it on
    temp = random.random()
    if temp <= probability:
        value_assign(plane, x, y)
    return None


i = 0
while i < L:
    j = 0
    while j < L:
        mother(plane, i, j, probability)
        j = j + 1
    i = i + 1

fig = plt.figure()
plt.pcolor(plane, cmap='binary')

plt.show()
