"""
Monte Carlo simulation for neutrino flavor and final state
Returns stuff to main script
"""
import math
import numpy as np
from statistics import NormalDist

class FinalState():
    def __init__(self, e_i, flavor_i, lepton_number, dist):
        """Initializing class to determine information about the final state after the collision
        Parameters:
        Initial energy (in MeV)
        Initial flavor (True for electron, False for muon)
        Distance from starting point to detector
        Lepton number (1 for neutrino, -1 for antineutrino)
        """
        self.e_i = e_i
        self.flavor_i = flavor_i
        self.dist = dist
        self.lepton_number = lepton_number
        pass

    def neutrino_flavor(self):
        """Determine the flavor of the neutrino at the point of collision, assuming 2 flavor options
        Parameters:
        Initial flavor
        Distance from starting point to detector
        Returns:
        Flavor of neutrino
        """
        delta_m12_sq = 7.53*(10**(-5)) #ev^2
        prob_of_oscillation = 0.855*(math.sin(delta_m12_sq*self.dist/(4*self.e_i)))

        random_number = np.random.uniform(0, 1)

        did_they_oscillate = random_number <= prob_of_oscillation

        if did_they_oscillate == True:
            #If the neutrino oscillated, return the other flavor
            return not self.flavor_i

        else:
            #If the neutrino did not oscillate, return the initial flavor
            return self.flavor_i
        
    def energy_distribution(self):
        """Determine the energy of the individual neutrino based on a Gaussian distribution of
        the beam energy
        Parameters:
        Beam energy
        Returns:
        Energy of neutrino
        """
        random_number = np.random.uniform(0, 1)
        e_nu = NormalDist(mu=self.e_i, sigma=10).inv_cdf(random_number)
        return abs(e_nu)

        

    def final_particles(self):
        """Monte Carlo simulation to determine the final state particles of the neutrino Argon collision
        Parameters:
        Initial energy of neutrino
        Flavor of neutrino from neutrino_flavor (True for electron, False for muon)
        Returns:
        Final state particle types
        Final state particle charge
        Final state particle momenta
        """

        flavor = self.neutrino_flavor() #True for electron, False for muon
        e_nu = self.energy_distribution()

        def qes(x):
            """This function defines the probability of a quasi-elastic scattering event
            happening based on the energy of the initial neutrino. This function was derived
            from real neutrino experiments
            """
            return 2*x*(math.e**(-(x**2)))
        
        def dis(x):
            """This function defines the probability of a deep inelastic scattering event
            happening based on the energy of the initial neutrino. This function was derived
            from real neutrino experiments
            """
            if x <= 0.75:
                return 0
            else:
                return -math.e**(-x+0.5)+0.8
        
        def pi(x):
            """This function defines the probability of a pi resonance event
            happening based on the energy of the initial neutrino. This function was derived
            from real neutrino experiments
            """
            if x <= 0.25:
                return 0
            else:
                return 0.25*x*math.e**(-(x-0.75)**2)
        
        gev = e_nu/1000 

        qes_prob = qes(gev)
        dis_prob = dis(gev)
        pi_prob = pi(gev)
        
        sum_prob = qes_prob + dis_prob + pi_prob

        random_number = np.random.uniform(0, sum_prob)

        qes_truth = random_number <= qes_prob
        dis_truth = (random_number > qes_prob)&(random_number <= (qes_prob + dis_prob))
        pi_truth = (random_number > (qes_prob + dis_prob))&(random_number <= sum_prob)

        final_state_particles = [] #Names
        final_particles_energy = [] #MeV
        final_particles_charge = [] #+1 or -1
        final_particles_mass = [] #MeV Natural units babyyyy

        #Comparing these, we can find out what type of interaction it is
        if qes_truth:       
            interaction_type = "QES" #This is a quasi-elastic scattering interaction
            if self.lepton_number == 1: #Neutrino
                mass_i = 940.6 #Mass of the neutron target
                if flavor == True: #electron flavor
                    final_state_particles = ["electron", "proton"]
                if flavor == False: #muon flavor
                    final_state_particles = ["muon", "proton"]
            if self.lepton_number == -1: #AntiNeutrino
                mass_i = 938.272 #Mass of proton target
                if flavor == True: #electron flavor
                    final_state_particles = ["positron", "neutron"]
                if flavor == False: #muon flavor
                    final_state_particles = ["antimuon", "neutron"]

        if dis_truth:
            interaction_type = "DIS" #This is a deep inelastic scattering interaction
            if self.lepton_number == 1: #Neutrino
                if flavor == True:
                    final_state_particles = ["electron"]
                if flavor == False:
                    final_state_particles = ["muon"]
            if self.lepton_number == -1: #Antineutrino
                if flavor == True:
                    final_state_particles = ["positron"]
                if flavor == False:
                    final_state_particles = ["antimuon"]

        if pi_truth:
            interaction_type = "pi" #This is a pi resonance interaction
            random_chance = np.random.uniform(0, 1) #Does the neutrino hit a proton or neutron?
            random_second_chance = np.random.uniform(0, 1) #Picks between 2 possible final state options where necessary
            if self.lepton_number == 1: #Neutrino
                if flavor == True: #electron flavor
                    if random_chance >= 0.50: #Hits proton
                        mass_i = 938.272
                        final_state_particles = ["electron", "proton", "pi+"]
                    if random_chance < 0.50: #Hits neutron
                        mass_i = 940.6
                        if random_second_chance >= 0.50: #Produces proton
                            final_state_particles = ["electron", "proton", "pi0"]
                        if random_second_chance < 0.50: #Produces neutron
                            final_state_particles = ["electron", "neutron", "pi+"]
                if flavor == False: #muon flavor
                    if random_chance >= 0.50: #Hits proton
                        mass_i = 938.272
                        final_state_particles = ["muon", "proton", "pi+"]
                    if random_chance < 0.50: #Hits neutron
                        mass_i = 940.6
                        if random_second_chance >= 0.50: #Produces proton
                            final_state_particles = ["muon", "proton", "pi0"]
                        if random_second_chance < 0.50: #Produces neutron
                            final_state_particles = ["muon", "neutron", "pi+"]
            if self.lepton_number == -1: #AntiNeutrino
                if flavor == True: #electron flavor
                    if random_chance >= 0.50: #Hits proton
                        mass_i = 938.272
                        if random_second_chance >= 0.50: #Produces proton
                            final_state_particles = ["positron", "proton", "pi-"]
                        if random_second_chance < 0.50: #Produces neutron
                            final_state_particles = ["positron", "neutron", "pi0"]  
                    if random_chance < 0.50: #Hits neutron
                        mass_i = 940.6
                        final_state_particles = ["positron", "neutron", "pi-"]
                if flavor == False: #muon flavor
                    if random_chance >= 0.50: #Hits proton
                        mass_i = 938.272
                        if random_second_chance >= 0.50: #Produces proton
                            final_state_particles = ["antimuon", "proton", "pi-"]
                        if random_second_chance < 0.50: #Produces neutron
                            final_state_particles = ["antimuon", "neutron", "pi0"]  
                    if random_chance < 0.50: #Hits neutron
                        mass_i = 940.6
                        final_state_particles = ["antimuon", "neutron", "pi-"]

            i = 0
            #electron, positron, muon, antimuon, proton, neutron, pi-, pi0, pi+
            while i < len(final_state_particles):
                if final_state_particles[i] == "electron":
                    final_particles_mass.append(0.511)
                    final_particles_charge.append(-1)

                if final_state_particles[i] == "positron":
                    final_particles_mass.append(0.511)
                    final_particles_charge.append(1)

                if final_state_particles[i] == "muon":
                    final_particles_mass.append(105.700)
                    final_particles_charge.append(-1)

                if final_state_particles[i] == "antimuon":
                    final_particles_mass.append(105.700)
                    final_particles_charge.append(1)
            
                if final_state_particles[i] == "proton":
                    final_particles_mass.append(938.272)
                    final_particles_charge.append(1)

                if final_state_particles[i] == "neutron":
                    final_particles_mass.append(940.600)
                    final_particles_charge.append(0)
                
                if final_state_particles[i] == "pi+":
                    final_particles_mass.append(139.570)
                    final_particles_charge.append(1)

                if final_state_particles[i] == "pi-":
                    final_particles_mass.append(139.570)
                    final_particles_charge.append(-1)

                if final_state_particles[i] == "pi0":
                    final_particles_mass.append(134.977)
                    final_particles_charge.append(0)

                i+=1

            #energy distribution
            if qes_truth or pi_truth:
                final_mass = sum(final_particles_mass)
                energy_difference = mass_i + e_nu - final_mass #Energy leftover after the final particles are created
                distributed = energy_difference/(len(final_state_particles))
            
            if dis_truth == True:
                distributed = e_nu * np.random.uniform(0.25, 0.5)/(len(final_state_particles))

            j = 0
            while j < len(final_state_particles):
                final_particles_energy.append(final_particles_mass[j] + distributed)

                j+=1

        return final_state_particles, final_particles_mass, final_particles_energy, final_particles_charge, interaction_type, flavor, e_nu
