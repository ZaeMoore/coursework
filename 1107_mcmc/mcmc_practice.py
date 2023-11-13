import numpy as np
from statistics import NormalDist
import h5py
from matplotlib import pyplot as plt
from numpy.random import uniform
import tqdm

f = h5py.File('./data.hdf', 'r')
xpos = np.array(f['data/xpos'][:])
ypos = np.array(f['data/ypos'][:])

def post(x, a, b, c):
    return a * x ** 2 + b * x + c

def proposal(x):
    return np.random.normal() + x
    
#Need to do this for a, b, and c to find the best values for these?
def mcmc(initial, post, prop, iterations):
    a = [initial]
    b = [initial]
    c = [initial]
    p = [post(xpos, a[-1], b[-1], c[-1])] #x[-1] Pulls the last value in the list
    cost_func = [np.sum((ypos - p)**2)]

    for i in tqdm.tqdm(range(iterations)):
        a_test = prop(a[-1])
        b_test = prop(b[-1])
        c_test = prop(c[-1])
        #Minimize the cost function
        p_test = post(xpos, a_test, b_test, c_test)
        cost_func_test = np.sum((ypos - p_test)**2)

        acc = cost_func_test/ cost_func[-1] #Acceptance fraction
        u = np.random.uniform(0, 1)
        if u <= acc:
            a.append(a_test)
            b.append(b_test)
            c.append(c_test)
            p.append(p_test)
            cost_func.append(cost_func_test)
    return a, b, c, p, cost_func
    
chaina, chainb, chainc, prob, cost = mcmc(10, post, proposal, 100000)

plt.figure()
plt.title("Evolution of the walker for Ax^2 + BX + C")
plt.plot(chaina, label="Param A", color="orange")
plt.plot(chainb, label="Param B", color="green")
plt.plot(chainc, label="Param C", color="blue")
plt.legend()
plt.ylabel('Param Values')
plt.xlabel('Iteration')

plt.figure() 
plt.title("Evolution of the walker for Ax^2 + BX + C")
plt.plot(chaina, label="Param A", color="orange")
plt.plot(chainb, label="Param B", color="green")
plt.plot(chainc, label="Param C", color="blue")
plt.xlim(0, 100)
plt.ylabel('a-value')
plt.xlabel('Iteration')

plt.figure()
plt.title("Posterior samples")
_ = plt.hist(chaina[100::100], bins=100)

plt.show()