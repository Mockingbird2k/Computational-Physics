""""
Question 1 Code:
Considering a function named Katooreh() which return an array of x

x = Katooreh()
def correlation(x):
    sigma2=np.var(x)
    j_number= 1,2,3,....  # for each distance we can calculate j
    size=len(x)
    average=np.average(x)
    cor_array=np.zeros(j_number)
    for j in range(j_number):
        cor=0
        for i in range(size-j):
            cor=cor+x[i]*x[i+j]
        cor=cor/(size-j)
        cor_array[j]=cor
    correlation_length=-1/(best_slope(np.arange(j_number),np.log(cor_array)))
    return correlation_length

"""