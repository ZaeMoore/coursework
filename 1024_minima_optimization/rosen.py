import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import rosen

x = np.arange(start = -1, stop = 3, step = 0.01)
y = np.arange(start = -1, stop = 3, step = 0.01)

X, Y = np.meshgrid(x, y)

z = rosen((X, Y))

x = -1
y = -1
i = 0
xList = [x]
yList = [y]
tau = 5*10**(-4)
while abs(rosen((x,y))) > 10**(-10):
    h = 10**(-7)
    xgrad = (rosen((x+(h/2),y))-rosen((x-(h/2),y)))/h
    ygrad = (rosen((x,y+(h/2)))-rosen((x,y-(h/2))))/h
    x = x-(xgrad*tau)
    y = y-(ygrad*tau)

    i = i+1
    xList.append(x)
    yList.append(y)
        
print("(X,Y) min values: ", x, y)
print("Number of points found: ", i)
print("Minimum z value: ", rosen((x,y)))

fig, axes = plt.subplots()
axes.plot(xList, yList, marker = 'o')
fig.set_size_inches(10,7)
plt.show()
