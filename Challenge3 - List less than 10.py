"""

Main
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.


Extras:
1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
2. Ask the user for a number and return a list that contains only elements from the original list that are smaller than that number given by the user.

"""


#Main Challenge
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for number in a:
    if number<5:
        print(number)



#Challenge extra 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
l=[]
for number in a:
    if number<5:
        l.append(number)
print(l)

#or

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
l=[number for number in a if number<5]
print(l)


#Challenge extras 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
yournumber=float(input("Enter a number: "))
l=[number for number in a if number<yournumber]
print(l)
