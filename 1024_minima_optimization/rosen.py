import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import rosen

x = np.arange(-1, 3, .01)
X, Y = np.meshgrid(x, x)

z = np.log(rosen((X, Y)))
plt.pcolormesh(X, Y, z, vmin=1e-3)
c = plt.colorbar()
plt.show()

#Brute force method
zz = rosen((X,Y))
z_val = np.ndarray.flatten(zz)

minimum = np.min(z_val)
print(minimum)

h = 0.005
max = 1
min = -1 + h
x_val = min
y_val = min
while x_val <= 1:
    while y_val <= 1:
        prevzros = rosen((x_val-h, y_val-h))
        zros = rosen((x_val, y_val))
        nextzros = rosen((x_val+h, y_val+h))
        if zros<prevzros and zros<nextzros:
            print("min: ", x_val, y_val, zros)
        y_val += h
    x_val += h


#Gradient method
