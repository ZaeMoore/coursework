"""
Main script for project 1
Need 2 other scripts that this one calls, one for the integral and one for the ODE
Each of these other 2 files will have multiple ways to solve
User should be alloed to decide what method is being used (including the options to use all) in this file,
and that is passed to the other 2
it should be straightforward to switch between different integration methods
Include a 'useage' readme file in your repository that details how to run the code.
"""
import integral_solver as integ
import ode_solver as ode

whatchadoin = input("Integral (Type 1) or ODE (Type 2)?: ")

#Integral
if whatchadoin == 1: 

    method = input("Choose a method of integration: riemann (type 1), trapezoidal (type 2), or simpsons (type 3): ")

    if method == 1:
        step_size = input("Choose the step size: ")
        integ.riemann(step_size)

    elif method == 2:
        step_size = input("Choose the step size: ")
        integ.trap(step_size)

    elif method == 3:
        step_size = input("Choose the step size: ")
        integ.simpson(step_size)

    else:
        print("Method is not a valid choice. Please try again.")

#ODE
elif whatchadoin == 2:

    method = input("Choose a method of ODE solving: euler (type 1) or runge-kutta (type 2): ")

    if method == 1:
        ode.euler(1)

    if method == 2:
        ode.rungekutta(1)
    
    else:
        print("Method is not a valid choice. Please try again")

else:
    print("Not a valid option. Please try again.")

