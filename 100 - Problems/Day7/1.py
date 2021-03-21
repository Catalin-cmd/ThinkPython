'''
Question 20:

    Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

    Suppose the following input is supplied to the program:

7

    Then, the output should be:

0
7
14
'''
class Solution:
    def generator(self, n):
        for i in range(0, n+n+1, 7):
            if n%7 == 0:
                print(i)
            
ob=Solution()
ob.generator(7)