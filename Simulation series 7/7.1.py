
import numpy as np
import matplotlib.pyplot as plt
import datetime
time=datetime.datetime.now()


point_number_array=np.array([100000])  #number of points in each calculation
sample_number=100, 500, 1000, 10000   #statistical number of averaging





'''
calculates the integral of e^(-x^2) with 'simple sampling' procedure in INTERVAL (a,b)
takes 'sample number' and point number as entrance and the result is a tuple of integration and its error
'''
def simple_intergral(point_number,sample_number):
    a=0
    b=2
    samples=np.zeros(shape=(sample_number,point_number))
    integral=np.zeros(sample_number)
    samples[:,:]=np.random.random(size=(sample_number,point_number))
    samples=(b-a)*samples
    samples=-samples*samples
    samples=np.exp(samples)
    for i in range(sample_number):
        integral[i]=(b-a)*np.average(samples[i,:])
    error=(np.var(integral))/(sample_number**0.5)
    integrated=np.average(integral)
    return (integrated,error)  


def intelligent_intergral(point_number,sample_number):
    g_int=0.8646647
    a=0
    b=2
    samples=np.zeros(shape=(sample_number,point_number))
    integral=np.zeros(sample_number)
    f_g=np.zeros(shape=(sample_number,point_number))  #this func should be get averaged instead of 'f'
    samples[:,:]=np.random.random(size=(sample_number,point_number))
    samples=(b-a)*samples
    samples=-np.log(1-g_int*samples/2)
    f_g=(np.exp((-samples)*samples)/np.exp(-samples))
    for i in range(sample_number):
        integral[i]=g_int*np.average(f_g[i,:])
    error=(np.var(integral))/(sample_number**0.5)
    integrated=np.average(integral)
    return (integrated,error)  
    



for i in range(len(sample_number)):
    intergral_array=np.zeros(shape=(len(point_number_array),sample_number[i]))
    integrated,error=simple_intergral(point_number_array[0],sample_number[i])
    print('For simple integral with ', sample_number[i], ' sample numbers')
    print(integrated,error)
    print(datetime.datetime.now()-time)

    print('For intelligent integral with ', sample_number[i], ' sample numbers')
    integrated,error=intelligent_intergral(point_number_array[0],sample_number[i])
    print(integrated,error)
    print(datetime.datetime.now()-time)
