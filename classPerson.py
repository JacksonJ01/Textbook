# Jackson J.
# 11/20/19
# This is the person class for the textbook lab project. Simple


class Person:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def details(self):
        return "Their name is " + self.first + " " + self.last + " and they are " + str(self.age)
