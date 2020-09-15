"""

Main
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

Extras:

1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user.
If not, print a different appropriate message.

"""


#Main Challenge
number=int(input("Enter a number: "))

if number%2==0:
    print(number," is even!")
else:
    print(number," is odd")


#Challenge extra 1
number=int(input("Enter a number: "))
if number%4==0:
    print("number is divisible by 4")
elif number%2==0:
    print("number is divisible by 2")
else:
    print("number is not divisible by 4 or 2!")

#Challenge extra 2
num=int(input("Enter first number: "))
check=int(input("Enter second number: "))
if num%check==0:
    print(num,"is divisible by",check)
else:
    print(num,"is not divisible by",check)
