"""
=========== Simple Inheritance==============
1. Every classes is the subclass of super class 'Object'
2. Reusable of code
3. Transitive in nature. Means properties in super-class will automatically available in sup-class
"""

# by default class person is the sup-class of super-class Object
class ParentClass(object):

    # Constructor
    def __init__(self):
        print("Parent constructor called")

    def meParent(self):
        print("Hi, This is parent")


# Inherited or Subclass of Person
class ChildClass(ParentClass):

    def __init__(self):
        print("Child constructor called")

    # Here we return true
    def meChild(self):
        print("Hi, This is child")


# Object creation
parent = ParentClass()
parent.meParent()

print("\n")

child = ChildClass()
child.meChild()
child.meParent()

