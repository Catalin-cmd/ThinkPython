'''
Question:

    Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
    The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
l=[]
for i in range(1000, 3001):
    j = str(i)
    for k in j:
        if int(j[0]) % 2 == 0 and int(j[1]) % 2 == 0 and int(j[2]) % 2 == 0 and int(j[3]) % 2 == 0:
            l.append(str(i))
        
print(','.join(sorted(set(l))))


# or, using ord() value for i in range(1000,3001)

lst = []

for i in range(1000,3001):
    flag = 1
    for j in str(i):          # every integer number i is converted into string
        if ord(j)%2 != 0:     # ord returns ASCII value and j is every digit of i. All the odd numbers(from 0 to 9) are odd in ASCII value too.
            flag = 0          # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))    # i is stored in list as string

print(",".join(lst))


