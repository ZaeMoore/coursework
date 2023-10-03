"""
Integral Solver
Methods for Riemann sum, trapezoidal rule, simpson's rule, scipy's trapzoidal solution, scipy's simpson's solution, and analytical solution
Returns the solutions to the main script
Solving for the enclosed charge of a sphere with a charge density of rho(r) = kr
"""
import scipy.integrate as integrate
import numpy as np

# K is just a constant that can be assigned to any numerical value
k = 5


# The equation to integrate over is rho(r) * r**3 * dr because we are integrating in spherical coordinates
def rho(r):
    return k * (r**3)


def riemann(step_size, radius, max_r):
    solution_out = []
    solution_in = []
    r_in = []
    r_out = []
    ro = radius
    ri = step_size  # Can't start r at 0, otherise get a divide by 0 error
    total_sum = 0
    while ri < radius:
        new_in = (
            4 * np.pi * step_size * rho(ri)
        )  # 4pi is from the theta and phi portion
        total_sum += new_in
        solution_in.append(total_sum)
        r_in.append(ri)
        ri += step_size
    while (
        ro < max_r
    ): 
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
        new_in = 4 * np.pi * 0.5 * step_size * (rho(ri) + rho(ri + step_size))
        total_sum += new_in
        solution_in.append(total_sum)
        ri += step_size
    while ro < max_r:
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
        new_in = (4 * np.pi * (step_size / 6) * (rho(ri) + 4 * rho(0.5 * (ri + ri + step_size)) + rho(ri + step_size)))
        total_sum += new_in
        solution_in.append(total_sum)
        r_in.append(ri)
        ri += step_size
    while ro < max_r:
        solution_out.append(total_sum)
        r_out.append(ro)
        ro += step_size

    return r_in, r_out, solution_in, solution_out, total_sum


def scipy_trap(step_size, radius):
    n = round(radius / step_size)
    r = np.linspace(0, radius, num=n)
    sci_trap = 4 * np.pi * integrate.trapz(rho(r), r)
    return sci_trap


def scipy_simp(step_size, radius):
    n = round(radius / step_size)
    r = np.linspace(0, radius, num=n)
    sci_simp = 4 * np.pi * integrate.simpson(rho(r), r)
    return sci_simp


def analytical(step_size, radius, max_r):
    total_Q = np.pi * k * (radius**4)
    r_in = np.arange(step_size, radius, step_size)
    r_out = np.arange(radius, max_r, step_size)
    e_in = k * np.pi * (r_in**2)
    e_out = total_Q * (1 / r_out**2)
    return r_in, r_out, e_in, e_out, total_Q
