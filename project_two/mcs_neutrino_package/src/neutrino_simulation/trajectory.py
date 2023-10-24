"""
Code for finding hit locations on pixel detector
given info regarding final state particles after neutrino interaction
"""

import math
import numpy as np


class FinalHit():
    def __init__(self, initialE, mass, charge, fieldStr):
        """
        Initializing class to determine information aout hit location and energy
        once particles reach pixel detector
        Parameters:
        initialE: initial energy of final state particles produced in neutrino interaction
        M: mass of final state particles
        C: charge of the final state particles
        fieldStr: strength of electric field
        """

        self.initialE = np.asarray(initialE)
        self.mass = np.asarray(mass)
        self.charge = np.asarray(charge)
        self.fieldStr = fieldStr
        self.mom = np.sqrt(2*self.mass*self.initialE)
        pass

    def momComponents(self, alpha):
        """
        takes the momentum of the particle and randomly selects two angles
        from some normal distrubition to define direction particle travels
        wrt x axis (path of incoming neutrino)

        parameters:
        Mom: momentums of the particles
        alpha: std in the normal distribution to sample angles from

       """


    
    
