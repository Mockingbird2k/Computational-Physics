import numpy as np
import matplotlib.pyplot as plt
import random

L = 200  # 'L' is length of model
earth = np.zeros(L)
point_scale = 100  # 'point_scale' is a measure of how many points you want to drop every time.calculation is as
# follows:2^(final_step)*point_scale-point_scale

global final_step  # we get data logarithmic. the number of times we get data is final_step
final_step = 6

global current_step  # 'current_step is created so that we can understand if we have gathered data 'final_step' times
# or not
current_step = 0

global point_counter  # 'point_counter' counts times which 'graph' is called.so that it can adjust the appropriate
# color for scattering
point_counter = 0

global time_array  # we keep in this  array,times of measurements
time_array = np.zeros(final_step)
'''in below we set times of measurement'''
i = 1
while i <= final_step:
    time_array[i - 1] = (2 ** i) * point_scale - point_scale
    i = i + 1

global ensemble_number  # number of times that the program runs to make an ensemble of datas
ensemble_number = 5

global ensemble_array  # ensemble_array is actually a 2D array. in every row of it,logarithm of 'NAHAMVARI' in
# different times is kept(every row is for a different run of program)
ensemble_array = np.zeros(shape=(ensemble_number, final_step))

global current_ensemble  # 'current_ensemble says that at the moment,system is runing,which one of the ensembles'
current_ensemble = 0

global height_ensemble_array  # height_ensemble_array is actually a 2D array. in every row of it,height of 'earth' in
# different times is kept(every row is for a different run of program)
height_ensemble_array = np.zeros(shape=(ensemble_number, final_step))


def coloring():  # determine color of variable 'color'
    if (point_counter // 2000) % 2 == 0:
        return 'r'
    else:
        return 'b'


def graph(x, y,
          color):  # x actually is x(th) element of 'earth' and y is corresponding height of it(value of earth[x])
    global point_counter  # color of point is 'color'
    plt.scatter(x, y, s=15, c=color)
    point_counter = point_counter + 1


def save_w(w):  # saves logarithm of 'NAHAMVARI'(w) in time 'current_step' of ensemble 'current_ensemble'
    ensemble_array[current_ensemble][current_step] = np.log2(w)


def save_height(height):  # saves average height of 'earth' in time 'current_step' of ensemble 'current_ensemble'
    height_ensemble_array[current_ensemble][current_step] = height


def w_cal(earth):  # calculates variance of data after a specific step
    w = (np.var(earth)) ** .5
    save_w(w)


def height_cal(earth):  # calculates average height of 'earth' in time 'current_step'
    height = np.average(earth)
    save_height(height)


def error_cal(
        ensemble_array):  # calculates error of 'NAHAMVARI' in a specified time(current_step) among different runs of program(ensembles)
    error_array = np.zeros(final_step)
    j = 0
    while j < final_step:
        error_array[j] = np.var(ensemble_array[:, j]) / (final_step - 1)
        j = j + 1
    return error_array


def average_cal(
        ensemble_array):  # calculates average of 'NAHAMVARI' in a specified time(current_step) among different runs of program(ensembles)
    average_array = np.zeros(final_step)
    j = 0
    while j < final_step:
        average_array[j] = np.average(ensemble_array[:, j])
        j = j + 1
    return average_array


def best_slope(x_arr, y_arr):  # finds the best slope,passes through arrays 'x_arr' and 'y_arr'
    xbar = np.average(x_arr)
    ybar = np.average(y_arr)
    xybar = np.average(x_arr * y_arr)
    x2bar = np.average(x_arr ** 2)
    slope = (xbar * ybar - xybar) / (xbar ** 2 - x2bar)
    return slope


def evo(earth, final_point):  # final_point is number of points which 'evo' drops in every cycle
    global current_step
    if current_step < final_step:
        current_point = 0
        while current_point < final_point:
            rand = random.randint(0, L - 1)
            if earth[rand] >= earth[(rand - 1) % L] and earth[rand] >= earth[(rand + 1) % L]:
                earth[rand] = earth[rand] + 1
            else:
                max_index = (rand - 1 + np.argmax((earth[(rand - 1) % L], earth[rand], earth[(rand + 1) % L]))) % L
                earth[rand] = earth[max_index]
            '''in this part point would be SCATTERED'''
            color = coloring()
            graph(rand, earth[rand], color)
            current_point = current_point + 1
        w_cal(earth)
        height_cal(earth)
        current_step = current_step + 1
        return evo(earth, final_point * 2)


while current_ensemble < ensemble_number:  # runs the system for several times('ensemble_number' times)
    evo(earth, point_scale)
    current_step = 0
    current_ensemble = current_ensemble + 1
    earth = np.zeros(L)

# plt.errorbar(np.log2(time_array) ,average_cal(ensemble_array),error_cal(ensemble_array),fmt='o')
print(best_slope(np.log2(time_array), average_cal(ensemble_array)))
print(height_ensemble_array[0])

plt.show()
