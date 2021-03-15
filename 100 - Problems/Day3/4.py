'''

Question 13:

    Write a program that accepts a sentence and calculate the number of letters and digits.

    Suppose the following input is supplied to the program:

hello world! 123

    Then, the output should be:

LETTERS 10
DIGITS 3
'''

def sentence(inp):
    alph, num = 0, 0
    for i in inp:
        if i.isalpha():
            alph+=1
        if i.isdigit():
            num+=1
    print('LETTERS', alph, '\nDIGITS', num)
    
sentence('hello world! 123')