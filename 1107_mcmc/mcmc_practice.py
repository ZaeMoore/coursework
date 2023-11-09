import numpy as np
from statistics import NormalDist
import h5py
from matplotlib import pyplot as plt
from numpy.random import uniform
import tqdm


#Goal is that the position of the walker will be a random drawing from the posterior prob distribution function
#Prior can be anything, can have it as 1 here

def post(x, a, b, c):
    #Proportional to the posterior probability, Also known as target probability
    return a * x ** 2 + b * x + c

def proposal(x):
    #Proposal distribution g(x1 | g0)
    return np.random.normal() + x
    
def mcmc(initial, post, prop, iterations):
    x = [initial]
    p = [post(x[-1])]
    for i in tqdm.tqdm(range(iterations)):
        x_test = prop(x[-1])
        p_test = post(x_test)

        acc = p_test / p[-1] #Acceptance fraction
        u = np.random.uniform(0, 1)
        if u <= acc:
            x.append(x_test)
            p.append(p_test)
    return x, p
    
chain, prob = mcmc(10, post, proposal, 1000000)

plt.figure()
plt.title("Evolution of the walker")
plt.plot(chain)
plt.ylabel('x-value')
plt.xlabel('Iteration')

plt.figure()
plt.title("Evolution of the walker")
plt.plot(chain)
plt.xlim(0, 100)
plt.ylabel('x-value')
plt.xlabel('Iteration')

plt.figure()
plt.title("Posterior samples")
_ = plt.hist(chain[100::100], bins=100)

plt.show()