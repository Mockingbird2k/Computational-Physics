

import numpy as np
import random
import matplotlib.pyplot as plt



def best_slope(x_arr,y_arr):  #finds the best slope,passes through arrays 'x_arr' and 'y_arr'
    xbar=np.average(x_arr)
    ybar=np.average(y_arr)
    xybar=np.average(x_arr*y_arr)
    x2bar=np.average(x_arr**2)
    slope=(xbar*ybar-xybar)/(xbar**2-x2bar)
    return slope


sample_number=8000 #number of samples we average over
probability_array=[.2,0.3,0.4,0.5]
p=probability_array[0]
q=1-p
time_array=np.array([100,200,300,400,500])
time=time_array[0]
x_bar_array=np.zeros(len(time_array))
x_position=0  #shows position of object 


x_bar_ensemble_array=np.zeros(shape=(len(probability_array),len(time_array)))
x2_bar_ensemble_array=np.zeros(shape=(len(probability_array),len(time_array)))

j=0
while j<len(probability_array):
    p=probability_array[j]
    i=0
    while i<len(time_array):
        time=time_array[i]
        s=0
        x_bar=0
        x2_bar=0
        while s<sample_number:
            x_position=0
            t=0
            while t<time:
                rand=random.random()
                if rand<p:
                    x_position-=1
                else:
                    x_position+=1
                t+=1
            x2_bar=x2_bar+x_position**2
            x_bar=x_bar+x_position
            s+=1
        x2_bar_ensemble_array[j,i]=x2_bar/sample_number  #dividing is for averaging
        x_bar_ensemble_array[j,i]=x_bar/sample_number  #dividing is for averaging
        i+=1
    j+=1
    
sigma2_ensemble_array=x2_bar_ensemble_array-(x_bar_ensemble_array)**2
fig,  (pic1,pic2)=plt.subplots(1,2,figsize=(10,10))
for j in range(0,len(probability_array)):
    print('best slope for line of x_bar with probability=',probability_array[j],'is:')
    p = probability_array[j]
    q = 1 - p

    if p-q < 0.0:
        x_bar_ensemble_array[j] = -1 * x_bar_ensemble_array[j]

    print(best_slope(time_array, x_bar_ensemble_array[j]))
    pic1.plot(time_array,x_bar_ensemble_array[j])
    print('best slope for line of sigma^2 with probability=',probability_array[j],'is:')
    print(best_slope(time_array,sigma2_ensemble_array[j]))
    pic2.plot(time_array,sigma2_ensemble_array[j])
plt.show()