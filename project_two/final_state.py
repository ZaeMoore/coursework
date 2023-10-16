"""
Monte Carlo simulation for neutrino flavor and final state
Returns stuff to main script
"""
import math
import numpy as np

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
        theta_12 = 33.82 #deg
        delta_m12_sq = 7.53*(10**(-5)) #ev^2
        prob_of_oscillation = 0.855*(math.sin(delta_m12_sq*self.dist/(4*self.e_i)))

        number_trials = 10000
        random_number = np.random.uniform(0, 1, size=number_trials) #10,000 possible neutrinos

        did_they_oscillate = random_number <= prob_of_oscillation #Of the 10,000, did they oscillate? true/false
        
        yes_they_oscillated = did_they_oscillate.sum() #Number that oscillated

        if yes_they_oscillated >= number_trials/2:
            #If the neutrino oscillated, return the other flavor
            return not self.flavor_i

        else:
            #If the neutrino did not oscillate, return the initial flavor
            return self.flavor_i

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

        def qes(e):
            """This function defines the probability of a quasi-elastic scattering event
            happening based on the energy of the initial neutrino. This function was derived
            from real neutrino experiments
            """
            return 0.2247*(e**-0.5)
        
        def dis(e):
            """This function defines the probability of a deep inelastic scattering event
            happening based on the energy of the initial neutrino. This function was derived
            from real neutrino experiments
            """
            return -85064.6*(math.log(e+9.09))**(-14.1465) + 0.71
        
        def pi(e):
            """This function defines the probability of a pi resonance event
            happening based on the energy of the initial neutrino. This function was derived
            from real neutrino experiments
            """
            return 0.1593*(e**-0.5)
        
        qes_prob = qes(self.e_i)
        dis_prob = dis(self.e_i)
        pi_prob = pi(self.e_i)
        
        sum_prob = qes_prob + dis_prob + pi_prob

        number_trials = 10000
        random_number = np.random.uniform(0, sum_prob, size=number_trials)

        qes_truth = random_number <= qes_prob
        dis_truth = random_number >= qes_prob and random_number <= (qes_prob + dis_prob)
        pi_truth = random_number >= (qes_prob + dis_prob) and random_number <= sum_prob

        qes_yes = qes_truth.sum()
        dis_yes = dis_truth.sum()
        pi_yes = pi_truth.sum()

        final_state_particles = [] #Names
        final_particles_energy = [] #MeV
        final_particles_charge = [] #+1 or -1
        final_particles_mass = [] #MeV/c^2

        #Comparing these, we can find out what type of interaction it is
        if qes_yes > dis_yes and qes_yes > pi_yes:          
            interaction_type = "QES" #This is a quasi-elastic scattering interaction
            if self.lepton_number == 1: #Neutrino
                if flavor == True: #electron flavor
                    final_state_particles = ["electron", "proton"]
                if flavor == False: #muon flavor
                    final_state_particles = ["muon", "proton"]
            if self.lepton_number == -1: #AntiNeutrino
                if flavor == True: #electron flavor
                    final_state_particles = ["electron", "proton"]
                if flavor == False: #muon flavor
                    final_state_particles = ["muon", "proton"]

        if dis_yes > qes_yes and dis_yes > pi_yes:
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

        else:
            interaction_type = "pi" #This is a pi resonance interaction
            random_chance = np.random.uniform(0, 1) #Does the neutrino hit a proton or neutron?
            random_second_chance = np.random.uniform(0, 1) #Picks between 2 possible final state options where necessary
            if self.lepton_number == 1: #Neutrino
                if flavor == True: #electron flavor
                    if random_chance >= 0.50: #Hits proton
                        final_state_particles = ["electron", "proton", "pi+"]
                    if random_chance < 0.50: #Hits neutron
                        if random_second_chance >= 0.50: #Produces proton
                            final_state_particles = ["electron", "proton", "pi0"]
                        if random_second_chance < 0.50: #Produces neutron
                            final_state_particles = ["electron", "neutron", "pi+"]
                if flavor == False: #muon flavor
                    if random_chance >= 0.50: #Hits proton
                        final_state_particles = ["muon", "proton", "pi+"]
                    if random_chance < 0.50: #Hits neutron
                        if random_second_chance >= 0.50: #Produces proton
                            final_state_particles = ["muon", "proton", "pi0"]
                        if random_second_chance < 0.50: #Produces neutron
                            final_state_particles = ["muon", "neutron", "pi+"]
            if self.lepton_number == -1: #AntiNeutrino
                if flavor == True: #electron flavor
                    if random_chance >= 0.50: #Hits proton
                        if random_second_chance >= 0.50: #Produces proton
                            final_state_particles = ["positron", "proton", "pi-"]
                        if random_second_chance < 0.50: #Produces neutron
                            final_state_particles = ["positron", "neutron", "pi0"]  
                    if random_chance < 0.50: #Hits neutron
                        final_state_particles = ["positron", "neutron", "pi-"]
                if flavor == False: #muon flavor
                    if random_chance >= 0.50: #Hits proton
                        if random_second_chance >= 0.50: #Produces proton
                            final_state_particles = ["antimuon", "proton", "pi-"]
                        if random_second_chance < 0.50: #Produces neutron
                            final_state_particles = ["antimuon", "neutron", "pi0"]  
                    if random_chance < 0.50: #Hits neutron
                        final_state_particles = ["anitmuon", "neutron", "pi-"]

            #Percent of neutrino energy that is distributed to the final state particles on top of their rest mass energy
            energy_distribution = np.random.uniform(0.25, 0.75)
            nu_energy_given = energy_distribution/len(final_state_particles) #each particle gets the same energy to simplify the problem

            i = 0
            #electron, positron, muon, antimuon, proton, neutron, pi-, pi0, pi+
            while i < len(final_state_particles):
                if final_state_particles[i] == "electron":
                    final_particles_mass[i] = 0.511
                    final_particles_charge[i] = -1

                if final_state_particles[i] == "positron":
                    final_particles_mass[i] = 0.511
                    final_particles_charge[i] = 1

                if final_state_particles[i] == "muon":
                    final_particles_mass[i] = 105.7
                    final_particles_charge[i] = -1

                if final_state_particles[i] == "antimuon":
                    final_particles_mass[i] = 105.7
                    final_particles_charge[i] = 1
            
                if final_state_particles[i] == "proton":
                    final_particles_mass[i] = 938.272
                    final_particles_charge[i] = 1

                if final_state_particles[i] == "neutron":
                    final_particles_mass[i] = 938.272
                    final_particles_charge[i] = 0
                
                if final_state_particles[i] == "pi+":
                    final_particles_mass[i] = 938.272
                    final_particles_charge[i] = 1

                if final_state_particles[i] == "pi-":
                    final_particles_mass[i] = 938.272
                    final_particles_charge[i] = -1

                if final_state_particles[i] == "pi0":
                    final_particles_mass[i] = 938.272
                    final_particles_charge[i] = 0

                #energy distribution
                final_particles_energy[i] = final_particles_mass[i] + self.e_i*nu_energy_given

                i+=1

        return final_state_particles, final_particles_mass, final_particles_energy, final_particles_charge, interaction_type
