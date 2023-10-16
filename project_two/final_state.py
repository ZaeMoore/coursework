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
        qes_interaction = False
        dis_interaction = False
        pi_interaction = False
        def qes(e):
            """This function defines the probability of a quasi-elastic scatteringe event
            happening based on the energy of the initial neutrino. This function was derived
            from real neutrino experiments
            """
            return 0.2247*(e**-0.5)
        
        def dis(e):
            return -85064.6*(math.log(e+9.09))**(-14.1465) + 0.71
        
        def pi(e):
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

        final_state_particles = []
        final_particles_energy = []
        final_particles_charge = []
        final_particles_mass = [] #In MeV/c^2

        #Comparing these, we can find out what type of interaction it is
        if qes_yes > dis_yes and qes_yes > pi_yes:
            #This is a quasi-elastic scattering interaction
            qes_interaction = True
            if self.lepton_number == 1: #Neutrino
                if flavor == True: #electron type
                    final_state_particles = ["electron", "proton"]
                    final_particles_mass = [0.511, 938.272]
                #Final state is lepton and proton
                if flavor == False:
                    final_state_particles = ["muon", "proton"]

            energy_distribution = np.random.uniform(0,1)
            final_particles_energy[0] = final_particles_mass[0] + self.e_i*energy_distribution
            final_particles_energy[1] = final_particles_mass[1] + self.e_i*(1-energy_distribution)

        if dis_yes > qes_yes and dis_yes > pi_yes:
            #This is a deep inelastic scattering interaction
            dis_interaction = True
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
            #This is a pi resonance interaction
            pi_interaction = True
            random_chance = np.random.uniform(0, 1) #If >.50, hits proton. If <.50, hit neutron
            if self.lepton_number == 1: #Neutrino
                if flavor == True: #electron flavor
                    if random_chance >= 0.50: #Hits proton
                        final_state_particles = ["electron", "proton", "pi+"]
                #Does it hit proton or neutron? 50/50 chance



        #We now know what type of interaction it is and can determine the final state particles that come from this collision!
        

#Itll either be DIS, qel, or pi resonance. Which one it is depends on the initial energy, use figure 2.6 from the neutrino basics book. Only CC
#QE could hit proton or neutron, say it's a 50/50