# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

#the intervals in which the bomb can be (on the X and Y axes)
xMin , xMax = 0, w-1
yMin , yMax = 0, h-1

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    #Update the bomb's Y interval
    if 'U' in bomb_dir:
        yMax = y0-1
    elif 'D' in bomb_dir:
        yMin = y0+1
    else:
        yMax  = yMin = y0

    #Update the bomb's X interval
    if 'R' in bomb_dir:
        xMin = x0+1
    elif 'L' in bomb_dir:
        xMax = x0-1
    else:
        xMax = xMin = x0
    
    #Send Batman to the middle of the bomb's intervals
    y0 = int((yMax+yMin)/2)
    x0 = int((xMax+xMin)/2)
    print(x0,y0)
