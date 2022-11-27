import numpy as np
import matplotlib.pyplot as plt


def count_closed_paths(grid, closed_paths_numbers, i, j, length):
    if length == 0:
        return
    else:
        closed_paths_count = 0
        steps_states = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for step in steps_states:
            new_i, new_j = step[0] + i, step[1] + j
            if grid[new_j][new_i] == 0:
                grid[new_j][new_i] = 1
                count_closed_paths(grid, closed_paths_numbers, new_i, new_j, length - 1)
                grid[new_j][new_i] = 0
            else:
                closed_paths_count += 1

        closed_paths_numbers[-length:] += (4 ** np.arange(0, length)) * closed_paths_count


def count_self_avoiding_paths(length, save=False):
    closed_paths_numbers = np.zeros(length, dtype=int)
    grid = np.zeros((2 * length + 1, 2 * length + 1), dtype=bool)
    i = j = length
    grid[j][j] = 1
    count_closed_paths(grid, closed_paths_numbers, i, j, length)

    total_paths_counts = 4 ** np.arange(1, length + 1)
    self_avoiding_paths_count = total_paths_counts - closed_paths_numbers

    if save:
        data = {
            'length': length,
            'counts': self_avoiding_paths_count
        }
        np.save("data/q7_" + str(length), data)

    return self_avoiding_paths_count


def show(length=3, file_name=None):
    print('1')
    if file_name is None:
        self_avoiding_paths_numbers = count_self_avoiding_paths(length, save=True)
    else:
        data = np.load('data/q7_' + file_name + '.npy', allow_pickle=True).tolist()
        length = data['length']
        self_avoiding_paths_numbers = data['counts']

    n_s = np.arange(1, length + 1)
    self_avoiding_paths_percentages = self_avoiding_paths_numbers / (4 ** n_s)

    plt.plot(n_s, self_avoiding_paths_numbers, linestyle='', marker='.', markersize=5)
    plt.xlabel(r'$N$')
    plt.ylabel(r'self avoiding paths count')
    plt.savefig(
        "images/q7_self_avoiding_count_" + str(length) + '.png')
    plt.show()

    plt.plot(n_s, self_avoiding_paths_percentages, linestyle='', marker='.', markersize=5)
    plt.xlabel(r'$N$')
    plt.ylabel(r'self avoiding paths percentage')
    plt.savefig(
        "images/q7_self_avoiding_percentage_" + str(length) + '.png')
    plt.show()

    print(self_avoiding_paths_numbers)


count_self_avoiding_paths(3, save=True)
show(file_name='3')