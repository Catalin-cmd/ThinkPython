'''
Question 28
Question:

    Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.
'''
str1 = input('First number: ')
str2 = input('Second number: ')

def sum(num1,num2):
    sum = int(num1)+int(num2)
    print(sum)

sum(str1,str2)