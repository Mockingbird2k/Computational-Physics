from numba import jit, cuda
import numpy as np
import matplotlib.pyplot as plt
import datetime

time = datetime.datetime.now()


def best_slope(x_arr, y_arr):  # finds the best slope,passes through arrays 'x_arr' and 'y_arr'
    xbar = np.average(x_arr)
    ybar = np.average(y_arr)
    xybar = np.average(x_arr * y_arr)
    x2bar = np.average(x_arr ** 2)
    slope = (xbar * ybar - xybar) / (xbar ** 2 - x2bar)
    return slope


# class of Ising

class ising:
    def __init__(self, beta, L):

        # parameters of ising are

        self.grid = self.random_grid(L)
        self.beta = beta
        self.T = 1 / beta
        self.exp_table = np.exp([-8 / self.T, -4 / self.T, 0, 4 / self.T, 8 / self.T])  # used for faster calculation
        self.L = L
        self.tau = 0  # Relaxation Time
        self.ksi = 0  # Length correlation
        self.measurement_counter = 0    # we use 'measurement_counter' for counting the "monte Carlo steps"
                                        # (each has L**2 steps) which occurs after equilibrium!!! so
                                        # 'measurement_counter' will be increased at the end of 'metropolis' function

        self.step = 0  # current step of system(after the initialization)
        self.equilibrium = 0  # if this be zero means syatem is not in equilibrium
                               # and if be 1 means system has passed equilibrium point!

        self.energy = self.beginning_energy()
        self.energy_array = np.zeros(1000)  # after equilibrium this array will be filled
                                            # and we will calculate energy correlation

        self.magnetization_array = None  # after finding Relaxation Time(tau)
                                         # this array will be filled and we will use it for data gathering

        self.ksi_array = None  # after finding Relaxation Time(tau)
                               # this array will be filled and we will use it for data gathering

        self.cv_array = None  # after finding Relaxation Time(tau)
                              # this array will be filled and we will use it for data gathering

        self.khi_array = None  # after finding Relaxation Time(tau)
                               # this array will be filled and we will use it for data gathering

        self.precision = 0.1  # if "delta E/E" is smaller than 'precision' we have equilibrium
        self.cycle = 200  # 20 may be enough.we save the energies of every 'cycle'
                          # and if "delta E/E" be smaller than 'precision' we have reached equilibrium!!!

        self.equilibrium_energy_array = np.zeros(self.cycle)

        # functions of Ising:

    # function below makes a random grid (L,L) with "binary" values(0 for down and 1 for up) and return it


    def random_grid(self, L):
        grid = np.random.choice([-1, 1], size=(L, L))
        return grid

    def beginning_energy(self):  # calculates the beginning amount of energy
        E = 0
        for i in range(L):
            for j in range(L):
                E += self.spin_energy(i, j)
        E = E / 2
        return E

    def equillibirium_energy_array_update(self):
        self.equilibrium_energy_array[self.measurement_counter % self.cycle] = self.energy

    def metropolis(self):  # main function that changes the spins of grid

        # 'x_rand' and 'y_rand' are position of spins which we are going to change them by "metorpolis" algorithm

        x_rand = np.random.choice(np.arange(0, L), size=(self.L) ** 2)
        y_rand = np.random.choice(np.arange(0, L), size=(self.L) ** 2)

        for i in range((self.L) ** 2):
            if self.step_accept(x_rand[i], y_rand[i]) == 1:

                # below updates energy of system

                self.energy += (-2 * self.spin_energy(x_rand[i], y_rand[i]))


                self.grid[x_rand[i], y_rand[i]] = (
                    -self.grid[x_rand[i], y_rand[i]])  # changes the spin if the metropolis step is accepted


            # updates the step of system

            self.step += 1



    def step_accept(self, x,
                    y):  # if 'step_accept'==0 means the metropolis step is not accepted and if 'step_accept'==1 means the metropolis step is accepted
        if -2 * self.spin_energy(x, y) <= 0:
            return 1
        else:
            rand = np.random.random()
            if -2 * self.spin_energy(x, y) == 8:
                if rand <= (self.exp_table[0]):
                    return 1
            if -2 * self.spin_energy(x, y) == 4:
                if rand <= (self.exp_table[1]):
                    return 1
        return 0

    def spin_energy(self, x, y):  # finds the energy of a specific spin in the grid
        spin_energy = np.sum(
            (self.grid[x - 1, y], self.grid[(x + 1) % L, y], self.grid[x, y - 1], self.grid[x, (y + 1) % L]))
        if spin_energy == 0:
            return 0
        elif spin_energy > 0:
            if self.grid[x, y] == 1:
                return -spin_energy
            else:
                return spin_energy
        elif spin_energy < 0:
            if self.grid[x, y] == 1:
                return -spin_energy
            else:
                return spin_energy

    def equilibrium_check(self):  # if equilibrium happens it changes 'self.equilibrium' AND ALSO RETURNS 1
        if self.equilibrium == 1:
            return 1
        else:
            if abs(((np.var(self.equilibrium_energy_array)) ** 0.5) / np.average(
                    self.equilibrium_energy_array)) < self.precision:
                self.equilibrium = 1
                self.measurement_counter = 0
                return 1
        return 0

    def correlation(self, pos_array):  # takes 'pos_array' and calculates its correlation
        sigma2 = np.var(pos_array)
        j_number = int(len(pos_array) / 10)  # j_number  determines until which number we calculate correlation
        if sigma2 != 0:
            cor_array = np.zeros(j_number)
            for j in range(j_number):
                cor_array[j] = np.dot(pos_array, np.roll(pos_array, j))
                cor_array[j] = cor_array[j] / len(pos_array)
                cor_array[j] = cor_array[j] - (np.average(pos_array)) ** 2
                cor_array[j] = cor_array[j] / sigma2
            return j_number - len(cor_array[cor_array < np.exp(-1)]) + 1

    # returns 'self.ksi'(length correlation of system)

    def length_correlation(self):
        sigma2 = np.var(self.grid)
        j_number = int(self.L / 10)
        cor_array = np.zeros(shape=(L, j_number))
        for i in range(self.L):
            for j in range(j_number):
                cor_array[i, j] = np.dot(self.grid[i, :], np.roll(self.grid[i, :], j))
                cor_array[i, j] = cor_array[i, j] / self.L
                cor_array[i, j] = cor_array[i, j] - np.average(self.grid[i, :]) ** 2
        result = np.zeros(j_number)  # this is the final length correlation
        result = np.average(cor_array, axis=0)
        result = result / sigma2
        return j_number - len(result[result < np.exp(-1)]) + 1





'''global variables are as follows:'''
# L_array=
beta_array = np.array(
    [0.1, 0.2, 0.3, 0.38, 0.39, 0.4, 0.41, 0.415, 0.42, 0.423, 0.426, 0.43, 0.433, 0.436, 0.44, 0.45, 0.5, 0.6])
L = 100  # length of grid
N = 10  # number of data we take from each lattice
sample_number = 4  # number of samples we average over
global grid  # this grid is global
grid = ising(beta_array[0], L)
cv_array = np.zeros(shape=(len(beta_array), sample_number))
khi_array = np.zeros(shape=(len(beta_array), sample_number))
magnetization_array = np.zeros(shape=(len(beta_array), sample_number))
energy_array = np.zeros(shape=(len(beta_array), sample_number))


m = 0
while m < len(beta_array):
    beta = beta_array[m]
    for num in range(sample_number):
        lattice = ising(beta, L)
        # in below we find equilibrium

        while 1:
            i = 0
            while i < 350:
                lattice.metropolis()
                lattice.equillibirium_energy_array_update()
                lattice.measurement_counter += 1
                lattice.equilibrium_check()
                if lattice.equilibrium == 1:
                    break
                i += 1
            if lattice.equilibrium == 0:
                lattice.precision *= 10
                continue
            else:
                break

        # system now is in equilibrium


        lattice.measurement_counter = 0
        for i in range(len(lattice.energy_array)):
            lattice.metropolis()
            lattice.energy_array[i] = lattice.energy
            lattice.measurement_counter += 1

        lattice.tau = lattice.correlation(lattice.energy_array)
        lattice.magnetization_array = np.zeros(20 * N)
        lattice.energy_array = np.zeros(20 * N)
        lattice.khi_array = np.zeros(N)
        lattice.cv_array = np.zeros(N)
        lattice.ksi_array = np.zeros(N)

        # in below we gather data from the lattice

        lattice.measurement_counter = 0
        for k in range(N):
            for j in range(20):
                for i in range(int(lattice.tau)):
                    lattice.metropolis()
                    lattice.measurement_counter += 1

                lattice.energy_array[20 * k + j] = lattice.energy
                lattice.magnetization_array[20 * k + j] = abs(np.sum(lattice.grid))

            lattice.ksi_array[k] = lattice.length_correlation()
            lattice.cv_array[k] = ((lattice.beta) ** 2) * np.var(lattice.energy_array[20 * k:20 * (k + 1)])
            lattice.khi_array[k] = lattice.beta * np.var(lattice.magnetization_array[20 * k:20 * (k + 1)])

        cv_array[m, num] = np.average(lattice.cv_array)
        khi_array[m, num] = np.average(lattice.khi_array)
        magnetization_array[m, num] = np.average(lattice.magnetization_array)
        energy_array[m, num] = np.average(lattice.energy_array)
        print('sample_number:', num, 'of beta=', beta, 'finished')
    m += 1

cv_array = np.average(cv_array, axis=1)
magnetization_array = np.average(magnetization_array, axis=1)
energy_array = np.average(energy_array, axis=1)
khi_array = np.average(khi_array, axis=1)

fig1, pic1 = plt.subplots(1, figsize=(20, 10))
pic1.set_xlabel('beta')
pic1.set_ylabel('cv')
pic1.plot(beta_array, cv_array)

fig2, pic2 = plt.subplots(1, figsize=(20, 10))
pic2.set_xlabel('beta')
pic2.set_ylabel('magnetization')
pic2.plot(beta_array, magnetization_array)

fig3, pic3 = plt.subplots(1, figsize=(20, 10))
pic3.set_xlabel('beta')
pic3.set_ylabel('energy')
pic3.plot(beta_array, energy_array)

fig4, pic4 = plt.subplots(1, figsize=(20, 10))
pic4.set_xlabel('beta')
pic4.set_ylabel('khi')
pic4.plot(beta_array, khi_array)

print(datetime.datetime.now() - time)
