import matplotlib.pyplot as plt
import matplotlib.collections as mc
import math
import time


# Making a plot of a list of segments(We needed 4 procedures to create this fractal. This will help us to do so)


def plot_segments(segments):
    fig, ax = plt.subplots()
    lines = mc.LineCollection(segments)
    ax.add_collection(lines)
    ax.margins(-0.2)
    ax.set_aspect('equal')
    ax.autoscale(False)
    return ax


# The 4 procedures which will create our Fractal


def fractal(seg):
    a = seg[0]
    e = seg[1]
    b = ((2 * a[0] + e[0]) / 3, (2 * a[1] + e[1]) / 3)
    d = ((a[0] + 2 * e[0]) / 3, (a[1] + 2 * e[1]) / 3)
    k = math.sqrt(3) / 6
    c = ((a[0] + e[0]) / 2 - k * (e[1] - a[1]), (a[1] + e[1]) / 2 + k * (e[0] - a[0]))
    return [(a, b), (b, c), (c, d), (d, e)]


# This function is obvious


def recurse(segments):
    return [x for s in segments for x in fractal(s)]


# Program starting
print('Hi Welcome to the Koch Fractal Program. '
      'Please set how many iterations this program can go (choose a number which is less than 10 otherwise you have '
      'to sit here for a long time)')
numb = int(input())
print("In the last plot you can zoom in to see more details. There isn't any limit for us")
print("Programmed by Mockingbird")
time.sleep(5)
# Creating the first iteration
a = (0.0, 0.5)
e = (1.0, 0.5)
ae = (a, e)
plot_segments([ae])
plt.pause(2)
plt.close()
segements = [(a, e)]

# Creating n iterations
i = 1
while i < numb:
    segements = recurse(segements)
    plot_segments(segements)
    plt.pause(2)
    plt.close()
    i += 1

plot_segments(segements)
plt.show()

