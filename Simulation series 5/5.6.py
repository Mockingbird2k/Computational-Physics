
import numpy as np
import matplotlib.pyplot as plt
import random
import datetime

time=datetime.datetime.now()



u=1/4  #probability of jumping up
d=1/4  #probability of jumping down
l=1/4  #probability of jumping left
r=1/4  #probability of jumping right


L=200
N=2000
grid=np.zeros(shape=(L//3,L),dtype=int)
grid[0,:]=2




def evo(grid):
    max_h=2  #'max_h' is the highest part of cluster +1!
    for n in range(N):
        current_x=random.randint(0,L-1)
        current_y=max_h
        while True:
            if max_h==(len(grid[:,0])-2):# in this part we extend boundries so that cluster will NOT reach them
                grid=np.concatenate((grid,np.zeros(shape=(L,L))),axis=0)
                #return grid
            rand=np.random.random()
            if 0<rand<u:
                current_y+=1
            elif u<rand<(u+d):
                current_y-=1
            elif (u+d)<rand<(u+d+l):
                current_x=((current_x-1)%L)
            elif (u+d+l)<rand<1:
                current_x=((current_x+1)%L)
            #below we check if particle is connected to the cluster or not
            if (grid[current_y,(current_x+1)%L]==2 or grid[current_y,(current_x-1)%L]==2 or grid[current_y+1,current_x]==2 or grid[current_y-1,current_x]==2 ):
                grid[current_y,current_x]=2
                temp=np.copy(grid[current_y,:])
                if len(temp[(temp==2)])==1:
                    max_h+=1
                break
            if current_y>(max_h):
                current_x=random.randint(0,L-1)
                current_y=max_h
            if max_h==len(grid[:,0]):
                grid=np.concatenate((grid,np.zeros(shape=(L,L))),axis=0)
    return grid
                
                
         
grid=evo(grid)
plt.pcolor(grid, cmap='inferno')
            
plt.show()
