# Jackson J.
# 11/20/19
# This is the person class for the textbook lab project. Simple


class Person:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def details(self):
        return "Their name is " + self.first + " " + self.last + " and their age is " + str(self.age)

    def details1(self):
        """I could use either detail statement for the Person"""
        return self.first + " " + self.last + " is " + str(self.age)


mypeep = Person("Jared", "Jackson", 18)
print(mypeep.details())
print(mypeep.details1())
