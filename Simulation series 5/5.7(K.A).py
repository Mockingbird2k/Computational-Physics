import numpy as np
import matplotlib.pyplot as plt
'''Set the defaults for your plots.'''
# plt.rcParams.update({'font.size': 20, 'figsize':(8,6)})
SMALL_SIZE = 12
MEDIUM_SIZE = 15
BIGGER_SIZE = 18

plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

plt.rc('axes', linewidth = 3 )
plt.rc('lines', linewidth = 2)

plt.rc('lines', markersize = 3)

plt.rc('figure', figsize=(15,10) )         # Image size


import warnings
warnings.filterwarnings('ignore')


def walks(n):
    if n == 1:
        return [[0], [1], [2], [3]]
    else:
        L = []
        for k in walks(n - 1):
            for i in range(4):
                if (k[-1] != 0 and i == 2):
                    L.append(k + [i])
                if (k[-1] != 2 and i == 0):
                    L.append(k + [i])
                if (k[-1] != 3 and i == 1):
                    L.append(k + [i])
                if (k[-1] != 1 and i == 3):
                    L.append(k + [i])
        return L


def walks2(n, m):
    L1 = []
    paths = walks(m)
    for k in paths:
        points = [[0, 0]]
        for i in range(len(k)):
            if (k[i] == 0):
                x = points[i][0] + 1
                y = points[i][1]
            if (k[i] == 1):
                y = points[i][1] + 1
                x = points[i][0]
            if (k[i] == 2):
                x = points[i][0] - 1
                y = points[i][1]
            if (k[i] == 3):
                y = points[i][1] - 1
                x = points[i][0]
            if [x, y] in points:
                break
            else:
                points += [[x, y]]
            if i == len(k) - 1:
                L1 += [k]
    count = 0
    for l in L1:
        for j in range(0, 4 ** (n - m)):
            L2 = []
            number = j
            quaternary = int(np.base_repr(number, base=4))
            for i in range(n - m):
                L2 += [quaternary % 10]
                quaternary = (quaternary // 10)
            L2.reverse()
            L = l + L2
            determiner = 0
            for i in range(m - 1, n - 1):
                if L[i] == 1 and L[i + 1] == 3:
                    determiner += 1
                    break
                if L[i] == 3 and L[i + 1] == 1:
                    determiner += 1
                    break
                if L[i] == 0 and L[i + 1] == 2:
                    determiner += 1
                    break
                if L[i] == 2 and L[i + 1] == 0:
                    determiner += 1
                    break
            if determiner == 0:
                points = [[0, 0]]
                for i in range(len(L)):
                    if (L[i] == 0):
                        x = points[i][0] + 1
                        y = points[i][1]
                    if (L[i] == 1):
                        y = points[i][1] + 1
                        x = points[i][0]
                    if (L[i] == 2):
                        x = points[i][0] - 1
                        y = points[i][1]
                    if (L[i] == 3):
                        y = points[i][1] - 1
                        x = points[i][0]
                    if [x, y] in points:
                        break
                    else:
                        points += [[x, y]]
                    if i == len(L) - 1:
                        count += 1

    return count
paths=[]
for i in range(1,21):
    paths+=[4**i]
paths=np.array(paths)

fig, ax = plt.subplots()
plt.xlabel("number of steps",fontsize=30)
plt.ylabel("number of paths(1e12)",fontsize=30)
plt.title("Number of all paths in a 2D walk",fontsize=20)
plt.plot(np.arange(1,21),paths,'.b-',markersize=2)
ax.tick_params(labelsize=20)
ax.legend()