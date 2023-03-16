from classes.MD_system import MDSystem
import numpy as np
from matplotlib import pyplot as plt

def auto_correlation(arr, tau):
    """ return auto correlation of particles for a seperation value tau """
    auto_cor = np.mean(np.sum(arr[:-tau] * arr[tau:], axis=2))
    auto_cor /= np.mean(np.sum(arr[:-tau] ** 2, axis=2))
    return auto_cor




""" calculate the velocity auto-correlation """
velocity = np.linspace(0.1, 2, 40)
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

""" Energy """

# initial data
size = 30
num_particle = 100
xs = np.repeat(np.linspace(0.1, 0.45, 10), 10)
ys = np.tile(np.linspace(0.1, 0.9, 10), 10)
init_pos = np.vstack((xs * size, ys * size))
kgs = {
    'num': 100,
    'L': 30,
    'init_pos': init_pos.T,
    'init_vel': 0.5
}

system = MDSystem(**kgs)  # instaciating the system
num = 50000

kinetic = np.zeros(num)
potential = np.zeros(num)
left_side = np.zeros(num)

for i in range(num):
    print(f"\r [Info]:main:timestep {i}", end='')
    system.timestep()  # evovle system
    left_side[i] = np.sum(system.dots[:, 0] < system.size / 2.0)  # number of particles on the left side
    kinetic[i] = system.kinetic()  # kinetic energy of the system
    potential[i] = system.potential()  # potential energy of the system

x_axis = np.linspace(1, num, num)
# plot energies
plt.plot(x_axis, potential, label=r'potential $V$')
plt.plot(x_axis, kinetic, label=r'kinetic $K$')
plt.plot(x_axis, kinetic + potential, label=r'energy $K + V$')
plt.legend()
plt.savefig(f"results/energy_conservation{system.num_particle}_{num}.jpg",
            dpi=200, bbox_inches='tight')
plt.show()

# plot particles on the left side of the system
plt.plot(np.linspace(1, num, num), left_side)
plt.xlabel(r'time ($10^{-3} \tau$)')
plt.ylabel('number of particles on the left side of the box')
plt.title(f"total number of particles = {system.num_particle}")
plt.grid()
plt.savefig(f"results/particles_on_left{system.num_particle}_{num}.jpg", dpi=200, bbox_inches='tight')
plt.show()
