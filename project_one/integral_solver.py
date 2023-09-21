'''
Integral Solver
you must implement an integrator using the simple riemann sum, the trapezoidal rule, 
and simpson's rule. In the case of the trapezoidal and simpson's rule, compare to 
the similar implementations in Scipy. 
3 options: Riemann, trapezoidal, simpson's
if t or s, compare to scipy's implementations
Delete these comments later
'''
#rho(r) = kr**3
#Find Q using integral solver
#Set R = 10
#For inside sphere, Q is integrated from 0 to r
#For outside sphere, Q is integrated from 0 to 10
#E = Q/(r**2) 
#Check that E_in = E_out at r = 10
#Check that E_out goes to 0 at r=inf
k = 5 #Factor to be defined for funsies
rad = 10 #radius of sphere in m

def rho(r):
    return k*(r**3)

def riemann(step_size):
    step_size

def trap(x):
    x

def simpson(x):
    x

