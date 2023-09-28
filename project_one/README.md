This is the first project for PHY-607 Computational Physics at SU
Created by Zae Moore

Packages required to run: scipy, numpy, matplotlib

This project is intended to be run from main_script.py
All required inputs will occur in the terminal when you run main_script.py
You will choose between solving the integral to find the electric field created by a charged sphere and solving the ode of Newton's law of cooling

For the integral:
You will input radius of the charged sphere (m), the maximum distance at which you wish to measure the electric field (m), and the desired step size for the integration methods. The main script will pass this to the integral_solver.py script, which will produce the solutions using the Riemann sum, trapezoidal rule, simpson's rule, scipy's trapzoidal solution, scipy's simpson's solution, and the analytical solution (which I solved by hand). The script will save 2 figures, one labeled integ.py which shows the electric field inside and outside of the charged sphere, and one labeled charge_integ.png which shows the total charge enclosed in the sphere as calculated by the different methods.

For the ODE:
You will input the initial temperature of the object (K), the temperature of the environment (K), the maximum time at which you wish to measure the temperature of the object (s), and the step size for the ode solving methods. The main script will pass this to the ode_solver.py script, which will produce solutions using the euler method, 4th order runge-kutta method, scipy's ode solver, and the analytical solution (which I solved by hand). The script will save 1 figure labeled ODE.png, which shows the temperature of the object over time as solved by each method.