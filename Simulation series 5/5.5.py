
import numpy as np
import matplotlib.pyplot as plt
import datetime

time=datetime.datetime.now()


sample_number=4000
u=1/4  #probability of jumping up
d=1/4  #probability of jumping down
l=1/4  #probability of jumping left
r=1/4  #probability of jumping right
Ti=10  #minimum steps of random walk
Tf=50  #maximum steps of random walk


def evo():
    global grid
    for i in range(T):
        rand_array=np.random.random_sample(sample_number)
        for j in range(sample_number):
            if 0<rand_array[j]<u:
                grid[j,current_x[j],current_y[j]+1]=1
                current_y[j]+=1
            elif u<rand_array[j]<(u+d):
                grid[j,current_x[j],current_y[j]-1]=1
                current_y[j]-=1
            elif (u+d)<rand_array[j]<(u+d+l):
                grid[j,current_x[j]-1,current_y[j]]=1
                current_x[j]-=1
            elif (u+d+l)<rand_array[j]<1:
                grid[j,current_x[j]+1,current_y[j]]=1
                current_x[j]+=1



def x2finder():  #finds the average variance of x over all samples
    global grid
    x2_bar=np.zeros(sample_number)  #contains <x^2> of each sample in time 'T'
    for k in range(sample_number):
        for i in range((2*T)+1):
            for j in range((2*T)+1):
                if grid[k,i,j]==1:
                    x2_bar[k]+=(j-T)**2
        x2_bar[k]=x2_bar[k]/(np.sum(grid[k,:,:]))  #divided by the total "mass"
    x2_bar_average=np.average(x2_bar)
    return x2_bar_average


def y2finder():  #finds the average variance of y over all samples
    global grid
    y2_bar=np.zeros(sample_number)  #contains <y^2> of each sample in time 'T' 
    for k in range(sample_number):
        for i in range((2*T)+1):
            for j in range((2*T)+1):
                if grid[k,i,j]==1:
                    y2_bar[k]+=(i-T)**2
        y2_bar[k]=y2_bar[k]/(np.sum(grid[k,:,:]))  #divided by the total "mass"
    y2_bar_average=np.average(y2_bar)
    return y2_bar_average



def best_slope(x_arr,y_arr):  #finds the best slope,passes through arrays 'x_arr' and 'y_arr'
    xbar=np.average(x_arr)
    ybar=np.average(y_arr)
    xybar=np.average(x_arr*y_arr)
    x2bar=np.average(x_arr**2)
    slope=(xbar*ybar-xybar)/(xbar**2-x2bar)
    return slope





r2_array=np.zeros(Tf-Ti)
for T in range(Ti,Tf):
    grid=np.zeros(shape=(sample_number,2*T+1,2*T+1),dtype=int)
    grid[:,T,T]=1
    current_x=np.zeros(sample_number,dtype=int)
    current_x[:]=T
    current_y=np.copy(current_x)    
    evo()
    x2bar=x2finder()
    y2bar=y2finder()
    r2_array[T-Ti]=x2bar+y2bar
    
    
plt.scatter(range(Ti,Tf),r2_array)
print('best slope is:')
print(best_slope(np.arange(Ti,Tf),r2_array))
print(datetime.datetime.now()-time)

plt.show()
        
      