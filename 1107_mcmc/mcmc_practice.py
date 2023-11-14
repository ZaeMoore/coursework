import numpy as np
from statistics import NormalDist
import h5py
from matplotlib import pyplot as plt
from numpy.random import uniform
import tqdm
import math

f = h5py.File('./data.hdf', 'r')
xpos = np.array(f['data/xpos'][:])
ypos = np.array(f['data/ypos'][:])

def model(x, a, b, c):
    return a * x ** 2 + b * x + c

def post(x):
    return likelihood(x) * prior(x)

def prior(x):
    return 1

def proposal(x):
    return np.random.normal() + x

def likelihood(m):
    return np.prod(math.e ** (-0.5 * (ypos - m)))
    
def mcmc(initial, model, prop, post, iterations):
    a = [initial]
    b = [initial]
    c = [initial]
    m = [model(xpos, a[-1], b[-1], c[-1])] #x[-1] Pulls the last value in the list
    p = [post(m)]

    for i in tqdm.tqdm(range(iterations)):
        a_test = prop(a[-1])
        b_test = prop(b[-1])
        c_test = prop(c[-1])
        m_test = model(xpos, a_test, b_test, c_test)
        p_test = post(m_test)

        acc = p_test / p[-1] #Acceptance fraction
        u = np.random.uniform(0, 1)
        if u <= acc:
            a.append(a_test)
            b.append(b_test)
            c.append(c_test)
            m.append(m_test)
            p.append(p_test)
    return a, b, c, m, p
    
chaina, chainb, chainc, prob, cost = mcmc(10, model, proposal, post, 100000)

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