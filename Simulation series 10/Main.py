from classes.MD_system import MDSystem
import numpy as np
from matplotlib import pyplot as plt


def auto_correlation(arr, tau):
    """ return auto correlation of particles for a separation value tau """
    auto_cor = np.mean(np.sum(arr[:-tau] * arr[tau:], axis=2))
    auto_cor /= np.mean(np.sum(arr[:-tau] ** 2, axis=2))
    return auto_cor


def simulate_system(init_vel):
    """ simulate the system for init_vel and take temp. and energy"""
    # initial data
    size = 30
    num_particle = 100
    xs = np.repeat(np.linspace(0.1, 0.45, 10), 10)
    ys = np.tile(np.linspace(0.1, 0.9, 10), 10)
    init_pos = np.vstack((xs * size, ys * size))
    kargs = {'num': num_particle,'L': size,'init_pos': init_pos.T,'init_vel': init_vel}

    system = MDSystem(**kargs)  # instantiating the system

    # wait for system to reach equilibrium
    for _ in range(5000):
        system.timestep()

    energy = system.energy()
    temp = np.zeros(1000)
    pressure = np.zeros(1000)
    for i in range(1000):
        for _ in range(10):
            system.timestep()
        temp[i] = system.temp()
        pressure[i] = system.reduced_pressure()

    return energy, np.mean(temp), np.std(temp), np.mean(pressure), np.std(pressure)


"""______________________________________________Main Body___________________________________________________________"""

""" Data """

velocity = np.linspace(0.1, 2, 40)

temps = np.zeros((40, 2))
pressures = np.zeros((40, 2))
energies = np.zeros(40)

for index, init_vel in enumerate(velocity):
    energies[index], temps[index, 0], temps[index, 1], pressures[index, 0], pressures[index, 1] = \
        simulate_system(init_vel)

np.save("data/temps_phase_transition.npy", temps)
np.save("data/energies_phase_transition.npy", energies)
np.save("data/pressure_phase_transition.npy", pressures)
#######################################################################################################################

""" Energy """

# initial data
size = 30
num_particle = 100
xs = np.repeat(np.linspace(0.1, 0.45, 10), 10)
ys = np.tile(np.linspace(0.1, 0.9, 10), 10)
init_pos = np.vstack((xs * size, ys * size))
kargs = {'num': 100,'L': 30,'init_pos': init_pos.T,'init_vel': 0.5}

system = MDSystem(**kargs)  # instaciating the system
num = 50000

kinetic = np.zeros(num)
potential = np.zeros(num)
left_side = np.zeros(num)

for i in range(num):
    system.timestep()   # evovle system
    left_side[i] = np.sum(system.dots[:, 0] < system.size / 2.0) # number of particles on the left side
    kinetic[i] = system.kinetic()   # kinetic energy of the system
    potential[i] = system.potential()   # potential energy of the system

x_axis = np.linspace(1, num, num)
# plot energies
plt.plot(x_axis, potential, label=r'potential $V$')
plt.plot(x_axis, kinetic, label=r'kinetic $K$')
plt.plot(x_axis, kinetic + potential, label=r'energy $K + V$')
plt.legend()
plt.savefig(f"results/energy_conservation{system.num_particle}_{num}.jpg")
plt.show()

# plot particles on the left side of the system
plt.plot(np.linspace(1, num, num), left_side)
plt.xlabel(r'time ($10^{-3} \tau$)')
plt.ylabel('number of particles on the left side of the box')
plt.title(f"total number of particles = {system.num_particle}")
plt.grid()
plt.savefig(f"results/particles_on_left{system.num_particle}_{num}.jpg")
plt.show()
#######################################################################################################################

""" Phase Transition"""
temps = np.load("data/temps_phase_transition.npy")
energy = np.load("data/energies_phase_transition.npy")
print(temps)
pressure = np.load('data/pressure_phase_transition.npy')

plt.errorbar(x=temps[:, 0], y=energy, xerr=temps[:, 1])
plt.xlabel("T")
plt.ylabel("E")
plt.title("E vs. T plot to see phase transition")
plt.savefig("results/phase_transition.jpg")
plt.show()

plt.errorbar(x=temps[:, 0], y=pressure[:, 0], xerr=temps[:, 1], yerr=pressure[:, 1], ls='-.')
plt.xlabel("T")
plt.ylabel("P")
plt.title("Pressure vs. Temp.")
plt.savefig("results/pressure_temp.jpg")
plt.show()
########################################################################################################################

"""Analyze the Temperature and Pressure"""
# initial data
size = 30
num_particle = 100
xs = np.repeat(np.linspace(0.1, 0.45, 10), 10)
ys = np.tile(np.linspace(0.1, 0.9, 10), 10)
init_pos = np.vstack((xs * size, ys * size))
kargs = {'num': num_particle,'L': size,'init_pos': init_pos.T,'init_vel': 1.5}

system = MDSystem(**kargs)  # instantiating the system
num = 5000

temp = np.zeros(num)
pressure = np.zeros(num)

for i in range(num):
    for _ in range(10):
        system.timestep()
    temp[i] = system.temp()
    pressure[i] = system.reduced_pressure()

x_axis = np.linspace(1, num, num)  # time axis
# plot temp
plt.plot(x_axis, temp)
plt.xlabel("time")
plt.ylabel('temperature T')
plt.title(f"number of particles = {system.num_particle}")
plt.grid()
plt.savefig(f"results/temp{system.num_particle}_{num}.jpg")
plt.show()

# plot pressure
plt.plot(x_axis, pressure)
plt.xlabel("time")
plt.ylabel('pressure P')
plt.title(f"number of particles = {system.num_particle}")
plt.grid()
plt.savefig(f"results/pressure{system.num_particle}_{num}.jpg")
plt.show()

print(f'\nEqualized Temp. is {np.mean(temp[-3000:])} (+/-) {np.std(temp[-3000:])} K')
print(f'Equalized pressure is {np.mean(pressure[-3000:])} (+/-) {np.std(pressure[-3000:])}')
########################################################################################################################

""" calculate the velocity auto-correlation """
velocity = np.load('data/velocity100_5000.npy')
end = np.exp(-1)

tau = 0
vel_cor = [auto_correlation(velocity, tau + 1)]
while vel_cor[-1] > end:
    print(f"\r ==> tau = {tau}", end='')
    tau += 1
    vel_cor.append(auto_correlation(velocity, tau + 1))

cutoff = tau
for _ in range(400):
    tau += 1
    vel_cor.append(auto_correlation(velocity, tau + 1))

print(f"\n\n ==> system relaxation time is: {2 * cutoff}")

num = len(vel_cor)
plt.plot(np.linspace(1, num, num), vel_cor, label=r"$C_v(\tau)$")
plt.plot(np.linspace(1, num, num), [end] * num, label=r"$e^{-1}$")
plt.xlabel(r"time $(unit = 2 \times 10^{-3})$")
plt.legend()
plt.savefig("results/velocity_correlation.jpg")
plt.show()
########################################################################################################################

""" Animate """
# initial data
size = 30
num_particle = 100
xs = np.repeat(np.linspace(0.1, 0.45, 10), 10)
ys = np.tile(np.linspace(0.1, 0.9, 10), 10)
init_pos = np.vstack((xs * size, ys * size))
kargs = {'num': num_particle,'L': size,'init_pos': init_pos.T,'init_vel': 3}

system = MDSystem(**kargs)  # instantiating the system
for _ in range(2000):
    system.timestep()

system.animate_system("animations/gas_phase")
