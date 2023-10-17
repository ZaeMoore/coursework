"""
Code for finding hit locations on pixel detector
given info regarding final state particles after neutrino interaction
"""

import math
import numpy as np


class FinalHit():
    def __init__(self, initialE, M, C, fieldStr):
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
        self.M = np.asarray(M)
        self.C = np.asarray(C)
        self.fieldStr = fieldStr
        pass

    
