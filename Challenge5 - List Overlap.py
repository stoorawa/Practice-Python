"""

Main
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this

"""


#Main Challenge
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#prints unique values in two lists
a=list(set(a))
b=list(set(b))
print(a)
print(b)

#prints matching values as a list
print([i for i in a if i in b])

#Challenge Extra 1
import random
#Generate 11 and 13 random numbers between 1 and 99
randomlist1 = random.sample(range(100), 11)
print(randomlist1)
randomlist2 = random.sample(range(100), 13)
print(randomlist2)
print([i for i in randomlist1 if i in randomlist2])
