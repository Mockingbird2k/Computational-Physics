import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import cmath
import time


def julia_set(c):
    # Initialise an empty array (corresponding to pixels)
    julia = np.zeros((x_res, y_res))

    # Loop over each pixel
    for ix in range(x_res):
        for iy in range(y_res):
            # Map pixel position to a point in the complex plane
            z = complex(ix / x_res * width + xmin, iy / y_res * height + ymin)
            # Iterate
            iteration = 0
            while abs(z) <= z_abs_max and iteration < max_iter:
                z = z ** 2 + c
                iteration += 1

            iteration_ratio = iteration / max_iter
            # Set the pixel value to be equal to the iteration_ratio
            julia[iy, -ix] = iteration_ratio

    # Plot the array using matplotlib's imshow
    fig, ax = plt.subplots()
    ax.imshow(julia, interpolation='bilinear')
    plt.axis()
    plt.show()


# Program starting
print('Hi Welcome to the Julia Set Program. '
      'Please set you complex number (The Origin function is : F(z) = z^2 + c)(Note that the max iterations is 1000')
c = complex(input())
print("Programmed by Mockingbird")
time.sleep(2)

# Parameters
x_res, y_res = 300, 300
xmin, xmax = -1.5, 1.5
width = xmax - xmin
ymin, ymax = -1.5, 1.5
height = ymax - ymin

max_iter = 1000

betta = (1 + cmath.sqrt(1 + 4 * (c.real * c.real + c.imag * c.imag))) / 2
betta = betta.real
z_abs_max = betta
julia_set(c)
