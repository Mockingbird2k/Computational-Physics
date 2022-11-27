
import numpy as np
import random
import matplotlib.pyplot as plt



delta_array=np.array([12,5.4,3.8,2.75,2,1.5,1.1,0.75,0.35])  #these 'delta's have the corresponding "acceptance-percentage" of 0.1,0.2,0.3,.....0.9



def gaussian(x):
    return (np.exp(-x*x))/(np.pi)**0.5

def metropolis(N,delta):  #does metropolis algorithm 'N' steps and returns an array which represents the probabilty of each point
    pos_rand=np.random.random(size=N)
    pos_rand-=1/2
    pos_rand*=2
    prob_rand=np.random.random(size=N)
    pos_array=np.zeros(N)
    current_pos=0
    movement_number=0  #represents the number of successful movements
    counter=0
    while counter<N:
        prob_rel=gaussian(current_pos+delta*pos_rand[counter])/gaussian(current_pos)
        if prob_rel>=1:
            current_pos=current_pos+delta*pos_rand[counter]
            pos_array[counter]=current_pos
            movement_number+=1
            counter+=1
            continue
        else:
            if prob_rand[counter]<prob_rel:
                current_pos=current_pos+delta*pos_rand[counter]
                pos_array[counter]=current_pos
                movement_number+=1
                counter+=1
                continue
            else:
                pos_array[counter]=current_pos
                counter+=1
                continue
                
    acceptance_percentage=movement_number/counter
    return pos_array,acceptance_percentage




def correlation(pos_array):
    sigma2=np.var(pos_array)
    j_number=4        #j_number  determines until which number we calculate correlation
    size=len(pos_array)
    average=np.average(pos_array)
    cor_array=np.zeros(j_number)
    for j in range(j_number):
        cor=0
        for i in range(size-j):
            cor=cor+pos_array[i]*pos_array[i+j]
        cor=cor/(size-j)
        cor_array[j]=cor
    correlation_length=-1/(best_slope(np.arange(j_number),np.log(cor_array)))
    return correlation_length




def best_slope(x_arr,y_arr):  #finds the best slope,passes through arrays 'x_arr' and 'y_arr'
    xbar=np.average(x_arr)
    ybar=np.average(y_arr)
    xybar=np.average(x_arr*y_arr)
    x2bar=np.average(x_arr**2)
    slope=(xbar*ybar-xybar)/(xbar**2-x2bar)
    return slope
    
    
N=10000
sample_number=100
correlation_length_array=np.zeros(len(delta_array))
correlation_length_array_tot=np.zeros(shape=(sample_number,len(delta_array)))
for j in range(sample_number):
    for i in range(len(delta_array)):
        delta=delta_array[i]
        pos_array,acceptance_percentage=metropolis(N,delta)
        correlation_length_array_tot[j,i]=correlation(pos_array)
        
for i in range(len(delta_array)):
    correlation_length_array[i]=np.average(correlation_length_array_tot[:,i])
    
    
print('corresponding correlation lengths are:')
print(correlation_length_array)    
#fig1, pic1=plt.subplots(1,figsize=(20,10))
#pic1.hist(pos_array,bins=np.arange(-5,5,.1))