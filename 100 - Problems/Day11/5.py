'''
Question 42
Question:

    Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
'''

l = [1,2,3,4,5,6,7,8,9,10]
def multiply_by2(item):
    return item*2
l = list(map(lambda x : x**2, l))
print(list(filter(lambda  x : x%2==0, l)))
