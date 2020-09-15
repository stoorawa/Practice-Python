"""

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

"""

num=int(input("Enter a number: "))

print([number for number in range(1,num+1) if num%number == 0])


#or


num=int(input("Enter a number: "))

for number in range(1,num+1):
    if num%number==0:
        print(number)
