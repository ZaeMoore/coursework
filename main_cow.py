#Main Program to Call Functions to Find the Cow

#User inputs variables and initial conditions
t = 0 #Time starts at 0
t_increment = float(input("Time increment (s) = ")) #User inputs time increment
x_i = float(input("Initial X Position (m) = "))
y_i = float(input("Initial Y Position (m) = "))
vx_i = float(input("Initial Velocity in X Direction (m/s) = "))
vy_i = float(input("Initial Velicty in Y Direction (m/s) = "))

def func1(x, y, v_x, v_y, k):
    Fg_y = -1000*9.8
    Fg_x = 0
    Fw_x = -k*((v_x)**2)
    Fw_y = -k*((v_y)**2)

    Ftot_x = Fg_x + Fw_x
    Ftot_y = Fg_y + Fw_y

    return Ftot_x, Ftot_y

def func2(x, y, v_x, v_y, Ftot_x, Ftot_y, t):
    xf = x + (v_x*t) + 0.5*Ftot_x*(t**2)/1000
    yf = y + (v_y*t) + 0.5*Ftot_y*(t**2)/1000

    v_xf = v_x + Ftot_x*t/1000
    v_yf = v_y + Ftot_y*t/1000

    return xf, yf, v_xf, v_yf