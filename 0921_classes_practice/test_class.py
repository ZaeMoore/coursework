

class LongFloat():

#init is called automatically when you create an instance of a class
#In this case, when you call this class you must pass it a value because __init__ requires it
#The self is passed to every method because that is how you access the instance of the class itself
    def __init__(self, value):
        self.value = value
        pass

    def print(self, some_string):
        print(some_string)

    def __add__(self, number): #This is a specially named method that Python recognizes
        return self.value + number

#You can have classes inherit from other classes

class Chair(): #Parent class
    def __init__(self):
        pass
    def sit(self):
        pass

class RecliningChair(Chair):
    def __init__(self):
        super().__init__() #This initializes the parent class Chair
        pass



'''
To call this in a terminal
a = test_class.LongFloat(value)
a.print("String")
'''
