import numpy as np
import matplotlib
import math
matplotlib.use("agg")
import matplotlib.pyplot as plt

x_list = np.arange(0, 10, 0.01)

def qes(x):
    return 2*x*(math.e**(-(x**2)))

def pi(x):
    if x <= 0.25:
        return 0
    else:
        return 0.25*x*math.e**(-(x-0.75)**2)
    
def dis(x):
    if x <= 0.75:
        return 0
    else:
        return -math.e**(-x+0.5)+0.8

pi_list = []
dis_list = []
i = 0
while i < len(x_list):
    pi_list.append(pi(x_list[i]))
    dis_list.append(dis(x_list[i]))
    i+=1

    
plt.figure(1)
plt.plot(x_list, qes(x_list), label="Quasielastic Scattering", color="red", linestyle="dashed", linewidth=2)
plt.plot(x_list, pi_list, label="Pi Resonance Scattering", color="blue", linestyle="dashed", linewidth=2)
plt.plot(x_list, dis_list, label="Deep Inelastic Scattering", color="purple", linestyle="dashed", linewidth=2)
plt.xlabel("$E_v$ (GeV)")
plt.xscale("log")
plt.ylabel("$\sigma$/$E_v$ ($10^{-38}cm^2/GeV$)")
plt.legend()
plt.title("Neutrino-Nucleon cross section contributions")
plt.savefig("interactions.png")