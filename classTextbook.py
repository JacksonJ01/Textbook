# Jackson J.
# 11/20/19
# This is the class file for the textbook
from classPerson import Person


class Textbook:

    def __init__(self, title, first, last, age, edition, isbn_number, publisher, year, quantity, price):
        self.title = title
        self.author = Person(first, last, age)
        self.edition = edition
        self.isbn = isbn_number
        self.pub = publisher
        self.year = year
        self.quantity = quantity
        self.price = price

    def add_inv(self):
        self.quantity += 1
        return self.quantity

    def deduct_inv(self):
        self.quantity -= 1
        if self.quantity < 5:
            print("Warning! Your quantity is below 5.")
        return self.quantity

    def book_info(self):
        print("Title: " + self.title)
        print(f"The author is: {self.author.details()}")
        print("It is the", self.edition, "edition")
        print("The ISBN number is: " + self.isbn)
        print(f"The publisher of \"{self.title}\" is: {self.pub}")
        print("It was published in", self.year)
        print("There are " + self.quantity + " left in stock")
        print(f"This book goes for {self.price} on the market")
