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
    rad = 1 #radius of sphere in m
    max_r = 10

    step_size = float(input("Choose the step size: "))

    #These return the total charge Q at each r
    rr_in, rr_out, rQ_in, rQ_out = integ.riemann(step_size, rad, max_r)
    
    tr_in, tr_out, tQ_in, tQ_out = integ.trap(step_size, rad, max_r)

    sr_in, sr_out, sQ_in, sQ_out =integ.simpson(step_size, rad, max_r)

    #Now to define E for each of these using Gauss' Law
    #E = Q/r**2 
    rE_in, rE_out, tE_in, tE_out, sE_in, sE_out = [], [], [], [], [], []
    for i in range(len(rQ_in)):
        rE_in.append(rQ_in[i] / ((rr_in[i])**2))
    for i in range(len(rQ_out)):
        rE_out.append(rQ_out[i]/ ((rr_out[i])**2))
    for i in range(len(tQ_in)):
        tE_in.append(tQ_in[i] / ((tr_in[i])**2))
    for i in range(len(tQ_out)):
        tE_out.append(tQ_out[i]/ ((tr_out[i])**2))
    for i in range(len(sQ_in)):
        sE_in.append(sQ_in[i] / ((sr_in[i])**2))
    for i in range(len(sQ_out)):
        sE_out.append(sQ_out[i]/ ((sr_out[i])**2))

    plt.figure(2)
    plt.plot(rr_in, rE_in, label = "Riemann Sum inside Sphere", color = "blue", linestyle = "dashdot", linewidth = 2)
    plt.plot(rr_out, rE_out, label = "Riemann Sum outside Sphere", color = "cyan", linestyle = "dashdot", linewidth = 2)
    plt.plot(tr_in, tE_in, label = "Trapezoidal Sum inside Sphere", color = "purple", linestyle = "dashed", linewidth = 2)
    plt.plot(tr_out, tE_out, label = "Trapezoidal Sum outside Sphere", color = "magenta", linestyle = "dashed", linewidth = 2)
    plt.plot(sr_in, sE_in, label = "Simpson Sum inside Sphere", color = "red", linestyle = "dotted", linewidth = 2)
    plt.plot(sr_out, sE_out, label = "Simpson Sum outside Sphere", color = "orange", linestyle = "dotted", linewidth = 2)
    plt.xlabel("r (m)")
    plt.ylabel("E-field")
    plt.legend()
    plt.title("E-Field of a charged sphere")
    plt.savefig("integ")

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




