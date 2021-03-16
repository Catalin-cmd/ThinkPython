'''
Question 15:

    Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

    Suppose the following input is supplied to the program:

9

    Then, the output should be:

11106

'''
total=0
a = input('Write somethng: ')
for i in range(1,5):
    total+=int(i*a) #at first iteration, result will be a, at second one, result will be aa, we multiply a string by i times
print(total)
