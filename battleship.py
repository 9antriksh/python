#!/usr/bin/env python

#BattleShip Game
from random import randint

#Creating the Board
board=[]
for i in range(10):
    board.append(["O"]*10)

#Printing the Board
def pb(b):
    for rb in b:
        print "   "+" ".join(rb)

print "-"*25 + "\n" + "| Welcome to Battleship |" + "\n"+"-"*25
pb(board)

#Cordinates of BattleShip
bcor=[[randint(0,9)],[randint(0,9)]]
shipcount=0
flag = False
while shipcount < 3:
    temprow=randint(0,9)
    tempcol=randint(0,9)
    for v in range(len(bcor[1])):
        if temprow==bcor[0][v] and tempcol==bcor[1][v]:
            flag = True
            break
    if flag==True:
        continue
    else:
        bcor[0].append(temprow)
        bcor[1].append(tempcol)
        shipcount+=1  
print bcor
       
#Attack Begins
for turn in range(5):
    found=False
    print "Turn Left:"+str(5-turn)
    grow=int(raw_input("Enter Missile Cordinates X:"))
    gcol=int(raw_input("Enter Missile Cordinates Y:"))
#check for integer remaining
   
    for c in range(4):
        if grow==bcor[0][c] and gcol==bcor[1][c]:
            found=True
            break
    
    if found and board[grow][gcol]=="O":
        board[grow][gcol]="X"
        print "\n"+"BOOM!!!  Ship Destroyed"
        shipcount-=1
    elif shipcount == -1:
        break
    elif (grow not in range(0,9) or gcol not in range(0,9)):
        print "Damn!!! Out of Range Target"
    elif board[grow][gcol]=="#" or board[grow][gcol]=="X":
        print "Missile wasted Cordinates already BOMBED!"
    else:
        print "----No Target Found----"
        board[grow][gcol]="#"
    pb(board)
    print "Ship Left:"+str(shipcount+1)
print "Game Over."
