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
k = 5

def rho(r):
    return k*(r**3)

def riemann(step_size, radius, max_r):
    solution_out = []
    solution_in = []
    r_in = []
    r_out = []
    ro = radius
    ri = 0
    while r_out < max_r:
        new_out = step_size * rho(ro)
        solution_out.append(new_out)
        r_out.append(ro)
        ro += step_size
    while r_in < radius:
        new_in = step_size * rho(ri)
        solution_in.append(new_in)
        r_in.append(ri)
        ri += step_size
    return r_in, r_out, solution_in, solution_out

def trap(step_size, radius, max_r):
    solution_out = []
    solution_in = []
    r_in = []
    r_out = []
    ro = radius
    ri = 0
    while r_out < max_r:
        r_out.append(ro)
        solution_out.append(0.5 * step_size * (rho(ro) + rho(ro + step_size)))
        ro += step_size
    while r_in < radius:
        r_in.append(ri)
        solution_in.append(0.5 * step_size * (rho(ri) + rho(ri + step_size)))
        ri += step_size

    return r_in, r_out, solution_in, solution_out

def simpson(step_size, radius, max_r):
    solution_out = []
    solution_in = []
    r_in = []
    r_out = []
    ro = radius
    ri = 0
    while r_out < max_r:
        solution_out.append((1/6) * (max_r - ro) * (rho(ro) + rho(max_r) + 4 * rho(0.5 * (max_r - ro))))
        r_out.append(ro)
        ro += step_size
    while r_in < radius:    
        solution_in.append((1/6) * ri * (rho(0) + 4 * rho(0.5 * ri) + rho(ri)))
        r_in.append(ri)
        ri += step_size

    return r_in, r_out, solution_in, solution_out