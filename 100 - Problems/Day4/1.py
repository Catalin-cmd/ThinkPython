'''
Question:

    Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

    Suppose the following input is supplied to the program:

Hello world!

    Then, the output should be:

UPPER CASE 1
LOWER CASE 9
'''
upper, lower = 0, 0
inp = input('Write a sentence:\n--> ')
for i in inp:
    if i.isupper():
        upper+=1
    if i.islower():
        lower+=1
print('UPPER CASE', upper, '\nLOWER CASE', lower)