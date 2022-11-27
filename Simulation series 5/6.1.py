
import numpy as np
import matplotlib.pyplot as plt





def best_slope(x_arr,y_arr):  #finds the best slope,passes through arrays 'x_arr' and 'y_arr'
    xbar=np.average(x_arr)
    ybar=np.average(y_arr)
    xybar=np.average(x_arr*y_arr)
    x2bar=np.average(x_arr**2)
    slope=(xbar*ybar-xybar)/(xbar**2-x2bar)
    return slope


N_array=np.zeros(10)
increament=1
sigma_N_array=np.zeros(10)
for n in range(1,11):
    N=increament
    increament*=2
    rand=np.array(N)
    rand=np.random.randint(1,10,size=N)
    number_of_numbers=np.zeros(9,dtype=int)  #this array keeps number of every number.FOR EXAMPLE how many times number '4' has come
    for j in range(1,10):
        number_of_numbers[j-1]=len(rand[rand==j])
    sigma_N_array[n-1]=((np.var(number_of_numbers))**0.5)/N
    #print(sigma_N_array)
    N_array[n-1]=N





fig, (pic1,pic2)=plt.subplots(2,figsize=(10,10))
pic1.hist(rand,bins=np.arange(.5,10.5,1),rwidth=.5)
pic2.scatter(np.log(N_array),np.log(sigma_N_array))
print('best slope is:')
print(best_slope(np.log(N_array),np.log(sigma_N_array)))

plt.show()
