'''

Question 16:

    Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. 
    >Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9

    Then, the output should be:

1,9,25,49,81

'''
inp = input('Write a list of numbers:\n-->').split(',')

def lista(num): #function for map
    return num**2

odd = [int(i) for i in inp if int(i)%2!=0] #return a list with integer odd numbers
restul = list(map(lista,odd))
print(', '.join(str(i) for i in restul)) #here each element in list must be string