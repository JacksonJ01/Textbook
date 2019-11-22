# Jackson J.
# 11/20/19
# This is the driver file
from classTextbook import Textbook


def modify(self):
    print("\nWhat would you like to modify?")
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

        elif change == "Age" or change == "A":
            print("What is the new age?")
            self.author.age = int(input(">>>"))
            print("The change has been made.")
            print("Do you wish to make another change?")
            another = input(">>>").title()
            if another == "Yes" or another == "Y":
                self.modify()
            else:
                print("Okay, I will take you back to the menu")

    elif change == "Edition" or change == "E":
        print("What would you like to change the edition to?")
        self.edition = input('>>>')
        print("The change has been made.")
        print("Do you wish to make another change?")
        another = input(">>>").title()
        if another == "Yes" or another == "Y":
            self.modify()
        elif another == "No" or another == "N":
            print("Okay, I will take you back to the menu?")

    elif change == "Isbn"or change == "I":
        print("What would you like to change the ISBN number to?")
        self.isbn = int(input(">>>"))
        print("The change has been made.")
        print("Do you wish to make another change?")
        another = input(">>>").title()
        if another == "Yes" or another == "Y":
            self.modify()
        elif another == "No" or another == "N":
            print("Okay, I will take you back to the menu?")

    elif change == "Publisher":
        print("What would you like to change about the publisher")
        self.pub = input(">>>")
        print("The change has been made")
        print("Do you wish to make another change?")
        another = input(">>>").title()
        if another == "Yes" or another == "Y":
            self.modify()
        elif another == "No" or another == "N":
            print("Okay, I will take you back to the menu?")

    elif change == "Year":
        print("What would you like to change the year to?.")
        self.year = int(input(">>>"))
        print("The change has been made.")
        print("Do you wish to make another change?")
        another = input(">>>").title()
        if another == "Yes" or another == "Y":
            self.modify()
        elif another == "No" or another == "N":
            print("Okay, I will take you back to the menu?")

    elif change == "Quantity":
        print("Has the quantity increased or decreased?")
        new = input(">>>").title()
        if new == "Increased" or new == "Increase" or new == "I":
            print("Okay, I will add one book to the invetory.")
            self.add_inv()
            print("It has been done.")
            print("I will take you back to the menu now.")

        elif new == "Decreased" or new == "Decrease" or new == "D":
            print("Okay, I will take a book out of the invetory.")
            self.deduct_inv()
            print("It has been done.")
            print("I will take you to the menu.")

    elif change == "Price":
        print("What? The price changed? What did it change to?")
        new = int(input(">>>"))
        if new < self.price:
            print("Oh, the price went down?")
            print("Nice?")
        elif new > self.price:
            print("What?! The price went up? Dang.")
        self.price = new


def menu():
    print("What would you like to do at the menu?")
    print("You can see:")
    print("-Book Info")
    print("Or you can:")
    print("-Modify Book Contents")
    print("And if you wish to, you can:")
    print("-Leave")
    do = input(">>>").title()

    if do == "Book Info" or do == "Book" or do == "Info" or do == "B" or do == "I" or do == "Bi":
        print("Which book would you like to see information for?")
        print(f"Choose \"{textbook1.title}\" or \"{textbook2.title}\"")
        book = input(">>>").title()
        if book == textbook1.title:
            textbook1.book_info()
            menu()

        elif book == textbook2.title:
            textbook2.book_info()
            menu()

    elif do == "Modify Book Contents" or do == "Modify" or do == "Contents" or do == "M" or do == "C" or do == "Mbc":
        print("Which textbook do you want to modify?")
        print(f'Choose "{textbook1.title}" or "{textbook2.title}"')
        book = input(">>>")
        if book == textbook1.title:
            modify(textbook1)
            menu()

        elif book == textbook2.title:
            modify(textbook2)
            menu()

    elif do == "Leave" or do == "L":
        print("Have a good day")
        exit()

    else:
        # while do != "Book Info" or do != "Book" or do != "Info" or do != "B" or do != "I" or do != "Bi" or do != "Modify Book Contents" or do != "Modify" or do != "Contents" or do != "M" or do != "C" or do != "Mbc" or do != "Leave" or do != "L":
        # print("Can you repeat that again?")
        # print("You can type a \"B\", an \"M\", or an \"L\"")
        # do = input(">>>").title
        # if do == "Book Info" or do == "Book" or do == "Info" or do == "B" or do == "I" or do == "Bi" or do == "Modify Book Contents" or do == "Modify" or do == "Contents" or do == "M" or do == "C" or do == "Mbc" or do == "Leave" or do == "L":
        # break
        print("I didn't catch that")
        menu()

    print("Would you like to go back to the menu?")
    back = input(">>>").title()
    if back == "No" or back == "N":
        print("Are you sure?")
        sure = input(">>>").title()
        if sure == "Yes" or sure == "Y":
            print("Alright")
            exit()
        elif sure == "No" or sure == "N":
            print("Alright, of to the menu we go")
            menu()
        else:
            print("Uhm, that wasn't a yes or no answer, so I'll take you to the menu anyways")
            print("You can leave for there if you wish")

    else:
        print("Okay, back to the menu we go")
        menu()


input("CLICK HERE, then PRESS ENTER")

print("Hello user, how are you?")
input(">>>").title()
print("And what might your name be?")
user = input(">>>").title()
print("Pleased to make your acquaintance, " + user + ".")

print("\nSo what is the name of the book you would like to enter information for?")
print("(Remember, to \"PRESS ENTER\" after typing)")
title = input('>>>').title()

print(f"\nAhh, I've heard of \"{title}\" before.")
print("I'm blanking on who the author is, would you mind helping me out?")

print("\nWhat's the authors first name?")
first = input(">>>").title()

print("\nAnd the last name?")
last = input('>>>').title()

print("\nFinally, what is their age?")
age = int(input('>>>'))

print("\nWhat edition this book?")
edition = input(">>>").title()

print("\nCoolio, now what's the ISBN number?")
isbn = int(input(">>>"))

print("\nWait. who was the publisher for them?")
pub = input(">>>").title()

print("\nWhen did they publish it? What year was that?")
year = int(input(">>>"))

print("\nHow many books are left in stock?")
quantity = int(input(">>>"))

print("\nAnd how much do those books sell for?")
price = int(input(">>>"))

textbook1 = Textbook(title, first, last, age, edition, isbn, pub, year, quantity, price)

print("\nWow, that's interesting")
print("And what about the other textbook?")
print("What was the name that one?")
title1 = input(">>>").title()

print("\nIs that one any good? I've never heard of it before.")
input(">>>").title()

print("\nHm, well who wrote it?")
print('What is the first name of this mysterious author?')
first1 = input(">>>").title()

print("\nAnd what is their last?")
last1 = input(">>>").title()

print("\nI think it's starting to come back to me.")
print("What was " + first1 + "'s age?")
age1 = int(input(">>>"))

print("\nI must have been thinking of someone else...")
print("Help me out for just a little longer.")
print("What's the edition of the book?")
edition1 = input(">>>").title()

print("Okay, and the ISBN number is")
isbn1 = int(input(">>>"))

print("\nOkay, almost done with these questions.")
print(f"Who is the publisher of \"{title1}\"?")
pub1 = input(">>>").title()

print("\nAnd what year was that published?")
year1 = int(input(">>>"))

print("\nSo how many are left in stock?")
quantity1 = int(input(">>>"))

print("\nOnly " + str(quantity1) + "left?")
print("So how much is that selling for?")
price1 = int(input(">>>"))

textbook2 = Textbook(title1, first1, last1, age1, edition1, isbn1, pub1, year1, quantity1, price1)

print("And that was the last of the \"Textbook\" questions.")
print("You can now interact with my system.\n")

menu()
