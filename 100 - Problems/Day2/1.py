'''

Question 4:

    Write a program which accepts a sequence of comma-separated numbers from console and generate a list 
    and a tuple which contains every number.Suppose the following input is supplied to the program:

34,67,55,33,12,98

    Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

'''


v = input('Enter a series of numbers separated by a comma: ') #Gets an input of comma-separated numbers

li = v.split(',') #split the string by comma
tu = tuple(li) #makes tuple from list

print(li)
print(tu)