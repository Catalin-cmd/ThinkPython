"""
Scenario
Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

The figure illustrates the rule used by the builders:



Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

Test your code using the data we've provided.
"""

blocks = int(input("Enter the number of blocks: "))
height = 0
counter = 0
while blocks> 0:
    counter+=1 #this will count how many blocks we've used
    blocks-=counter #this will count how many blocks we have left
    height+=1 #this is the actual height of the pyramid
if blocks<0: #if the row is not completed the height will not be added
        height-=1
print("The height of the pyramid:", height)
