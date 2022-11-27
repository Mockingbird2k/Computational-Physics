


import numpy as np
import matplotlib.pyplot as plt
from numba import jit


line=20  #length of grid it is
line=line+2 #"+2" is for two valley in which object dies in!
p=1/2
q=1-p 



@jit(nopython=True)  #'jit' runs the function in 'C' not in 'Python'
def evo(array): #this func evolves the grid untill the probability of being alive be less than 0.0001
    death_prob_tot=0
    death_prob=0
    T_bar=0
    t=0
    while 1:
        temp_array=np.zeros(len(array))
        for i in range(len(array)):
            if 1<i<len(array)-2:
                temp_array[i]=array[i-1]*q+array[i+1]*p
            elif i==0:
                temp_array[i]=array[i+1]*p
            elif i==len(array)-1:
                temp_array[i]=array[i-1]*q
            elif i==1:
                temp_array[i]=array[i+1]*p
            elif i==len(array)-2:
                temp_array[i]=array[i-1]*q
        t+=1
        death_prob=temp_array[0]+temp_array[len(array)-1]
        death_prob_tot+=death_prob
        array=np.copy(temp_array)
        T_bar+=(t)*(death_prob)
        if 1-death_prob_tot<0.0000001:
            return T_bar



T_bar_array=np.zeros(line-2)
for i in range(line-2):
    grid=np.zeros(line)
    grid[i+1]=1
    T_bar_array[i]=evo(grid)
    
plt.plot(T_bar_array)
print(np.average(T_bar_array))
plt.show()
            
        
        