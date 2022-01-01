import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, x, y = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    orientation =""
    if light_y - y > 0:
        orientation = "S"
        y +=1
    elif light_y -y < 0:
        orientation = "N"
        y -=1

    if light_x - x > 0:
        orientation += "E"
        x +=1
    elif light_x -x < 0:
        orientation += "W"
        x -=1
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(orientation)
