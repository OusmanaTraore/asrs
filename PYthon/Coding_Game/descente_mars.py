import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    

# game loop
while True:
    
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
    print("V=", v_speed , file=sys.stderr, flush=True)
    print("Y=", y , file=sys.stderr, flush=True)
    
    v_ab= - v_speed 
    if  v_ab > 40:
        print("Vitesse  KO > 40 :" , v_speed, file=sys.stderr, flush=True)
        print("0 0")
    elif  v_ab < 40:
        print("Vitesse  OK < 40 :" , v_speed, file=sys.stderr, flush=True)
        print("0 4")
 
    print("0 3")
      
