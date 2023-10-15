import math
import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

number_darts = int(input("Total number of darts: "))
darts_thrown = 0
in_ellipse = 0
a = 10
b = 5
delta = 0.0001
dela = a + delta
delb = b + delta

x = np.random.uniform(0, delb, size=number_darts)
y = np.random.uniform(0, dela, size=number_darts)

truth_out = (x*x)/(delb*delb) + (y*y)/(dela*dela) <= 1
truth_in = (x*x)/(b*b) + (y*y)/(a*a) <= 1

yes_out = truth_out.sum()
yes_in = truth_in.sum()
  
area_out = (yes_out * 4 * dela * delb)/number_darts
area_in = (yes_in * 4 * a * b)/number_darts

#should be bigger than 30, smaller than 60
circ = (area_out - area_in)/delta
print("Circumference: " + str(circ))