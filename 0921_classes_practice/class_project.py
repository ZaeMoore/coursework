import math

# returns '4.08E+10'
class LongFloat():

    def __init__(self, sig_digits, exp, digits):
        self.sig = sig_digits
        self.exp = exp
        self.digits = digits
        pass

    def to_LongFloat(self, value):
        if isinstance(value, LongFloat):
            return value.sig, value.exp
        elif isinstance(value, float):
            exp = round(math.log(float))
            sig = round(float / 10**exp, self.digits)
            return LongFloat(sig, exp)

    #x = a / 1eN * 10**b -> a and b are integers. N is just used to make sure a is between 0 and 10.
    #Define a print method that will print answewrs in sign fig
    #Each method will return LongFloat(a,b)

    #Add 2 precise long floats
    def __add__(self, other):
        sig2 = self.to_LongFloat(other)[0]
        exp2 = self.to_LongFloat(other)[1]

        diff = abs(self.exp - exp2) #Difference in exponential values
        if diff == 0:
            sum_sig = self.sig + sig2
            if sum_sig >= 10:
                sum_sig /= 10
                sum_exp = self.exp + 1
            else:
                sum_exp = self.exp
        elif self.exp > exp2:
            sig2_new = sig2/(10**diff)
            sum_sig = round(self.sig + sig2_new, self.digits)
            sum_exp = self.exp
        elif exp2 > self.exp:
            sig_new = self.sig/(10**diff)
            sum_sig = round(sig_new + sig2, self.digits)
            sum_exp = self.exp

        return sum_sig, sum_exp
    
    def __sub__(self, other):
        sig2 = self.to_LongFloat(other)[0]
        exp2 = self.to_LongFloat(other)[1]

        diff = abs(self.exp - exp2) #Difference in exponential values
        if diff == 0:
            diff_sig = self.sig - sig2
            diff_exp = self.exp
        elif self.exp > exp2:
            sig2_new = sig2/(10**diff)
            diff_sig = round(self.sig - sig2_new, self.digits)
            diff_exp = self.exp
        elif exp2 > self.exp:
            sig_new = self.sig/(10**diff)
            diff_sig = round(sig_new - sig2, self.digits)
            diff_exp = self.exp

        return diff_sig, diff_exp
    
    def __mul__(self, other):
        sig2 = self.to_LongFloat(other)[0]
        exp2 = self.to_LongFloat(other)[1]

        mul_exp = self.exp + exp2
        mul_sig = self.sig * sig2

        new_exp = round(math.log(mul_sig))
        new_sig = round(mul_sig/10**new_exp, self.digits)

        new_exp += mul_exp

        return new_sig, new_exp
    
    def __div__(self, other):
        sig2 = self.to_LongFloat(other)[0]
        exp2 = self.to_LongFloat(other)[1]

        diff_exp = self.exp - exp2
        diff_sig = self.sig - sig2

        

        return other
        

class Vector([]):

    def __add__(self, other):
        return other