'''
Question 40
Question:

    Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
'''
inp = input('Say something: ')
if (inp == 'yes') or (inp == 'Yes') or (inp == 'YES'):
    print('Yes')
else:
    print('No')
    
#or, the smarter way:

inp = input('Say something: ').lower()
if inp == 'yes':
    print('Yes')
else:
    print('No')