import h5py
from matplotlib import pyplot as plt
import numpy as np

f = h5py.File('./data.hdf', 'r')

def func(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

tau = 10**(-4)

xpos = f['data/xpos'][:]
ypos = f['data/ypos'][:]

rsqchange = 1
a = 1
b = 1
c = 1
d = 0
h = (10**-4)

rsq = sum((ypos - func(xpos, a, b, c, d))**2)

while rsqchange > 0.01:

    aderiv = (func(xpos, a+h/2, b, c, d) - func(xpos, a-h/2, b, c, d))/h
    bderiv = (func(xpos, a, b+h/2, c, d) - func(xpos, a, b-h/2, c, d))/h
    cderiv = (func(xpos, a, b, c+h/2, d) - func(xpos, a, b, c-h/2, d))/h
    dderiv = (func(xpos, a, b, c, d+h/2) - func(xpos, a, b, c, d-h/2))/h
    
    a -= tau*aderiv
    b -= tau*bderiv
    c -= tau*cderiv
    d -= tau*dderiv

    rsqnew = sum((ypos - func(xpos, a, b, c, d))**2)
    rsqchange = abs(rsq - rsqnew)
    rsq = rsqnew

ymean = np.mean(ypos)
rsqdenom = sum((ypos - ymean)**2)

rsquared = rsq/rsqdenom

print(rsquared)
print(rsqchange)