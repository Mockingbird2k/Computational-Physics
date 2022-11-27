import datetime
import numpy as np
import matplotlib.pyplot as plt
import random

time = datetime.datetime.now()
L = 100
plane = np.zeros(shape=(L + 1, L))
off_number = -L  # value of off cells would be this
i = 1
while i < L + 1:
    j = 0
    while j < L:
        plane[i, j] = off_number
        j += 1
    i += 1

probability = .6
global counter
counter = 1


def recolor(plane, max_value, min_value):  # subtitutes cells of array(plane),which have max_value with min_value
    i = 1
    while i < L + 1:
        j = 0
        while j < L:
            if plane[i, j] == max_value:
                plane[i, j] = min_value
            j += 1
        i += 1

    return None


def percolation_check(plane):  # checks if percolation has happened or not
    j = 0
    while j < L:
        if plane[L, j] == 0:
            print('percolated!')
            return None
        j += 1
    print('did NOT percolate!')
    return None


def value_assign(plane, x, y):  # assign a value to a newly born cell(in 2D array 'plane')
    if plane[(x - 1), y] == off_number and plane[x, y - 1] == off_number:
        global counter
        plane[x, y] = counter
        counter = counter + 1
        return None
    elif plane[(x - 1), y] != off_number and plane[x, y - 1] == off_number:
        plane[x, y] = plane[x - 1, y]
    elif plane[(x - 1), y] == off_number and plane[x, y - 1] != off_number:
        plane[x, y] = plane[x, y - 1]
    elif plane[(x - 1), y] != off_number and plane[x, y - 1] != off_number:
        sorted_temp = np.sort((plane[x - 1, y], plane[x, y - 1]))
        plane[x, y] = sorted_temp[0]
        recolor(plane, sorted_temp[1], sorted_temp[0])
    return None


def mother(plane, x, y,
           probability):  # checks if a random number is less than probability,turns it on(gives birth to it!  LOL)
    temp = random.random()
    if temp <= probability:
        value_assign(plane, x, y)
    return None


i = 1
while i < L + 1:
    j = 0
    while j < L:
        mother(plane, i, j, probability)
        j = j + 1
    i = i + 1

percolation_check(plane)
print(datetime.datetime.now() - time)
fig = plt.figure()
plt.pcolor(plane)

plt.show()
