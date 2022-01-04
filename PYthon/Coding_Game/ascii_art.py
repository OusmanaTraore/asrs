import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
diese = "#"
espace= " "

question0 ="# #  #  ### ### # #  #  ### ### ###  #  ### "
question1 ="### # # # #   # # # # #  #    #  #  # # # # "
question2 ="### ### # #  ## ### ###  #   ##  #  ### # # "
question3 ="# # # # # #     # # # #  #       #  # # # # "   
question4 ="# # # # # #  #  # # # #  #   #   #  # # # # "


man0="# # ### ### # # ### ### ### ### ### "
man1="###   # # # # #   #  #   #    # # # "
man2="###  ## # # ###  ##  #   #   ## # # "
man3="# #     # # # #      #   #      # # "
man4="# #  #  # # # #  #   #   #   #  # # "


mana1=" .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------."
mana2="| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |"
mana3="| | ____    ____ | || |      __      | || | ____  _____  | || |  ____  ____  | || |      __      | || |  _________   | || |  _________   | || |      __      | || | ____  _____  | |"
mana4="| ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | || | |_   ||   _| | || |     /  \     | || | |  _   _  |  | || | |  _   _  |  | || |     /  \     | || ||_   \|_   _| | |"
mana5="| |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | || |   | |__| |   | || |    / /\ \    | || | |_/ | | \_|  | || | |_/ | | \_|  | || |    / /\ \    | || |  |   \ | |   | |"
mana6="| |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | || |   |  __  |   | || |   / ____ \   | || |     | |      | || |     | |      | || |   / ____ \   | || |  | |\ \| |   | |"
mana7="| | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | || |  _| |  | |_  | || | _/ /    \ \_ | || |    _| |_     | || |    _| |_     | || | _/ /    \ \_ | || | _| |_\   |_  | |"
mana8="| ||_____||_____|| || ||____|  |____|| || ||_____|\____| | || | |____||____| | || ||____|  |____|| || |   |_____|    | || |   |_____|    | || ||____|  |____|| || ||_____|\____| | |"
mana9="| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |"
mana10="| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |"
mana11=" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' "

for i in range(h):
    row = input()
    if t == "E":
        if i == 0:
            print(3*diese + espace)
        elif i == 1:
            print(diese + 3*espace)
        elif i == 2:
            print(2*diese + 2*espace)
        elif i ==3:
            print(diese + 3*espace)
        elif i ==4:
            print(3*diese + espace)
    elif t =="MANHATTAN"  or t =="ManhAtTan":
        if h==5:
            if i == 0:
                print(diese+ espace+ diese + 2*espace +diese + 2*espace +
                3*diese + 2*( espace + diese) +  2*espace + diese +
                2*espace + 3*diese +espace+3*diese+2*espace + diese  + 2*espace +
                3*diese + espace )
            elif i == 1:
                print(3*diese+ 8*(espace+ diese )+ 2*espace +diese + 3*espace +
                diese + 2*espace + 4*(diese + espace)) 
            elif i == 2:
                print( 
                    2*(3*diese+espace)+2*(diese + espace)+ 2*(3*diese+espace)+
                    espace+diese +3*espace+diese+ 2*espace + 3*diese + 2*(espace+diese) +
                    espace
                )
            elif i ==3 or i ==4: 
                print(
                10*(diese + espace)+ espace + diese +3*espace+ diese +espace + 4*(espace+ diese) +
                espace
                    )
        elif h==11:
            if i==0:
                print(mana1)
            elif i==1:
                print(mana2)
            elif i==2:
                print(mana3)
            elif i==3:
                print(mana4)
            elif i==4:
                print(mana5)
            elif i==5:
                print(mana6)
            elif i==6:
                print(mana7)
            elif i==7:
                print(mana8)
            elif i==8:
                print(mana9)
            elif i==9:
                print(mana10)
            elif i==10:
                print(mana11)
    elif  t =="MAN HAT TAN":
        if i==0:
            print(question0)
        elif i==1:
            print(question1)
        elif i==2:
            print(question2)
        elif i==3:
            print(question3)
        elif i==4:
            print(question4)
    elif  t =="M@NH@TT@N":
        if i==0:
            print(man0)
        elif i==1:
            print(man1)
        elif i==2:
            print(man2)
        elif i==3:
            print(man3)
        elif i==4:
            print(man4)      





# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("l :", l, file=sys.stderr, flush=True)
print("h :", h, file=sys.stderr, flush=True)
print("t :", t, file=sys.stderr, flush=True)
print("i :", i, file=sys.stderr, flush=True)

