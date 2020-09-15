"""

Main
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
2. Print out that many copies of the previous message on separate lines. 

"""


#Main Challenge
from datetime import date
name=input("Enter your name: ")
age=int(input("Enter your age: "))

currentyear = date.today().year
numberofyears=str((currentyear) + (100-age))

print("Hello " + name + ", you will be 100 in the year " + numberofyears +".")


#Challenge extra 1
message="Hello " + name + ", you will be 100 in the year " + numberofyears +". "
num=int(input("Enter a number: "))
for i in range(num):
    print(message, end='')
   

#Challenge extra 2
message="Hello " + name + ", you will be 100 in the year " + numberofyears +"."
num=int(input("\nEnter a number: "))
for i in range(num):
    print(message,"\n")
