# Jackson J.
# 11/20/19
# This is the driver file
from classTextbook import Textbook


def menu():
    """Modifying Textbook
    Printing Textbook: adds to inv
    Decreasing inv
    """
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
        print(f"Choose from \"{textbook1.title}\" or \"{textbook2.title}\"")
        book = input(">>>").title()
        if book == textbook1.title:
            textbook1.book_info()

        elif book == textbook2.title:
            textbook2.book_info()

    elif do == "Modify Book Contents" or do == "Modify" or do == "Contents" or do == "M" or do == "C" or do == "Mbc":
        print()

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

print("\nWhat edition is that?")
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
