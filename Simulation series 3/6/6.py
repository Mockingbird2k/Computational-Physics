import datetime
import numpy as np
import matplotlib.pyplot as plt
import random

time = datetime.datetime.now()
L_array = np.array([10, 100, 200])


def plane_init():  # creates a 2D array(plane) and prepares 'plane' for start(sets its initial values)
    plane = np.zeros(shape=(L + 1, L))
    i = 1
    while i < L + 1:
        j = 0
        while j < L:
            plane[i, j] = off_number
            j += 1
        i += 1
    return plane


probability = .57
probability_array = np.array(
    [0.1, 0.2, 0.3, 0.4, 0.45, 0.50, 0.55, 0.57, 0.58, 0.59, 0.60, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69,
     0.7, 0.8, 0.9])
global counter
counter = 1


def recolor(plane, max_value, min_value):  # subtitutes cells of array(plane),which have max_value with min_value
    color_array[int(max_value)] = color_array[int(min_value)]
    return None


def percolation_check(plane):  # checks if percolation has happened or not
    j = 0
    while j < L:
        if color_checker(plane[L, j]) == 1:
            return 1
        j += 1
    return 0


def color_checker(value):
    if color_array[int(value)] != int(value):
        return color_checker(color_array[int(value)])
    if color_array[int(value)] == int(value):
        if int(value) == 0:
            return 1
        else:
            return 0


def value_assign(plane, x, y):  # assign a value to a newly born cell(in 2D array 'plane')
    if plane[(x - 1), y] == off_number and plane[x, y - 1] == off_number:
        global counter
        plane[x, y] = counter
        counter = counter + 1
        return None
    elif plane[(x - 1), y] != off_number and plane[x, y - 1] == off_number:
        plane[x, y] = color_array[int(plane[x - 1, y])]
    elif plane[(x - 1), y] == off_number and plane[x, y - 1] != off_number:
        plane[x, y] = color_array[int(plane[x, y - 1])]
    elif plane[(x - 1), y] != off_number and plane[x, y - 1] != off_number:
        sorted_temp = np.sort((color_array[int(plane[x - 1, y])], color_array[int(plane[x, y - 1])]))
        plane[x, y] = sorted_temp[0]
        recolor(plane, sorted_temp[1], sorted_temp[0])
    return None


def mother(plane, x, y,
           probability):  # checks if a random number is less than probability,turns it on(gives birth to it!  LOL)
    temp = random.random()
    if temp <= probability:
        value_assign(plane, x, y)
    return None


Q_array = np.zeros(shape=(len(L_array),
                          len(probability_array)))  # in cell (i,j) of this array,value says the probability of percolation of system in length length_array[i] and probability of probaility_array[j]
k = 0
while k < len(L_array):
    L = L_array[k]
    off_number = -L  # value of off cells would be this
    m = 0
    while m < len(probability_array):
        Q = 0  # 'Q' counts the how many times percolation has happened in 100 run of system
        probability = probability_array[m]
        n = 0
        while n < 100:
            color_array = np.arange(L ** 2 + 1)
            counter = 1
            global plane
            plane = plane_init()
            i = 1
            while i < L + 1:
                j = 0
                while j < L:
                    mother(plane, i, j, probability)
                    j = j + 1
                i = i + 1
            n += 1
            Q = Q + percolation_check(plane)
        Q_array[k, m] = Q / 100
        m += 1
    k += 1

print(datetime.datetime.now() - time)
fig = plt.figure()
plt.plot(probability_array, Q_array[0, :])
plt.plot(probability_array, Q_array[1, :])
plt.plot(probability_array, Q_array[2, :])

plt.show()