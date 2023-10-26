import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import rosen


#Gradient method
#Start at each corner

start = [-1, -1]
delh = 0.0001
def gradient(vector):

    grax = (rosen((vector[0] + delh/2, vector[1])) - rosen((vector[0] - delh/2, vector[1])))/delh
    gray = (rosen((vector[0], vector[1] + delh/2)) - rosen((vector[0], vector[1] - delh/2)))/delh

    return (grax, gray)

i = 0
tolerance = 10**(-10)
N = 100
diff = [0,0]
pointsx = []
pointsy = []
pointsz = []
tau = [0.0001, 0.0001]
z = 0
while z >= tolerance:
    pointsx.append(start[0])
    pointsy.append(start[1])
    pointsz.append(rosen((start[0], start[1])))
    print("vector: ", start)

    gradx = gradient(start)[0]
    grady = gradient(start)[1]
    print("gradient: ", gradx, grady)


    diff[0] = -tau[0] * gradx
    diff[1] = -tau[1] * grady
    print("diff", diff)

    newstart = [start[0] + diff[0], start[1] + diff[1]]    

    tau[0] = (diff[0]*gradient(newstart)[0])/(gradient(newstart)[0] - gradx)
    tau[1] = (diff[1]*gradient(newstart)[1])/(gradient(newstart)[1] - grady)

    if (rosen((start[0], start[1])) <= tolerance):
            print(rosen((start[0], start[1])))
            print(start[0], start[1])
            break
    
    start[0] += diff[0]
    start[1] += diff[1]

    i+=1

x = np.arange(-1, 3, .01)
X, Y = np.meshgrid(x, x)

z = np.log(rosen((X, Y)))
plt.scatter(pointsx, pointsy)
#plt.pcolormesh(X, Y, z, vmin=1e-3)
#c = plt.colorbar()
plt.show()