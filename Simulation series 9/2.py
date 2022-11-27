import numpy as np
import matplotlib.pyplot as plt


# This Program wrote for a simple harmonic oscillator which K/m=1 so the equation will simplify to: d(dx)/dt^2 = -x



def euler(xi, step, time):
    """ euler method """
    # finding count
    count = int(time / step)

    # initialization
    x = np.zeros(count)
    x_dot = np.zeros(count)
    x[0] = xi

    for i in range(count - 1):
        x[i + 1] = x[i] + x_dot[i] * step
        x_dot[i + 1] = x_dot[i] + -(x[i]) * step

    return x, x_dot, count


def euler_cromer(xi, step, time):
    """ euler-Cromer method """
    # finding count
    count = int(time / step)

    # initialization
    x = np.zeros(count)
    x_dot = np.zeros(count)
    x[0] = xi

    for i in range(count - 1):
        x_dot[i + 1] = x_dot[i] + -(x[i]) * step
        x[i + 1] = x[i] + x_dot[i + 1] * step

    return x, x_dot, count


def verlat(xi, step, time):
    """ verlat method """
    # calc ing count
    count = int(time / step)

    # initialization
    x = np.zeros(count + 2)
    x_dot = np.zeros(count + 1)
    x[0:2] = xi, xi

    for i in range(1, count + 1):
        x[i + 1] = 2 * x[i] - x[i - 1] + -(x[i]) * step ** 2
        x_dot[i] = (x[i + 1] - x[i - 1]) / (2 * step)

    # deleting zero factors
    x = np.delete(x, [0, -1])
    x_dot = np.delete(x_dot, 0)

    return x, x_dot, count


def velocity_verlat(xi, step, time):
    """ velocity verlat method """
    # finding count
    count = int(time / step)

    # initialization
    x = np.zeros(count)
    x_dot = np.zeros(count)
    x[0] = xi
    x_dot[0] = 0

    for i in range(count - 1):
        x[i + 1] = x[i] + x_dot[i] * step + 0.5 * step ** 2 * -(x[i])
        x_dot[i + 1] = x_dot[i] + 0.5 * (-(x[i + 1]) + -(x[i])) * step

    return x, x_dot, count


def beeman(xi, step, time):
    """ beeman method """
    # find count
    count = int(time / step)
    # initialize
    x = np.zeros(count + 1)
    x_dot = np.zeros(count + 1)
    x[0:2] = xi
    x_dot[0] = 0

    for i in range(1, count):
        x[i + 1] = x[i] + x_dot[i] * step + 1.0 / 6 * (4 * -(x[i]) - -(x[i - 1])) * step ** 2

        x_dot[i + 1] = x_dot[i] + 1 / 6.0 * ( 2 * -(x[i + 1]) + 5 * -(x[i]) - -(x[i - 1])) * step

    # deleting zero factors
    x = np.delete(x, 0)
    x_dot = np.delete(x_dot, 0)

    return x, x_dot, count

# Initial variables

xi = 1
step = 0.01
end = 60

# simulating different methods

eu = euler(xi, step, end)
euc = euler_cromer(xi, step, end)
ve = verlat(xi, step, end)
vev = velocity_verlat(xi, step, end)
bee = beeman(xi, step, end)

time = np.linspace(0, 10, eu[2])

# Part A: between two """, the diagrams will save separately. Out of """, the diagrams will be shown together
# In this part we calculate and show the x versus t diagram

"""
plt.plot(time, eu[0], label='Euler')
plt.xlabel('time')
plt.ylabel('x')
plt.title("solution for d^2 x / dt^2 = - x using Euler")
plt.savefig("9.2A Euler.jpg", bbox_inches='tight')
plt.close()

plt.plot(time, euc[0], label='Euler-Cromer')
plt.xlabel('time')
plt.ylabel('x')
plt.title("solution for d^2 x / dt^2 = - x using Euler-Cromer")
plt.savefig("9.2A Euler-Cromer.jpg", bbox_inches='tight')
plt.close()

plt.plot(time, ve[0], label='Verlat')
plt.xlabel('time')
plt.ylabel('x')
plt.title("solution for d^2 x / dt^2 = - x using Verlat")
plt.savefig("9.2A Verlat.jpg", bbox_inches='tight')
plt.close()

plt.plot(time, vev[0], label='Velocity-Verlat')
plt.xlabel('time')
plt.ylabel('x')
plt.title("solution for d^2 x / dt^2 = - x using Velocity-Verlat")
plt.savefig("9.2A Velocity-Verlat.jpg", bbox_inches='tight')
plt.close()

plt.plot(time, bee[0], label='Beeman')
plt.xlabel('time')
plt.ylabel('x')
plt.title("solution for d^2 x / dt^2 = - x using Beeman")
plt.savefig("9.2A Beeman.jpg", bbox_inches='tight')
plt.close()
"""
plt.plot(time, eu[0], label='Euler')
plt.plot(time, euc[0], label='Euler-Cromer')
plt.plot(time, ve[0], label='Verlat')
plt.plot(time, vev[0], label='Velocity-Verlat')
plt.plot(time, bee[0], label='Beeman')
plt.xlabel('time')
plt.ylabel('x')
plt.title("solution for d^2 x / dt^2 = - x using different methods")
plt.legend()
plt.savefig("9.2A different methods.jpg", bbox_inches='tight')
plt.show()

# Part B:In this part we calculate and show the phase diagram. the diagrams will save separately.

plt.plot(eu[0], eu[1], label='Euler')
plt.xlabel('x')
plt.ylabel('x_dot')
plt.title("Phase diagram using Euler")
plt.savefig("9.2B Euler.jpg", bbox_inches='tight')
plt.close()

plt.plot(euc[0], euc[1], label='Euler-Cromer')
plt.xlabel('x')
plt.ylabel('x_dot')
plt.title("Phase diagram using Euler-Cromer")
plt.savefig("9.2B Euler-Cromer.jpg", bbox_inches='tight')
plt.close()

plt.plot(ve[0], ve[1], label='Verlat')
plt.xlabel('x')
plt.ylabel('x_dot')
plt.title("Phase diagram using Verlat")
plt.savefig("9.2B Verlat.jpg", bbox_inches='tight')
plt.close()

plt.plot(vev[0], vev[1], label='Velocity-Verlat')
plt.xlabel('x')
plt.ylabel('x_dot')
plt.title("Phase diagram using Velocity-Verlat")
plt.savefig("9.2B Velocity-Verlat.jpg", bbox_inches='tight')
plt.close()

plt.plot(bee[0], bee[1], label='Beeman')
plt.xlabel('x')
plt.ylabel('x_dot')
plt.title("Phase diagram using Beeman")
plt.savefig("9.2B Beeman.jpg", bbox_inches='tight')
plt.close()

# Part C: Energy of the system (considering omega(w) = k = 1

# Variables
ttime = np.linspace(1, 60, 60)

meu = np.zeros(len(ttime))
mec = np.zeros(len(ttime))
mve = np.zeros(len(ttime))
mvv = np.zeros(len(ttime))
mbe = np.zeros(len(ttime))

# Finding maximum velocity to find A. from A we can calculate energy
for i in range(len(ttime)):
    time = ttime[i]
    eu = euler(xi, step, time)
    euc = euler_cromer(xi, step, time)
    ve = verlat(xi, step, time)
    vev = velocity_verlat(xi, step, time)
    bee = beeman(xi, step, time)
    meu[i] = np.amax(eu[1])
    mec[i] = np.amax(euc[1])
    mve[i] = np.amax(ve[1])
    mvv[i] = np.amax(vev[1])
    mbe[i] = np.amax(bee[1])

E = meu * meu / 2
plt.plot(ttime, E, label='Euler')

E = mec * mec / 2
plt.plot(ttime, E, label='Euler-Cromer')

E = mve * mve / 2
plt.plot(ttime, E, label='Verlat')

E = mvv * mvv / 2
plt.plot(ttime, E, label='Velocity-Verlat')

E = mbe * mbe / 2
plt.plot(ttime, E, label='Beeman')

plt.xlabel('Time')
plt.ylabel('Energy')
plt.title("Energy verus Time")
plt.legend()
plt.savefig("9.2C Energy.Time.jpg", bbox_inches='tight')
plt.show()
