import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = int(25) , int(33)
# n = int(input())  # maximum number of turns before game over.
# x0, y0 = [int(i) for i in input().split()]
x0 , y0 = int(5) , int(15)
# game loop
# while True:

    # bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
while w-x0 !=0:
    if  w -x0 > 0:
        x0 +=1
    elif w -x0 < 0:
        x0 -=1
    elif w - x0 == 0:
        for i in range (10):
            row = (i*"x")
            print(row)
            x0 -=1
    print(f"width: {w - x0}, x: {x0}")

    #     y0 +=4
    #     # y0 +=7   #tower
    # # elif bomb_dir == "U":
    # #     y0 -=6
    # elif bomb_dir == "R":
    #     x0 +=2
    # # elif bomb_dir == "L":
    # #     x0 -=7
    # elif bomb_dir == "D":
    #     y0 +=7
    # # elif bomb_dir == "DL":
    # #     x0 +=1
    # #     y0 -=1
    # elif bomb_dir == "UR":
    #     x0 +=4
    #     y0 -=2
    # # elif bomb_dir == "UL":
    # #     x0 -=6
    # #     y0 -=6
print(f"width: {w}, height: {h}")
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # A single line providing the move to be made: U UR R DR D DL L or UL
    # print(x0,  y0)
    # print(bomb_dir)

    # the location of the next window Batman should jump to.
