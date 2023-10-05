"""
* In-class work
    * try inverse CDF and rejection sampling with exponential function 
    * classic PI estimation
        * What about an ellipse? (or other function)
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy as sp
import scipy.integrate as integrate
matplotlib.use("agg")

k = 5 #Some constant

#pdf = ke^x from 0 to 1
#cdf = int(ke^x) from 0 to 1 = k(e - 1)
#normalized cdf = 1/((e-1))e^x
#inverse cdf: x = e^y/(e-1)
#ln(x) = y - ln(e-1)
#y = ln(x(e-1) + 1) = 

def pdf(x):
    return k * np.exp(x)

def invcdf(x):
    return np.log(1.718*x + 1) 
    
#inverse cdf
xrandom = np.random.uniform(0,1,100000)


#rejection
#max for uniform has to be greater than the function everywhere

i = 0
max_value = k*np.exp(1)
max_range = max_value + 0.1 * max_value
xrejection = []
while len(xrejection) < 100000:
    x_test = np.random.uniform(0,1)
    y_test = np.random.uniform(0, max_range)

    y_compare = pdf(x_test)

    if y_test < y_compare:
        xrejection.append(x_test)

plt.figure(1)
plt.hist(invcdf(xrandom), label="inverse cdf")
plt.hist(xrejection, label="rejection sampling")
plt.legend()
plt.savefig("randomhisto.png")