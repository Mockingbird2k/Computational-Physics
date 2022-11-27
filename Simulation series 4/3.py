

import numpy as np
import matplotlib.pyplot as plt
import random
import datetime
time=datetime.datetime.now()
L_array=np.array([201,301,1001])
probability=.58
probability_array=np.array([0.50,0.55,0.58])
S=1 #area of cluster


n=10   #number of ensembles in each seri(probability)

ensemble_result=np.zeros(shape=(len(probability_array),2,n)) #first index for seri of probability,second for 'Rg' or 'S' in order,and third for n(th) ensemble.FOR EXAMPLE:ensemble_result[0,1,,4]='S' of 5th ensemble for probability 0.5
ensemble_result_average=np.zeros(shape=(len(probability_array),2))  #averages of ensemble_result
ensemble_result_errors=np.zeros(shape=(len(probability_array),2)) #errors of ensemble_result
ensemble_log_result_average=np.zeros(shape=(len(probability_array),2))#averages of logarithm of ensemble_result
ensemble_log_result_errors=np.zeros(shape=(len(probability_array),2)) #errors of logarithm of ensemble_result



def x_cm_finder(plane):#finds the x coordinate of center of mass of cluster
    i=0
    x_cm=0
    while i<L:
        j=0
        while j<L:
            if plane[i,j]==1:
                x_cm=x_cm+j
            j+=1
        i+=1
    x_cm=x_cm/S
    return x_cm


def y_cm_finder(plane):#finds the y coordinate of center of mass of cluster
    i=0
    y_cm=0
    while i<L:
        j=0
        while j<L:
            if plane[i,j]==1:
                y_cm=y_cm+i
            j+=1
        i+=1
    y_cm=y_cm/S
    return y_cm


def x_var_finder(plane,x_cm):#finds the x variance of system around the x_cm 
    i=0
    x_var=0
    while i<L:
        j=0
        while j<L:
            if plane[i,j]==1:
                x_var=x_var+j**2
            j+=1
        i+=1
    x_var=x_var/S
    x_var=x_var-x_cm**2
    return x_var


def y_var_finder(plane,y_cm):#finds the y variance of system around the y_cm 
    i=0
    y_var=0
    while i<L:
        j=0
        while j<L:
            if plane[i,j]==1:
                y_var=y_var+i**2
            j+=1
        i+=1
    y_var=y_var/S
    y_var=y_var-y_cm**2
    return y_var
    
    

def growth(plane): #this function every time,make the cluster bigger just one step
    i=0             #in this func -1 means off,0 means not determined yet,1 means on and finally 2 means on but the cell is on boundries and its neighbours should be checked
    global S
    temp=np.zeros(shape=(L,L))
    temp=plane.copy()
    while i<L:
        j=0
        while j<L:
            if plane[i,j]==2:
                if temp[i-1,j]==0:
                    rand=random.random()
                    if rand<=probability:
                        temp[i-1,j]=2
                        S+=1
                    else:
                        temp[i-1,j]=-1
                if temp[i,j-1]==0:
                    rand=random.random()
                    if rand<=probability:
                        temp[i,j-1]=2
                        S+=1
                    else:
                        temp[i,j-1]=-1
                if temp[i,(j+1)%L]==0:
                    rand=random.random()
                    if rand<=probability:
                        temp[i,(j+1)%L]=2
                        S+=1
                    else:
                        temp[i,(j+1)%L]=-1
                if temp[(i+1)%L,j]==0:
                    rand=random.random()
                    if rand<=probability:
                        temp[(i+1)%L,j]=2
                        S+=1
                    else:
                        temp[(i+1)%L,j]=-1
                temp[i,j]=1
            j+=1
        i+=1
    plane=temp.copy()
    return plane
                
                    

def evo(plane):
    global S
    i=0
    while 1:
        initial_S=S
        plane=growth(plane)
        i+=1
        if initial_S==S:
            k=0
            while k<L: #in this part cells with value of 2,are turned into 1 because we have no more evolution
                j=0
                while j<L:
                    if plane[k,j]==2:
                        plane[k,j]=1
                    j+=1
                k+=1
            return plane
                    
                    



i=0
while i<len(probability_array):
    probability=probability_array[i]
    L=L_array[i]
    j=0
    while j<n:
        plane=np.zeros(shape=(L,L),dtype=np.int8)
        plane[L//2,L//2]=2
        plane=evo(plane)
        
        x_cm=x_cm_finder(plane)
        y_cm=y_cm_finder(plane)
        x_var=x_var_finder(plane,x_cm)
        y_var=y_var_finder(plane,y_cm)
        Rg=(x_var+y_var)**.5
        ensemble_result[i,0,j]=Rg
        ensemble_result[i,1,j]=S
        
        S=1
        j+=1
    i+=1

   
i=0
while i<len(probability_array):
    j=0
    while j<2:
        ensemble_result_average[i,j]=np.average(ensemble_result[i,j,:])
        ensemble_result_errors[i,j]=((np.var(ensemble_result[i,j,:]))/(n-1))**.5
        ensemble_log_result_average[i,j]=np.log(np.average(ensemble_result[i,j,:]))
        ensemble_log_result_errors[i,j]=((np.log(np.var(ensemble_result[i,j,:])))/(n-1))**.5
        j+=1
    i+=1
       



fig, (pic1,pic2)=plt.subplots(2,figsize=(20,30))
pic1.errorbar(ensemble_log_result_average[:,1],ensemble_log_result_average[:,0],yerr=ensemble_log_result_errors[:,0],xerr=ensemble_log_result_errors[:,1],fmt='o')
pic2.errorbar(probability_array,ensemble_result_average[:,0],yerr=ensemble_result_errors[:,0],fmt='o')

print(datetime.datetime.now()-time) 
        
plt.show()
