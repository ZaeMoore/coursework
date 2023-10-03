"""
ODE Solver
Methods for Euler's method, 4th order Runge-kutta method, scipy's solution, and analytical solution
Returns the solutions to the main script
"""
import numpy as np
import scipy as sp
from scipy.integrate import odeint

k = 3.0 # k is a positive constant related to the type of material and size of the object


def func(t, y, temp_env):
    dydt = -k * (y - temp_env)
    return dydt


def euler(h, t_0, max_t, temp_0, temp_env):
    t = t_0
    t_list = [t_0]
    temp = temp_0
    temp_eu = [temp_0]
    while t <= max_t:
        new_temp = h * func(t, temp, temp_env)
        temp = temp + new_temp
        temp_eu.append(temp)
        t += h
        t_list.append(t)

    return temp_eu, t_list


def rungekutta(h, t_0, max_t, temp_0, temp_env):  # h is step size
    t = t_0
    temp = temp_0
    temp_rk = [temp_0]
    while t <= max_t:
        k1 = func(t, temp, temp_env)
        k2 = func(t + 0.5 * h, temp + 0.5 * k1 * h, temp_env)
        k3 = func(t + 0.5 * h, temp + 0.5 * k2 * h, temp_env)
        k4 = func(t + h, temp + k3 * h, temp_env)

        temp = temp + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        temp_rk.append(temp)
        t += h

    return temp_rk


def scipy_sol(h, max_t, y_0, temp_env):
    t_eval = np.arange(0, max_t, h)
    sci_sol = odeint(func, y_0, t_eval, args=(temp_env,), tfirst=True)
    return t_eval, sci_sol


def analytic_sol(h, y_0, max_t, temp_env):
    t = np.arange(0, max_t, h)
    c = temp_env - y_0
    solution = temp_env - c * np.exp(-k * t)

    return solution, t
