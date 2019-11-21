# Jackson J.
# 11/20/19
# This is the driver file
from classTextbook import Textbook


def menu():
    """Modifying Textbook
    Printing Textbook: adds to inv
    Decreasing inv
    Book info
    """
    print("")
    return


input("CLICK HERE, then PRESS ENTER")

print("Hello user, how are you?")
input(">>>")
print("And what might your name be?")
user = input(">>>")
print("Pleased to make your acquaintance, " + user + ".")

print("\nSo what is the name of the book you would like to enter information for?")
print("(Remember, to \"PRESS ENTER\" after typing)")
title = input('>>>')

print(f"\nAhh, I've heard of \"{title}\" before.")
print("I'm blanking on who the author is, would you mind helping me out?")

print("\nWhat's the authors first name?")
first = input(">>>")

print("\nAnd the last name?")
last = input('>>>')

print("\nFinally, what is their age?")
age = int(input('>>>'))

print("\nWhat edition is that?")
edition = input(">>>")

print("\nCoolio, now what's the ISBN number?")
isbn = int(input(">>>"))

print("\nWait. who was the publisher for them?")
pub = input(">>>")

print("\nWhen did they publish it? What year was that?")
year = int(input(">>>"))

print("\nHow many books are left in stock?")
quantity = int(input(">>>"))

print("\nAnd how much do those books sell for?")
price = int(input(">>>"))

book1 = Textbook(title, first, last, age, edition, isbn, pub, year, quantity, price)

print("\nWow, that's interesting")
print("And what about the other textbook?")
print("What was the name that one?")
title1 = input(">>>")

print("\nIs that one any good? I've never heard of it before.")
input(">>>")

print("\nHm, well who wrote it?")
print('What is the first name of this mysterious author?')
first1 = input(">>>")

print("\nAnd what is their last?")
last1 = input(">>>")

print("\nI think it's starting to come back to me.")
print("What was " + first1 + "'s age?")
age1 = int(input(">>>"))

print("\nI must have been thinking of someone else...")
print("Help me out for just a little longer.")
print("What's the edition of the book?")
edition1 = input(">>>")

print("Okay, and the ISBN number is")
isbn1 = int(input(">>>"))

print("\nOkay, almost done with these questions.")
print(f"Who is the publisher of \"{title1}\"?")
pub1 = input(">>>")

print("\nAnd what year was that published?")
year1 = int(input(">>>"))

print("\nSo how many are left in stock?")
quantity1 = int(input(">>>"))

print("\nOnly " + str(quantity1) + "left?")
print("So how much is that selling for?")
price = int(input(">>>"))

print("And that was the last of the \"Textbook\" questions.")
print("You can now interact with my system.\n")

menu()
