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
import csv

print("Welcome to the interactive neutrino experience where we all suffer")

number_trials = int(input("Number of trials: "))

dist = int(input("Distance from start to detector (m): "))
lepton_number = int(input("Neutrino (Type 1) or Antineutrino (Type -1)? "))
if lepton_number == 1:
    print("Neutrino")
if lepton_number == -1:
    print("Antineutrino")
if lepton_number != 1 and lepton_number != -1:
    lepton_number = 1
    print("Invalid input, assuming neutrinos")

flavor = int(input("Initial flavor of Neutrino (Type 1 for electron, Type 2 for muon): "))
if flavor == 1:
    print("Electron Neutrino")
    initial_f = "Electron"
    flavor_i = True
elif flavor == 2:
    print("Muon Neutrino")
    initial_f = "Muon"
    flavor_i = False
elif flavor != 1 and flavor != 2:
    print("Invalid input, assuming electron neutrinos")
    flavor_i = True

e_initial = int(input("Average energy of neutrino beam (between 10 and 10,000 MeV): "))

final_particle_names = []
final_particle_mass = []
final_particle_energy = []
final_particle_charge = []
interaction_type = []
data = [["Trial", "Initial Flavor", "Final Flavor", "Type of Interaction", "Final State Particles", "Energy of neutrino (MeV)"]]
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
    flavor = final[5]
    if flavor == True:
        final_f = "Electron"
    if flavor == False:
        final_f = "Muon"
    data.append([i+1, initial_f, final_f, final[4], final[0], final[6]])
    i+=1


with open("neutrinodata.csv", 'w', newline='') as file:
    wr = csv.writer(file)
    wr.writerows(data)

#Output a .csv file with info
#Output a plot with positions of hits

