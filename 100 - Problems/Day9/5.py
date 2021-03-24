'''
Question 30
Question:

    Define a function that can accept two strings as input and print the string with maximum length in console. 
    If two strings have the same length, then the function should print all strings line by line.
'''

str1 = input('First string: ')
str2 = input('Second string: ')

def length(st1, st2):
    if len(st1)>len(st2):
        print(st1)
    elif len(st2)>len(st1):
        print(st2)
    else:
        print(st1, st2, sep='\n')

length(str1,str2)