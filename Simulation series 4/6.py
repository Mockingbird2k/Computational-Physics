


import numpy as np
import random
import matplotlib.pyplot as plt


sample_number=10000 #number of samples we average over
line=20  #length of grid it is
initial_pos_array=np.arange(0,line)
p=1/2
q=1-p
x_position=0  #shows position of object 


T_bar_ensemble_array=np.zeros(len(initial_pos_array))

j=0
while j<len(initial_pos_array):
    s=0
    T_bar=0
    while s<sample_number:
        x_position=initial_pos_array[j]
        t=0
        T=0
        while 1:
            rand=random.random()
            if rand<p:
                x_position-=1
            else:
                x_position+=1
            if x_position==-1 or x_position==line:
                T=t
                break
            t+=1
        T_bar=T_bar+T
        s+=1
    T_bar_ensemble_array[j]=T_bar/sample_number  #dividing is for averaging
    j+=1
    
print(np.average(T_bar_ensemble_array))
for j in range(0,len(initial_pos_array)):
    plt.plot(initial_pos_array,T_bar_ensemble_array)
plt.show()