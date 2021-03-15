'''
Question 10

    Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing 
    all duplicate words and sorting them alphanumerically.

    Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again

    Then, the output should be:

again and hello makes perfect practice world

'''

# inp = set(input('Write a sentence: ').split(' '))

# print(' '.join(sorted(inp)))

#or

print(' '.join(sorted(set(input('Write a sentence: ').split(' ')))))