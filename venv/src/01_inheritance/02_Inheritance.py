"""
How constructors are called
"""
class ParentClass(object):
    m = 'Hello Mr Parent'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def basicDetails(self):
        print("Hi Mr "+self.name+"("+str(self.age)+")")

    def toString(self):
        print("toString in parent")


class ChildClass(ParentClass):

    # this class initialization
    def __init__(self, name, age, salary, post):
        # parent class initialization
        #ParentClass.__init__(self, name, age)
        super().__init__(name, age)
        self.salary = salary
        self.post = post

    def childDetails(self):
        print("Salary: "+str(self.salary)+" Prof: "+self.post)

    def toString(self):
        super().toString() # calling super class same named method
        print("toString in child")

a = ChildClass('Goutam D', 27, 150000, 'AI Expart')
a.basicDetails()
a.childDetails()
print(a.m)
a.toString()

