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
#integ.riemann(step_size, rho, k, rad, r)
def riemann(step_size, rho, radius, r, max_r):
    solution_out = 0
    r_out = radius
    while r_out < max_r:
        solution_out += step_size * rho(r_out)
        r_out += step_size
    solution_in = step_size * rho(r)
    return solution_out, solution_in

def trap(step_size, rho, radius, r, max_r):
    #Area of trap: 0.5*h*(base1 + base2)
    solution_out = 0
    r_out = radius
    while r_out < max_r:
        r_new = r_out + step_size
        solution_out += 0.5 * step_size * (rho(r_out) + rho(r_new))
        r_out += step_size
    solution_in = 0.5 * step_size * (rho(r) + rho(r + step_size))
    return solution_out, solution_in

def simpson(step_size, rho, radius, r, max_r):
    solution_out = (1/6) * (max_r - radius) * (rho(radius) + rho(max_r) + 4 * rho(0.5 * (max_r - radius)))
    solution_in = (1/6) * r * (rho(0) + 4 * rho(0.5 * r) + rho(r))
    return solution_out, solution_in