import numpy as np
import matplotlib.pyplot as plt
import datetime
import random

time = datetime.datetime.now()


u = 1 / 4  # probability of jumping up
d = 1 / 4  # probability of jumping down
l = 1 / 4  # probability of jumping left
r = 1 / 4  # probability of jumping right

max = 1
leng = 5
sample_number = 1000

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

def evo():
    global kappa
    kappa = np.zeros(max+3)
    c = 0
    n = 0
    j = 0
    current_x = np.zeros(4**leng,dtype=int)
    current_y = np.zeros(4**leng,dtype=int)

    while j > -1:
            c = 0
            rnd = np.random.random_sample(sample_number)
            #print(rnd)
            if 0 < rnd[j] < u:
                current_y[j] += 1
                n += 1
            elif u < rnd[j] < (u + d):
                current_y[j] -= 1
                n += 1
            elif (u + d) < rnd[j] < (u + d + l):
                current_x[j] -= 1
                n += 1
            elif (u + d + l) < rnd[j] < 1:
                current_x[j] += 1
                n += 1

            while c < j:

                if (current_x[j] == current_x[c]) and (current_y[j] == current_y[c]):
                    #print(n)
                    current_x[j] = current_x[c - 1]
                    current_y[j] = current_y[c - 1]
                    c = j
                    j -= 1
                    kappa[n] = kappa[n]+1
                    n -= 1
                    print(kappa[max])

                c += 1
            #print(current_x[j], current_y[j])
            if j == max+1:
                return kappa
            j += 1





k = evo()
print (k)



print(datetime.datetime.now() - time)
