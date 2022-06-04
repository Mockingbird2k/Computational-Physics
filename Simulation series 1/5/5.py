import numpy as np
import matplotlib.pyplot as plt
import random
import time


# Produce a random integer between 1 and 3.(both included)


def rand_num():
    rand = random.randint(1, 3)
    return rand


# Scales a vector(vec) with scale multiplication 'r'


def scaler(vec, r):
    vec[0] = vec[0] * r
    vec[1] = vec[1] * r
    return vec


# We had this beauty in Question 5


def Serpinski(vlft, vmd, vrt, step, numb):
    if step < numb:
        vec1 = scaler(vmd - vlft, 1 / 2)
        vec2 = scaler(vrt - vlft, 1 / 2)
        rand = rand_num()
        if rand == 1:
            Serpinski(vlft, vlft + vec1, vlft + vec2, step + 1, numb)
        elif rand == 2:
            Serpinski(vlft + vec1, vmd, vlft + vec1 + vec2, step + 1, numb)
        elif rand == 3:
            Serpinski(vlft + vec2, vlft + vec1 + vec2, vrt, step + 1, numb)
    else:
        plt.fill([vlft[0], vmd[0], vrt[0]], [vlft[1], vmd[1], vrt[1]], color='blue')


# Program starting
print('Hi Welcome to the Serpinski Fractal with random number approach Program. '
      'Please set how many iterations this program can go (choose a number which is less than 7 otherwise you have '
      'to sit here for a long time)')
numb = int(input())
print("In the last plot you can zoom in to see more details. There isn't any limit for us")
print("Programmed by Mockingbird")
time.sleep(5)

fig = plt.figure()
plt.ylim(0, 200)
plt.xlim(0, 200)
vertex_left = np.array([0, 0])
vertex_middle = np.array([100, 173.205])
vertex_right = np.array([200, 0])
i = 0

#in each run time,a triangle is drawn which maybe repetitive
rnumb= 4 ** (numb + 1)

while i < rnumb:
    Serpinski(vertex_left, vertex_middle, vertex_right, 0, numb)
    i += 1
plt.show()
