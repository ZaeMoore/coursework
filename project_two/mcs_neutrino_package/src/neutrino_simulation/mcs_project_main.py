"""
Main script for project two, monte carlo simulation for phy 607

This package simulates the interaction of neutrinos and liquid Argon atoms, and the resulting
final state particles.

"""
import math
import numpy as np
import matplotlib

matplotlib.use("agg")
import matplotlib.pyplot as plt
import neutrino_simulation.final_state as fs
from neutrino_simulation.trajectory import F, findClosest, FinalHit
import csv

print(
    "Welcome to the interactive neutrino simulation experience, where a neutrino's best quality is its wiggles!"
)
print(
    "Here, we will conduct a number of simulations to learn about how neutrinos interact with Argon atoms!"
)

number_trials = int(input("Number of trials/runs: "))

dist = int(input("Distance from the start of the neutrino beam to the detector (m): "))
lepton_number = int(input("Neutrino (Type 1) or Antineutrino (Type -1)? "))
if lepton_number == 1:
    print("Neutrino")
if lepton_number == -1:
    print("Antineutrino")
if lepton_number != 1 and lepton_number != -1:
    lepton_number = 1
    print("Invalid input, assuming neutrinos")

flavor = int(
    input("Initial flavor of Neutrino (Type 1 for electron, Type 2 for muon): ")
)
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

beam_energy = int(
    input("Average energy of neutrino beam (between 10 and 10,000 MeV): ")
)

oscillated = 0
qes_data = 0
pi_data = 0
dis_data = 0
final_particle_names = []
final_particle_mass = []
final_particle_energy = []
final_particle_charge = []
interaction_type = []
data = [
    [
        "Trial",
        "Initial Flavor",
        "Final Flavor",
        "Type of Interaction",
        "Final State Particles",
        "Energy of neutrino (MeV)",
    ]
]
i = 0
# Each element in these arrays is its own array that represents one event
while i < number_trials:
    event = fs.FinalState(beam_energy, flavor_i, lepton_number, dist)
    final = event.final_particles()
    final_particle_names.append(final[0])
    final_particle_mass.append(final[1])
    final_particle_energy.append(final[2])
    final_particle_charge.append(final[3])
    interaction_type.append(final[4])
    if final[4] == "QES":
        qes_data += 1
    if final[4] == "DIS":
        dis_data += 1
    if final[4] == "pi":
        pi_data += 1
    flavor = final[5]
    if flavor_i != flavor:
        oscillated += 1
    if flavor == True:
        final_f = "Electron"
    if flavor == False:
        final_f = "Muon"
    data.append([i + 1, initial_f, final_f, final[4], final[0], final[6]])
    i += 1

percent_oscillated = 100 * oscillated / number_trials
percent_qes = 100 * qes_data / number_trials
percent_pi = 100 * pi_data / number_trials
percent_dis = 100 * dis_data / number_trials
print("Percent of neutrinos that oscillated: ", percent_oscillated)
print("Percent of interactions that were qes: ", percent_qes)
print("Percent of interactions that were pi resonance: ", percent_pi)
print("Percent of interactions that were dis: ", percent_dis)

with open("neutrinodata.csv", "w", newline="") as file:
    wr = csv.writer(file)
    wr.writerows(data)

    
#print(final_particle_mass)
#print(final_particle_energy)
#print(final_particle_charge)

#Zae pls help, too many empty lists

particleMass = [item for sublist in final_particle_mass for item in sublist]
particleE = [item for sublist in final_particle_energy for item in sublist]
particleCharge = [item for sublist in final_particle_charge for item in sublist]



#print(len(particleMass), len(particleE), len(particleCharge))

initialE_filt = []
mass_filt = []
charge_filt = []

# 0 charge particles won't generate current in silicon sensors

for i in range(len(particleMass)): #filter out 0 charge particles
    if particleCharge[i] == 1 or particleCharge[i] == -1:
        initialE_filt.append(particleE[i])
        mass_filt.append(particleMass[i])
        charge_filt.append(particleCharge[i])

        
        
print(mass_filt, initialE_filt, charge_filt)

detection = FinalHit(
    initialE_filt,
    mass_filt,
    charge_filt,
    100,
    1,
    5,
    0.1
    )

xVel, yVel, zVel = detection.vComponents
xHit, yHit, zHit, Efin = detection.WhereHit(xVel, yVel, zVel, 10, -10)

fig, ax1 = plt.subplots()
fig, ax2 = plt.subplots()

for i in range(len(xHit)):
    if xHit[i] > 0:
        ax1.plot(yHit[i], zHit[i], color = 'blue')
    if xHit[i] < 0:
        ax2.plot(yHit[i], zHit[i], color = 'red')

plt.show()
        


# Output a plot with positions of hits
