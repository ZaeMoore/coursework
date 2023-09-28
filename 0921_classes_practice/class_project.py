import math
'''
* high precision floating point object
      * add / subtract / multiply / divide
      * built ontop of integers
      * use base 10
      * choose a specific number of significant digits
      * methods should accept either a LongFloat or float
      * define a print() in scientific notation 
* high precision vector inherited from list
      * (same methods as the floating point object)
      * implement a sort method
'''
sig = 10
exp = 4
digits = 2
list_one = [0, 1, 2, 3]
import matplotlib.pyplot as plt
import timeit

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
            exp = round(math.log(value))
            sig = round(value / 10**exp, self.digits)
            return sig, exp

    #Add 2 precise long floats
    def __add__(self, other):
        sig2 = round(math.log(other))
        exp2 = round(other / 10**exp, self.digits)

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

        #print(new_sig + "E" + new_exp)
        return new_sig, new_exp


class Vector():

    def __init__(self, vector, digits):
        self.digits = digits
        self.vector = vector
        pass

    def to_LongFloat(self, value):
        exp = round(math.log(value))
        sig = round(value / 10**exp, self.digits)
        return sig, exp

    def __add__(self, vector_other):
        new_vector_sig = []
        new_vector_exp = []
        sig1_vector = []
        sig2_vector = []
        exp1_vector = []
        exp2_vector = []
        i = 0
        for i in range(len(self.vector)):
            sig1_vector.append(self.to_LongFloat(self.vector[i])[0])
            exp1_vector.append(self.to_LongFloat(self.vector[i])[1])
            sig2_vector.append(self.to_LongFloat(vector_other[i])[0])
            exp2_vector.append(self.to_LongFloat(vector_other[i])[1])
            new_vector_sig.append(sig1_vector[i] + sig2_vector[i])
            new_vector_exp.append(exp1_vector[i] + exp2_vector[i])
        return new_vector_sig, new_vector_exp
    
    def __sub__(self, vector_other):
        new_vector_sig = []
        new_vector_exp = []
        sig1_vector = []
        sig2_vector = []
        exp1_vector = []
        exp2_vector = []
        for i in self.vector:
            sig1_vector.append(self.to_LongFloat(self.vector)[0])
            exp1_vector.append(self.to_LongFloat(self.vector)[1])
            sig2_vector.append(self.to_LongFloat(vector_other)[0])
            exp2_vector.append(self.to_LongFloat(vector_other)[1])
            new_vector_sig.append(sig1_vector[i] - sig2_vector[i])
            new_vector_exp.append(exp1_vector[i] - exp2_vector[i])

        return new_vector_sig, new_vector_exp
    
    def __mul__(self, vector_other):
        new_vector_sig = []
        new_vector_exp = []
        sig1_vector = []
        sig2_vector = []
        exp1_vector = []
        exp2_vector = []
        for i in self.vector:
            sig1_vector.append(self.to_LongFloat(self.vector)[0])
            exp1_vector.append(self.to_LongFloat(self.vector)[1])
            sig2_vector.append(self.to_LongFloat(vector_other)[0])
            exp2_vector.append(self.to_LongFloat(vector_other)[1])
            new_vector_sig.append(sig1_vector[i] * sig2_vector[i])
            new_vector_exp.append(exp1_vector[i] * exp2_vector[i])

        return new_vector_sig, new_vector_exp
    
    def __div__(self, vector_other):
        new_vector_sig = []
        new_vector_exp = []
        sig1_vector = []
        sig2_vector = []
        exp1_vector = []
        exp2_vector = []
        for i in self.vector:
            sig1_vector.append(self.to_LongFloat(self.vector)[0])
            exp1_vector.append(self.to_LongFloat(self.vector)[1])
            sig2_vector.append(self.to_LongFloat(vector_other)[0])
            exp2_vector.append(self.to_LongFloat(vector_other)[1])
            new_vector_sig.append(sig1_vector[i] / sig2_vector[i])
            new_vector_exp.append(exp1_vector[i] / exp2_vector[i])

        return new_vector_sig, new_vector_exp
    
    def sort(self):
        x = self.vector
        for i in range(len(x)):
            for j in range(0, len(x) - i - 1):
                if x[j] > x[j+1]:
                    x[j], x[j+1] = x[j+1], x[j]
        
        return x

    def mergesort(self, list):
        x = list
        n = len(x)
        if n > 1:
            mid = n // 2
            left = x[:mid]
            right = x[mid:]

            #Repeat the splitting and sorting for each half
            self.mergesort(left)
            self.mergesort(right)
        
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    x[k]=left[i]
                    i=i+1
                else:
                    x[k]=right[j]
                    j=j+1
                k=k+1

            while i < len(left):
                x[k]=left[i]
                i=i+1
                k=k+1

            while j < len(right):
                x[k]=right[j]
                j=j+1
                k=k+1
        return x
    
    def sort_compare(self):
        n = len(self.vector)
        y1 = timeit.timeit("self.sort()")
        y2 = timeit.timeit("self.mergesort()")
        x = (1, 2)
        y = (y1, y2)
        plt.figure(1)
        plt.scatter(x, y)
        plt.annotate("Bubble sort", (1, y1))
        plt.annotate("Merge sort", (2, y2))
        plt.savefig("sortcompare")
        print("Plot for time to sort list of length {n}", n=n)
    