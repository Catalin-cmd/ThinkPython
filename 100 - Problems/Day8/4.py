'''
Question 25
Question:

    Define a class, which have a class parameter and have a same instance parameter.
    
'''
#Classes and instances have attributes, not parameters

class ClassAttr:
    var = 7 #this is an class attribute
    def __init__(self, var1 = 8):
        self.var1 = var1 #instance attribute
        
number = ClassAttr()
print(number.var)
print(number.var1)