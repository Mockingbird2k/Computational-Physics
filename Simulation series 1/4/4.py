import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as mc


def plot_segments(segments):
    fig, ax = plt.subplots()
    lines = mc.LineCollection(segments)
    ax.add_collection(lines)
    ax.margins()
    ax.set_aspect('equal')
    ax.autoscale()
    return ax


def pascal(a):
    l = len(a)
    b = np.array(range(0,l+1))
    l = len(b)
    b[0] = 1
    b[l-1] = 1
    i = 1
    while i < l-1 :
        b[i] = a[i-1] + a[i]
        i += 1
    return b

def recurse(segments):
    return [x for s in segments for x in pascal(s)]

#yey
f = 10
k = 1
x = (0.5, 1)
y = (0.48, 1)
xx = (0.48, 0.98)
yy = (0.46, 0.98)
xxx = (0.52, 0.98)
yyy = (0.50, 0.98)
xyy = (xx, yy)
segements = [(x, y), (xx, yy), (xxx, yyy)]
plot_segments(segements)
a = np.array([1, 1])


for k in range(f) :
    b = pascal(a)
    a = b
    print(b)
for k in range(f) :
    x = (1-f, 1-f)
    y = (1-f)
   # plot_segments([xy])
plt.show()
