'''
Question 39
Question:

    Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
'''

t = (1,2,3,4,5,6,7,8,9,10)
t2 = tuple(i for i in t if i%2==0)
print(t2)