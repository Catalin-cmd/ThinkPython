'''

Question 17:

    Write a program that computes the net amount of a bank account based a transaction log from console input. 
    The transaction log format is shown as following:

D 100
W 200

    D means deposit while W means withdrawal.

    Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100

    Then, the output should be:

500
'''

deposit=0
while True:
    inp = input('Transaction log (D-deposit, W-withdrawal). Type \'q\' to exit: ').split(' ')
    if 'q' in inp:
        break
    else:
        if inp[0] == 'D':
            deposit+=int(inp[1])
        elif inp[0] == 'W':
            deposit-=int(inp[1])
print(deposit)

