import math

# returns '4.08E+10'
class LongFloat():

    def __init__(self, sig_digits, exp, digits):
        self.sig_digits = sig_digits
        self.exp = exp
        self.digits = digits
        pass

    def to_LongFloat(self, value):
        if isinstance(value, LongFloat):
            return value
        elif isinstance(value, float):
            exp = round(math.log(float))
            sig = round(float / 10**exp, self.digits)
            return LongFloat(sig, exp)

    #x = a / 1eN * 10**b -> a and b are integers. N is just used to make sure a is between 0 and 10.
    #Define a print method that will print answewrs in sign fig
    #Each method will return LongFloat(a,b)

    def __add__(self, other):
        return other
    
    def __sub__(self, other):
        return other
    
    def __mul__(self, other):
        return other
    
    def __div__(self, other):
        return other
        

class Vector([]):

    def __add__(self, other):
        return other