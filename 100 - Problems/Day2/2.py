'''Question 5:

    Define a class which has at least two methods:

        getString: to get a string from console input
        printString: to print the string in upper case.

    Also please include simple test function to test the class methods.
    
'''

class Test:
       
    def getString(self):
        self.inp = input('Please write something: ')
    
    def printString(self):
        print(self.inp.upper())
    
ob1 = Test() 
ob1.getString()
ob1.printString()