"""
Code for finding hit locations on pixel detector
given info regarding final state particles after neutrino interaction
"""

import math
import numpy as np
import scipy

def F(y, t, fieldStr, fieldOscFreq, fieldOscStr, gamma, chargeVal, ):
    "Function for scipy ODE integration"
    
    return [y[1], (-gamma*y[1]) + chargeVal*fieldStr + fieldOscStr*np.sin(fieldOscFreq*y[0])]

def findClosest(array, val):
    "Finds value closest value to (+/-)val in an array and returns that value and its index"
    
    array = np.asarray(array)
    idx = (np.abs(array - val)).argmin()
    return idx
    

class FinalHit:
    def __init__(self, initialE, mass, charge, fieldStr, fieldOscFreq, fieldOscStr,gamma):
        """
        Initializing class to determine information aout hit location and energy
        once particles reach pixel detector
        Parameters:
        initialE: initial energy of final state particles produced in neutrino interaction
        mass: mass of final state particles
        charge: charge of the final state particles
        fieldStr: strength of average electric field
        fieldOscFreq: frequency field oscillates (in x)
        fieldOscStr: strength of oscillations (in x)
        gamma: a sort of drag coefficient of the particle
        """

        self.initialE = np.asarray(initialE)
        self.mass = np.asarray(mass)
        self.charge = np.asarray(charge)
        self.fieldStr = fieldStr
        self.fieldOscFreq = fieldOscFreq
        self.fieldOscStr = fieldOscStr
        self.gamma = gamma
        self.mom = np.sqrt(2*self.mass*self.initialE)
        pass

    def vComponents(self, alpha):
        """
        takes the momentum of the particle and randomly selects two angles
        from some normal distrubition to define direction particle travels
        wrt x axis (path of incoming neutrino)

        assume particles traveling in z direction

        parameters:
        Mom: momentums of the particles
        alpha: std in the normal distribution to sample angles from

        returns:
        xVel: velocity in x direction
        yVel: velocity in y direction
        zVel: velocity in z direction

       """

        absVelocity = self.mom/self.mass #non relativistic neutrinos
        theta = np.random.normal(loc = 0.0, scale = alpha, size = len(self.mom))
        rng = np.random.default_rng()
        phi = rng.random(len(self.mom))*np.pi*2
        xVel = absVelocity*np.sin(theta)*np.cos(phi)
        yVel = absVelocity*np.sin(theta)*np.sin(phi)
        zVel = absVelocity*np.cos(theta)

        return xVel, yVel, zVel

    

    def WhereHit(self, xVel, yVel, zVel, xPos, xNeg):
        """
        Takes velocities and returns hit locations and energies
        once particles reach some point along x axis
        
        parameters:
        xVel: velocity in x direction
        yVel: velocity in y direction
        zVel: velocity in z direction
        xPos: location of pixel detector along positive x axis
        xNeg: location of pixel detector along negative x axis

        """
        hitLocX = []
        hitLocY = []
        hitLocZ = []
        E = []
        a_t = np.arange(start = 0, stop = 50, step = 0.1)
                
                
            
        for i in range(len(self.initialE)):
            finalVelZ = zVel[i]
            finalVelY = yVel[i]
            initVelX = xVel[i]
            finalMass = self.mass[i]

            sol = scipy.integrate.odeint(
                F,
                [0, initVelX],
                a_t,
                args = (self.fieldStr, self.fieldOscFreq, self.fieldOscStr, self.gamma, self.charge[i])
                )
            if self.charge[i] == -1:
                idx = findClosest(sol[:,0], xNeg)
                finalX = xNeg
            if self.charge[i] == 1:
                idx = findClosest(sol[:,0], xPos)
                finalX = xPos

            finalVelX = sol[idx,1]
            finalE = (finalVelZ**2 + finalVelY**2 + finalVelX**2)
            time = a_t[idx]
            finalY = finalVelY*time
            finalZ = finalVelZ*time

            hitLocX.append(finalX)
            hitLocY.append(finalY)
            hitLocZ.append(finalZ)
            E.append(finalE)
            print(i)
                                             
        return(hitLocX, hitLocY, hitLocZ, E)




            

    
