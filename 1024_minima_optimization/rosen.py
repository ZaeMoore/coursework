import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import rosen


#Gradient method
#Start at each corner

vector = [-1, -1] #probably best one to start in
h = 0.0001
def gradient(x, y):

    grax = (rosen((x + h/2, y)) - rosen((x - h/2, y)))/h
    gray = (rosen((x, y + h/2)) - rosen((x, y - h/2)))/h

    return (grax, gray)

tolerance = 10**(-10)
tau = [10**(-8), 10**(-8)]
x = vector[0]
y = vector[1]
z = rosen((vector[0],vector[1]))
pointsx = [vector[0]]
pointsy = [vector[1]]
pointsz = [z]
while z >= tolerance:
    gradx, grady = gradient(x, y)

    diffx = -tau[0] * gradx
    diffy = -tau[1] * grady

    nextgradx, nextgrady = gradient(x + diffx, y + diffy)

    tau[0] = (diffx*nextgradx)/(nextgradx - gradx)
    tau[1] = (diffy*nextgrady)/(nextgrady - grady)
    
    x += diffx
    y += diffy
    z = rosen((x,y))
    
    pointsx.append(x)
    pointsy.append(y)
    pointsz.append(z)


print("X, Y = ", vector[0], vector[1])
print("Z minimum = ", z)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(pointsx, pointsy, pointsz)
plt.show()
