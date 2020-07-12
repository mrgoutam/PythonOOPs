"""
Protected members are those members of the class which cannot be accessed outside the class but can be
accessed from within the class and it’s subclasses.
"""

class Base:
    def __init__(self):
        # Protected member
        self._a = 2

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a) # this is accessible from this sub-class


obj1 = Derived()
obj2 = Base()

# Calling protected member Outside class will result in AttributeError
try:
    print(obj1.a)
except:
    print("Child instance: Error as a is protected and this is not accessible from out of the class")

try:
    print(obj2.a)
except:
    print("Base instance: Error as a is protected and this is not accessible from out of the class")


