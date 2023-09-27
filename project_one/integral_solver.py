'''
Integral Solver
you must implement an integrator using the simple riemann sum, the trapezoidal rule, 
and simpson's rule. In the case of the trapezoidal and simpson's rule, compare to 
the similar implementations in Scipy. 
'''
import scipy.integrate as integrate
import numpy as np
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
    return r_in, r_out, solution_in, solution_out, total_sum

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

    return r_in, r_out, solution_in, solution_out, total_sum

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

    return r_in, r_out, solution_in, solution_out, total_sum

def scipy_trap(step_size, radius):
    r = np.arange(0, radius, step_size)
    sci_trap = integrate.trapezoid(rho(r))
    return sci_trap

def scipy_simp(step_size, radius):
    r = np.arange(0, radius, step_size)
    sci_simp = integrate.simpson(rho(r))
    return sci_simp

def analytical(step_size, radius, max_r):
    total_Q = k/3
    r_in = np.arange(step_size, radius, step_size)
    r_out = np.arange(radius, max_r, step_size)
    e_in = k/3 * r_in
    e_out = k/3 * (1/r_out**2)
    return r_in, r_out, e_in, e_out, total_Q