'''
Question 31
Question:

    Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
'''

def dict_values1():
    d = dict()
    for i in range(1,21):
        d[i]=i*2
    print('dict_values1:', d)

def dict_values2():
    d = {i:i*2 for i in range(1,21)}
    print('dict_values2:', d)
    
dict_values1()
dict_values2()