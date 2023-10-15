"""
Main script for project two, monte carlo simulation for phy 607
Authors: Zae Moore, Andrew Dowling
"""
import math
import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

print("Welcome to the interactive neutrino experience where we all suffer")
number_darts = int(input("Number of trials: "))
#Input: flavor of neutrino we're starting with, distance traveled before collision, initial energy/momentum, number of collisions