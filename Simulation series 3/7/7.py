#
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
     0.7, 0.8, 0.9, 1])
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


def color_checker(
        value):  # checks if a color should be considered as color==0 or not(is connected to infinity cluster or not)
    if color_array[int(value)] != int(value):
        return color_checker(color_array[int(value)])
    if color_array[int(value)] == int(value):
        if int(value) == 0:
            return 1
        else:
            return 0


def area_infinity(area_array,
                  counter):  # checks which clusters are connected with infinity cluster and then sums their area together as area of infinity cluster
    # note:counter is the number of clusters with different color
    area_infinity = area_array[0]  # 'area_infinity' will be area of infinity_cluster
    i = 1
    while i <= counter:
        if color_checker(i) == 1:
            area_infinity += area_array[i]
        i += 1
    return area_infinity


def value_assign(plane, x, y):  # assign a value to a newly born cell(in 2D array 'plane')
    if plane[(x - 1), y] == off_number and plane[x, y - 1] == off_number:
        global counter
        plane[x, y] = counter
        area_array[int(plane[x, y])] += 1  # increases the area of cluster with value==plane[x,y]
        counter = counter + 1
        return None
    elif plane[(x - 1), y] != off_number and plane[x, y - 1] == off_number:
        plane[x, y] = color_array[int(plane[x - 1, y])]
        area_array[int(plane[x, y])] += 1  # increases the area of cluster with value==plane[x,y]
    elif plane[(x - 1), y] == off_number and plane[x, y - 1] != off_number:
        plane[x, y] = color_array[int(plane[x, y - 1])]
        area_array[int(plane[x, y])] += 1  # increases the area of cluster with value==plane[x,y]
    elif plane[(x - 1), y] != off_number and plane[x, y - 1] != off_number:
        sorted_temp = np.sort((color_array[int(plane[x - 1, y])], color_array[int(plane[x, y - 1])]))
        plane[x, y] = sorted_temp[0]
        area_array[int(plane[x, y])] += 1  # increases the area of cluster with value==plane[x,y]
        recolor(plane, sorted_temp[1], sorted_temp[0])
    return None


def mother(plane, x, y,
           probability):  # checks if a random number is less than probability,turns it on(gives birth to it!  LOL)
    temp = random.random()
    if temp <= probability:
        value_assign(plane, x, y)
    return None


connection_probability_array = np.zeros(shape=(len(L_array),
                                               len(probability_array)))  # in cell (i,j) of this array,value says the
# probability that a cell can connect to an infinity cluster in length 'length_array[i]' and probability of
# 'probaility_array[j]'(of course if there is NO infinity cluster,the corresponding probability of connection would
# be ZERO)
k = 0
while k < len(L_array):
    L = L_array[k]
    off_number = -L  # value of off cells would be this
    m = 0
    while m < len(probability_array):
        Q = 0  # 'Q' counts the how many times percolation has happened in 100 run of system
        connection_probability = 0  # 'connection_probability' calculates the probability of a cell to connect to
        # infinity cluster(note:the value WOULD be averaged)
        probability = probability_array[m]
        n = 0
        while n < 100:
            area_array = np.zeros(
                L ** 2 + 1)  # this array keeps the "area" of a cluster in it.and is evaluated in 'value assign
            # function'
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
            temp = percolation_check(plane)  # if temp is 1,percolation has occured.if be 0,has NOT percolated
            if temp == 1:
                connection_probability += area_infinity(area_array, counter)
            Q = Q + temp
        connection_probability_array[k, m] = (connection_probability / 100) / L ** 2
        m += 1
    k += 1

print(datetime.datetime.now() - time)

fig = plt.figure()
plt.plot(probability_array, connection_probability_array[0, :])
plt.plot(probability_array, connection_probability_array[1, :])
plt.plot(probability_array, connection_probability_array[2, :])

plt.show()