# Jackson J.
# 11/20/19
# This is the class file for the textbook
from classPerson import Person
from Textbook import menu


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

    def modify(self):
        print("What would you like to modify?")
        print("Title")
        print("Author")
        print("Edition")
        print("ISBN")
        print("Publisher")
        print("Year")
        print("Quantity")
        print("Price")
        change = input(">>>").title()
        if change == "Title":
            print("And what would you like to change that to??")
            self.title = input(">>>").title()
            print("The change has been made.")
            print("Do you wish to make another change?")
            another = input(">>>").title()
            if another == "Yes" or another == "Y":
                self.modify()
            else:
                print("Okay, I will take you back to the menu.")
                menu()
        elif change == "Author":
            print("What about the author would you like to change?")
            print("First Name")
            print("Last Name")
            print("Age")
            change = input(">>>").title()
            if change == "First" or change == "First Name" or change == "F" or change == "Fn":
                print("What is the new first name?")
                self.author.first = input(">>>").title()
                print("The change has been made.")
                print("Do you wish to make another change?")
                another = input(">>>").title()
                if another == "Yes" or another == "Y":
                    self.modify()
                else:
                    print("Okay, I will take you back to the menu.")
                    menu()
            elif change == "First" or change == "Last Name" or change == "L" or change == "Ln":
                print("What is the new last name?")
                self.author.last = input(">>>").title()
                print("The change has been made.")
                print("Do you wish to make another change?")
                another = input(">>>").title()
                if another == "Yes" or another == "Y":
                    self.modify()
                else:
                    print("Okay, I will take you back to the menu")
                    menu()

            elif change == "Age" or change == "A":
                print("What is the new age?")
                self.author.age = input(">>>")
                print("The change has been made.")
                print("Do you wish to make another change?")
                another = input(">>>").title()
                if another == "Yes" or another == "Y":
                    self.modify()
                else:
                    print("Okay, I will take you back to the menu")
                    menu()
