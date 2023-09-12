#Main Program to Call Functions to Find the Cow
import matplotlib.pyplot as plt


#User inputs variables and initial conditions
t = 0 #Time starts at 0
t_increment = float(input("Time increment (s) = ")) #User inputs time increment
x_i = float(input("Initial X Position (m) = "))
y_i = float(input("Initial Y Position (m) = "))
vx_i = float(input("Initial Velocity in X Direction (m/s) = "))
vy_i = float(input("Initial Velicty in Y Direction (m/s) = "))
k = float(input("Wind resistance factor = "))

#A function that takes in the cow’s current position and velocity vector and returns the total force vector
def func1(v_x, v_y, k):
    Fg_y = -1000*9.8
    Fg_x = 0
    Fw_x = -k*((v_x)**2)
    Fw_y = -k*((v_y)**2)

    Ftot_x = Fg_x + Fw_x
    Ftot_y = Fg_y + Fw_y

    return Ftot_x, Ftot_y

#A function which takes the cow’s current position, velocity, and the acting force, and returns a new position and velocity some *small* time later
def func2(x, y, v_x, v_y, Ftot_x, Ftot_y, t):
    xf = x + (v_x*t) + 0.5*Ftot_x*(t**2)/1000
    yf = y + (v_y*t) + 0.5*Ftot_y*(t**2)/1000

    v_xf = v_x + Ftot_x*t/1000
    v_yf = v_y + Ftot_y*t/1000

    return xf, yf, v_xf, v_yf

def calculatePotential(height):
    potential= 1000*9.8*height
    return potential

def calculateKinetic(velocityx,velocityy):
    kinetic=.5*1000*((velocityx**2+velocityy**2)**.5)
    return kinetic

def calculateTotalenergy(height, velocityx, velocityy):
    total_energy=calculatePotential(height) + calculateKinetic(velocityx,velocityy)
    return total_energy

#Let's get this bread
xList = [x_i]
yList = [y_i]
vxList = [vx_i]
vyList = [vy_i]
tList = [0]
FxList = [0]
FyList = [0]
uList = [0]
kList = [0]
eList = [0]
vx = vx_i 
vy = vy_i
x = x_i
y = y_i
time = 0
while y > 0: #Loop over all time that cow is in the air
    #Find the forces
    forces = func1(vx, vy, k)
    Fx = forces[0]
    Fy = forces[1]
    FxList.append(Fx)
    FyList.append(Fy)

    #Find position, velocity
    values = func2(x, y, vx, vy, Fx, Fy, t_increment)
    x = values[0]
    y = values[1]
    vx = values[2]
    vy = values[3]
    xList.append(x)
    yList.append(y)
    vxList.append(vx)
    vyList.append(vy)

    #Energies
    uList.append(calculatePotential(y))
    kList.append(calculateKinetic(vx, vy))
    eList.append(calculateTotalenergy(y, vx, vy))

    time+= t_increment
    tList.append(time)

print(yList)

plt.scatter(tList,yList)
plt.title("Bread")
plt.xlabel("Time (s)")
plt.ylabel("Y (m)")
plt.savefig("mygraph.png")

