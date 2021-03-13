'''
Question:

    Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

    Suppose the following input is supplied to the program:

Hello world
Practice makes perfect

    Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
'''
ls=[]
while True:
    inp = input('Write how many lines do you want: ')
    if inp=='':
        break
    ls.append(inp)

print('\n'.join(ls).upper())