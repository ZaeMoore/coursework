import math

sig = 10
exp = 4
digits = 2
list_one = [0, 1, 2, 3]

class Longgg():

    def __init__(self, sig_digits, exp, digits):
        self.sig = sig_digits
        self.exp = exp
        self.digits = digits
        pass

    def to_LongFloat(self, value):
        if isinstance(value, Longgg):
            return value.sig, value.exp
        elif isinstance(value, float):
            exp = round(math.log(float))
            sig = round(float / 10**exp, self.digits)
            return Longgg(sig, exp)

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

        print(sum_sig + "E" + sum_exp)
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

        print(diff_sig + "E" + diff_exp)
        return diff_sig, diff_exp
    
    def __mul__(self, other):
        sig2 = self.to_LongFloat(other)[0]
        exp2 = self.to_LongFloat(other)[1]

        mul_exp = self.exp + exp2
        mul_sig = self.sig * sig2

        new_exp = round(math.log(mul_sig))
        new_sig = round(mul_sig/10**new_exp, self.digits)

        new_exp += mul_exp

        print(new_sig + "E" + new_exp)
        return new_sig, new_exp
    
    def __div__(self, other):
        sig2 = self.to_LongFloat(other)[0]
        exp2 = self.to_LongFloat(other)[1]

        div_exp = self.exp - exp2
        div_sig = self.sig/sig2

        new_exp = round(math.log(div_sig))
        new_sig = round(div_sig/10**new_exp, self.digits)

        new_exp += div_exp

        print(new_sig + "E" + new_exp)
        return new_sig, new_exp


class Vector([]):
    #Should be able to add, subtract, multiple, or divice a vector by a Long High Precision Number. 
    #Will probably need to loop
    #Also make a sort method

    def __add__(self, other):
        return other
    

long_one = Longgg(sig, exp, digits)
vector_one = Vector(list_one)