import numpy as np
import matplotlib.pyplot as plt

numbers = np.array([5, 10, 100, 1000])
sample_number = 100000  # numbers of each data
result = np.zeros(shape=(sample_number, len(numbers)))


for i in range(0, len(numbers)):
    N = numbers[i]
    rand_array = np.random.randint(1, 10, size=N*sample_number)
    rand_array = rand_array.reshape(sample_number, N)
    for j in range(N):
        result[:, i] = result[:, i] + rand_array[:, j]
    result[:, i] = result[:, i]/N

fig, ((pic1, pic2), (pic3, pic4)) = plt.subplots(2, 2, figsize=(10, 10))
pic1.hist(result[:, 0], bins=np.arange(.5, 9, .1), rwidth=5)
pic2.hist(result[:, 1], bins=np.arange(2, 8, .1), rwidth=0.5)
pic3.hist(result[:, 2], bins=np.arange(4, 6, .05), rwidth=0.5)
pic4.hist(result[:, 3], bins=np.arange(4.5, 5.5, .01), rwidth=0.5)

plt.show()
