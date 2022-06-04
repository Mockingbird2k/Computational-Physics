import matplotlib.pyplot as plt
import matplotlib.collections as mc
import time


# Making a plot of a list of segments(We needed 2 procedures to create this fractal. This will help us to do so)


def plot_segments(segments):
    fig, ax = plt.subplots()
    lines = mc.LineCollection(segments)
    ax.add_collection(lines)
    ax.margins()
    ax.set_aspect('equal')
    ax.autoscale()
    return ax


# The 2 procedures which will create our Fractal


def fractal(seg):
    global i
    i += 1
    a = seg[0]
    c = seg[1]
    k = 3 / 6
    if i % 2 == 1 : b = ((a[0] + c[0]) / 2 - k * (c[1] - a[1]), (a[1] + c[1]) / 2 + k * (c[0] - a[0]))
    if i % 2 == 0 : b = ((a[0] + c[0]) / 2 + k * (c[1] - a[1]), (a[1] + c[1]) / 2 - k * (c[0] - a[0]))
    return [(a, b), (b, c)]


# This function is obvious


def recurse(segments):
    return [x for s in segments for x in fractal(s)]


# Program starting

print('Hi Welcome to the Heighway Dragon Fractal Program. '
      'Please set how many iterations this program can go (choose a number which is less than 20 otherwise you have '
      'to sit here for a long time)')
numb = int(input())
print("In the last plot you can zoom in to see more details. There isn't any limit for us")
print("Programmed by Mockingbird")
time.sleep(5)

# Creating the first iteration

a = (0.1, 0.1)
c = (0.5, 0.1)
ac = (a, c)
plot_segments([ac])
plt.pause(2)
plt.close()
segements = [(a, c)]
i = 0

# Creating n iterations
f = 1
while f < numb:
    segements = recurse(segements)
    i = 0
    plot_segments(segements)
    if f == numb - 1 : plt.show()
    else : plt.pause(2)
    plt.close()
    f += 1



