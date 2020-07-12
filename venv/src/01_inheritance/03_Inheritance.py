"""
Multiple inheritance
"""

class P1(object):
    def __init__(self):
        self.str1 = "Parent 1"
        print("Parent 1 print")

    def toString(self):
        print("toString: P1")


class P2(object):
    def __init__(self):
        self.str2 = "Parent 2"
        print("Parent 2 print")

    def toString(self):
        print("toString: P2")


class C(P1, P2):
    def __init__(self):
        P1.__init__(self)
        P2.__init__(self)
        print("Child print")

    def printStrs(self):
        print(self.str1, self.str2)

    def toString(self):
        P1.toString(self)
        P2.toString(self)
        print("toString: C")


ob = C()
ob.printStrs()
ob.toString()