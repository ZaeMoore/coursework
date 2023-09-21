'''
ODE Solver
You must implement an ODE integrator/evolver by hand. You should implement both 
Euler's method and 4th order Runge-kutta (you do not need to derive the weights). 
You must also compare to one provided by the Scipy library. 
2 Options: Euler's method or 4th order Runge-kutta
Always do the scipy one and show comparison
Delete these comments later
'''
#Newton's law of Cooling?
#https://en.wikipedia.org/wiki/Newton%27s_law_of_cooling
#https://knowledge.carolina.com/discipline/physical-science/physics/newtons-law-of-cooling/

def euler(h, t, y, func):
    y += h * func(t, y)
    t += h
    return t, y

def rungekutta(h, t, y, func): #h is step size
    k1 = func(t, y)
    k2 = func(t + 0.5 * h, y + 0.5 * k1 * h)
    k3 = func(t + 0.5 * h, y + 0.5 * k2 * h)
    k4 = func(t + h, y + k3 * h)

    y += (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    t += h

    return t, y