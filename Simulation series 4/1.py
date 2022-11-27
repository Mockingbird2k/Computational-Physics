import datetime
import numpy as np
import matplotlib.pyplot as plt
import random

time = datetime.datetime.now()
L_array = np.array([10, 20, 40, 80, 160])


def plane_init():  # creates a 2D array(plane) and prepares 'plane' for start(sets its initial values)
    plane = np.zeros(shape=(L + 1, L))
    i = 1
    #print(L)
    while i < L + 1:
        j = 0
        while j < L:
            plane[i, j] = off_number
            j += 1
        i += 1
    return plane


probability = .57
probability_array = np.array(
    [.0, .05, .1, .15, .20, .25, .30, .35, .4, .45, .50, .52, .54, .56, .58, .583, .587, .59, .593, .597, .60, .603,
     .607, .61, .63, .65, .70, .75, .8, .85, .9, .95, 1])
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


def real_color(
        value):  # this function is very similar to function 'color_checker' but it returns the real color of a color
    if color_array[int(value)] != int(value):
        return real_color(color_array[int(value)])
    if color_array[int(value)] == int(value):
        return int(value)


def big_cluster_finder(real_color_array, area_array,
                       temp):  # in the case,system has percolated it finds the "real color" of the bigest cluster(except the percolated cluster)
    max_S = 0  # area of bigest cluster                         #if system has percolated,temp is 1.else temp is 0
    index = L ** 2 + 1  # color of bigest cluster(-1 means there is no cluster but infinity cluster)
    i = 0
    while i <= counter:
        if real_color_array[i] != 0:
            j = i
            temp_S = 0
            while j <= counter:
                if real_color_array[j] == real_color_array[i]:
                    temp_S += area_array[j]
                j += 1
            if temp_S > max_S:
                max_S = temp_S
                index = real_color_array[i]
        i += 1
    return (index, max_S)  # 'index'==L**2+1 means that the whole grid a infinity cluster


def x_cm_finder(plane, index, max_S):  # finds the x coordinate of center of mass of cluster
    i = 1
    x_cm = 0
    while i < L + 1:
        j = 0
        while j < L:
            if real_color_array[int(plane[i, j])] == index:
                x_cm = x_cm + j
            j += 1
        i += 1
    x_cm = x_cm / max_S
    return x_cm


def y_cm_finder(plane, index, max_S):  # finds the y coordinate of center of mass of cluster
    i = 1
    y_cm = 0
    while i < L + 1:
        j = 0
        while j < L:
            if real_color_array[int(plane[i, j])] == index:
                y_cm = y_cm + i
            j += 1
        i += 1
    y_cm = y_cm / max_S
    return y_cm


def x_var_finder(plane, x_cm, index, max_S):  # finds the x variance of system around the x_cm
    i = 1
    x_var = 0
    while i < L + 1:
        j = 0
        while j < L:
            if real_color_array[int(plane[i, j])] == index:
                x_var = x_var + (j - x_cm) ** 2
            j += 1
        i += 1
    x_var = x_var / max_S
    return x_var


def y_var_finder(plane, y_cm, index, max_S):
    i = 1
    y_var = 0
    while i < L + 1:
        j = 0
        while j < L:
            if real_color_array[int(plane[i, j])] == index:
                y_var = y_var + (i - y_cm) ** 2
            j += 1
        i += 1
    y_var = y_var / max_S
    return y_var


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
           probability):  # checks if a random number is less than probability,turns it on
    temp = random.random()
    if temp <= probability:
        value_assign(plane, x, y)
    return None


ksi_array = np.zeros(shape=(len(L_array), len(probability_array)))
k = 0
while k < len(L_array):
    L = L_array[k]
    off_number = -L  # value of off cells would be this

    m = 0
    while m < len(probability_array):
        Q = 0  # 'Q' counts the how many times percolation has happened in 100 run of system
        probability = probability_array[m]
        Rg = 0
        n = 0
        while n < 10:
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
            Q = Q + temp
            real_color_array = np.arange(
                L ** 2 + 1)  # all the connected clusters have the same number and stored in this array
            s = 0
            while s < counter:
                if s == real_color(s):
                    h = 0
                    while h <= counter:
                        if real_color(h) == s:
                            real_color_array[h] = s
                        h += 1
                s += 1
            (index, max_S) = big_cluster_finder(real_color_array, area_array,
                                                temp)  # here the color of biggest cluster('index') and its area
            # max_S is evaluated
            if max_S != 0:
                x_var = x_var_finder(plane, x_cm_finder(plane, index, max_S), index, max_S)
                y_var = y_var_finder(plane, y_cm_finder(plane, index, max_S), index, max_S)
                Rg += (x_var + x_var)  # at the end we will divide Rg by 100
        Rg = Rg / 100
        ksi_array[k, m] = Rg ** .5
        m += 1
    k += 1

print(datetime.datetime.now() - time)
# plt.pcolor(plane)


fig = plt.figure()
plt.scatter(probability_array, ksi_array[0, :])
plt.scatter(probability_array, ksi_array[1, :])
plt.scatter(probability_array, ksi_array[2, :])
plt.scatter(probability_array, ksi_array[3, :])
plt.scatter(probability_array, ksi_array[4, :])

plt.show()
