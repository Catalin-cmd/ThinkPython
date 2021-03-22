'''
Question 23
Question:

    Write a method which can calculate square value of number

Hints:

Using the ** operator which can be written as n**p where means n^p
'''

class Square:
    def get_square(self,num):
        return num**2
    
ob1=Square()
print(ob1.get_square(6))