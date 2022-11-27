
import numpy as np
sample_number=100
N=10**7


def rhoz_integral(N): #N will be the number of samples in 'simple integrating'
                        #rho=(1/6)*(z +  3)
    samples=np.random.random(size=N)
    samples=samples-1/2
    samples*=2
    integrand=(np.pi)*(samples/4)*(samples+3)*(1-samples**2)
    integral=2*np.average(integrand)
    return integral




def M_integral(N): #N will be the number of samples in 'simple integrating'
                        #rho=(1/6)*(z +  3)
    samples=np.random.random(size=N)
    samples=samples-1/2
    samples*=2
    integrand=(np.pi)*(1/4)*(samples+3)*(1-samples**2)
    integral=2*np.average(integrand)
    return integral


result=np.zeros(sample_number)


for i in range(sample_number):
    result[i]=rhoz_integral(N)/M_integral(N)
    
    
integral=np.average(result)
print('position of center of mass respect to the center is:')
print(integral)