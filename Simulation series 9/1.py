import numpy as np
import matplotlib.pyplot as plt

# Introducing Functions


# The Analytical Answer of Q
def analytical_sol(x):
    return 0.00001 * (1 - np.exp(-x/0.003))


# The Euler Method (entries are inital value, steps, time) (This method solves equation step by step)
def euler(xi, step, time):
    count = int(time / step)
    count += 1
    x = np.zeros(count)
    x[0] = xi
    for i in range(count - 1):
        x[i + 1] = x[i] + step * 10/3000 + (1000/3) * step * -1 * x[i]
    return x, count


# Initial Variables


xi = 0
step = 1/1000000 # Step size
end = 0.02



# solving the equation

# integrate
Q, count = euler(xi, step, end)
time = np.linspace(0, end, count)


# Plotting
plt.plot(time, Q, ls='--', label='simulation')
#plt.plot(time, analytical_sol(time), ls='-', label='analytical sol.')
plt.xlabel('time (s)')
plt.ylabel('charge Q (c)')
plt.legend()
plt.show()


# Comparing Analytical solution and Simulation

# list of steps to find delta
steps = np.linspace(100, 100000, 1000)

# find the expected value of Q using the analytical solution
x_end = analytical_sol(end)

# stores the difference in the numeric and analytic solutions
delta = np.zeros(len(steps))

# data aquisition

for i in range (len(steps)):
    step = 1/steps[i]
    steps[i] = end / steps[i]
    Q, _ = euler(xi, step, end)

    delta[i] = (np.absolute(x_end - Q[-1]))
print(delta[0], delta[1])

# Plotting

plt.plot(steps, delta, label='data')
plt.xlabel('time step (h)')
plt.ylabel('error (delta)')
plt.legend()
plt.show()
