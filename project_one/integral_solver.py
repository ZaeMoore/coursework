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

#rho(r) is the charge density
#For this solid sphere, the charge is evenly distributed throughout the sphere
#K represents any constant
#To find Q, we must do a spherical integral over rho which simplifies to Q = 4 pi * integ rho(r) * r^2 dr

def rho(r):
    return k*(r**2)

def riemann(step_size, radius, max_r):
    solution_out = []
    solution_in = []
    r_in = []
    r_out = []
    ro = radius
    ri = step_size #Can't start r at 0, otherise get a divide by 0 error
    total_sum = 0
    while ri < radius:
        new_in = step_size * rho(ri)
        total_sum += new_in
        solution_in.append(total_sum)
        r_in.append(ri)
        ri += step_size
    while ro < max_r: #Outside of the sphere, the total charge is constant
        solution_out.append(total_sum)
        r_out.append(ro)
        ro += step_size
    return r_in, r_out, solution_in, solution_out

def trap(step_size, radius, max_r):
    solution_out = []
    solution_in = []
    r_in = []
    r_out = []
    ro = radius
    ri = step_size
    total_sum = 0
    while ri < radius:
        r_in.append(ri)
        new_in = 0.5 * step_size * (rho(ri) + rho(ri + step_size))
        total_sum += new_in
        solution_in.append(total_sum)
        ri += step_size
    while ro < max_r: #Outside of the sphere, the total charge is constant
        r_out.append(ro)
        solution_out.append(total_sum)
        ro += step_size

    return r_in, r_out, solution_in, solution_out

def simpson(step_size, radius, max_r):
    solution_out = []
    solution_in = []
    r_in = []
    r_out = []
    ro = radius
    ri = step_size
    total_sum = 0
    while ri < radius:
        new_in = (step_size/6) * (rho(ri) + 4 * rho(0.5 * (ri + ri + step_size)) + rho(ri + step_size))
        total_sum += new_in
        solution_in.append(total_sum)
        r_in.append(ri)
        ri += step_size
    while ro < max_r: #Outside the sphere, the total charge is constant
        solution_out.append(total_sum)
        r_out.append(ro)
        ro += step_size

    return r_in, r_out, solution_in, solution_out