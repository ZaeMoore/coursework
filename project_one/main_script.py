"""
Main script for project 1
Need 2 other scripts that this one calls, one for the integral and one for the ODE
Each of these other 2 files will have multiple ways to solve
User should be allowed to decide what method is being used (including the options to use all) in this file,
and that is passed to the other 2
it should be straightforward to switch between different integration methods
Include a 'useage' readme file in your repository that details how to run the code.
"""
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import solve_ivp
import numpy as np
import integral_solver as integ
import ode_solver as ode


whatchadoin = input("Integral (Type 1) or ODE (Type 2)?: ")

#Integral
if whatchadoin == "1": 
     #Factor to be defined for funsies
    rad = 10 #radius of sphere in m
    max_r = 100

    step_size = float(input("Choose the step size: "))

    rr_in, rr_out, rsol_in, rsol_out = integ.riemann(step_size, rad, max_r)
    
    tr_in, tr_out, tsol_in, tsol_out = integ.trap(step_size, rad, max_r)

    simp_out, simp_in =integ.simpson(step_size, rad, max_r)

    plt.figure(2)
    plt.plot(rr_in, rsol_in, label = "Riemann Sum inside Sphere", color = "blue", linestyle = "dashed", linewidth = 3)
    plt.plot(rr_out, rsol_out, label = "Riemann Sum outside Sphere", color = "blue", linestyle = "dashed", linewidth = 3)
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (K)")
    plt.legend()
    plt.title("Solving Newton's Law of Cooling")
    plt.savefig("ODE")

#ODE
elif whatchadoin == "2":

    t_0 = 0 #Initial time
    temp_0 = 40 #Initial temperature in Kelvin
    time = t_0

    step_size = float(input("Choose the step size: "))
    max_t = int(input("Maximum time value (s) = "))

    temp_eu, t_list = ode.euler(step_size, t_0, max_t, temp_0)
    temp_rk = ode.rungekutta(step_size, t_0, max_t, temp_0)

    t_list_sci, sci_sol = ode.scipy_sol(step_size, max_t, temp_0)
    analytic_sol, analytic_time = ode.analytic_sol(step_size, temp_0, max_t)

    #Plot rk, eu, and scipy solutions
    plt.figure(1)
    plt.plot(t_list, temp_eu, label = "Euler", color = "blue", linestyle = "dashed", linewidth = 3)
    plt.plot(t_list, temp_rk, label = "Runge-Kutta", color = "purple", linestyle = "dashed", linewidth = 3)
    plt.plot(t_list_sci, sci_sol, label = "Scipy solution", color = "red", linestyle = "dashed")
    plt.plot(analytic_time, analytic_sol, label = "Exact solution", color = "green")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (K)")
    plt.legend()
    plt.title("Solving Newton's Law of Cooling")
    plt.savefig("ODE")

else:
    print("Not a valid option. Please try again.")




