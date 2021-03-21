'''
Question 21:

    A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
    The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2

    The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. 
    If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2

    Then, the output of the program should be:

2
'''
import math

x,y=0,0

while True:
    inp = input('Robot moves: ').split()
    if not inp:
        break
    if inp[0] == 'UP':          #command here
        x+=int(inp[1])          #unit here
    elif inp[0] =='DOWN':
        x-=int(inp[1])
    elif inp[0] == 'LEFT':
        y+=int(inp[1])
    elif inp[0] == 'RIGHT':
        y-=int(inp[1])

print(round(math.sqrt((x**2+y**2))))
