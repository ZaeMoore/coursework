"""
Main script for project two, monte carlo simulation for phy 607
Authors: Zae Moore, Andrew Dowling
"""
import math
import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import final_state as fs

print("Welcome to the interactive neutrino experience where we all suffer")
number_trials = int(input("Number of trials: "))
#Input: flavor of neutrino we're starting with, distance traveled before collision, initial energy/momentum, number of collisions

dist = int(input("Distance from start to detector (m): "))
lepton_number = int(input("Neutrino (Type 1) or Antineutrino (Type -1)? "))
flavor = input("Neutrino flavor? Type electron or muon: ")
if flavor == "electron":
    flavor_i = True
if flavor == "muon":
    flavor_i = False
else:
    flavor_i = True
    "Invalid input, assuming electron neutrinos"

e_initial = int(input("Initial energy of neutrinos (MeV): "))

final_particle_names = []
final_particle_mass = []
final_particle_energy = []
final_particle_charge = []
interaction_type = []

i = 0
#Each element in these arrays is its own array that represents one event
while i<number_trials:
    event = fs.FinalState(e_initial, flavor_i, lepton_number, dist)
    final = event.final_particles()
    final_particle_names.append(final[0])
    final_particle_mass.append(final[1])
    final_particle_energy.append(final[2])
    final_particle_charge.append(final[3])
    interaction_type.append(final[4])

    i+=1



#Output a .csv file with info
#Output a plot with positions of hits