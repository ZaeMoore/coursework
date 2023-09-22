"""
Main script for project 1
Need 2 other scripts that this one calls, one for the integral and one for the ODE
Each of these other 2 files will have multiple ways to solve
User should be alloed to decide what method is being used (including the options to use all) in this file,
and that is passed to the other 2
it should be straightforward to switch between different integration methods
Include a 'useage' readme file in your repository that details how to run the code.
"""
#https://docs.scipy.org/doc/scipy/ Look here for how to code these things
import matplotlib
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import solve_ivp
import numpy as np
import integral_solver as integ
import ode_solver as ode


whatchadoin = input("Integral (Type 1) or ODE (Type 2)?: ")

#Integral
if whatchadoin == 1: 
    k = 5 #Factor to be defined for funsies
    rad = 10 #radius of sphere in m

    def rho(r):
        return k*(r**3)

    step_size = input("Choose the step size: ")
    integ.riemann(step_size)
    
    integ.trap(step_size)

    integ.simpson(step_size)



#ODE
elif whatchadoin == 2:
    k = 3 #k is a positive constant related to the type of material and size of the object
    temp_env = 10 #Temperature of environment in Kelvin

    #y is temperature, t is time
    def func(t, y):
        return -k(y-temp_env)
    
    t_0 = 0 #Initial time
    y_0 = 40 #Initial temperature in Kelvin
    t_list = [t_0]
    y_rk = [y_0]
    y_eu = [y_0]

    step_size = input("Choose the step size: ")
    max_t = int(input("Maximum time value (s) = "))

    while t_rknew <= max_t:

        t_rknew, y_rknew = ode.euler(step_size, t_0, y_0, func)
        y_rk.append(y_rknew)

        t_eunew, y_eunew = ode.rungekutta(step_size, t_0, y_0, func)
        y_eu.append(y_eunew)

        t_list.append(t_rknew)

    t_eval, sci_sol = ode.scipy_sol(step_size, max_t, y_0, func)
    analytic_sol = ode.analytic_sol(step_size, y_0, temp_env, k, max_t)

    #Plot rk, eu, and scipy solutions
    plt.figure(1)
    plt.plot(t_list, y_eu, label = "Euler", color = "blue", linestyle = "dashed")
    plt.plot(t_list, y_rk, label = "Runge-Kutta", color = "green", linestyle = "dashed")
    plt.plot(t_eval, sci_sol, label = "Scipy solution", color = "red", linestyle = "dashed")
    plt.plot(t_eval, analytic_sol, label = "Exact solution", color = "purple")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (K)")
    plt.title("Solving Newton's Law of Cooling")

else:
    print("Not a valid option. Please try again.")

