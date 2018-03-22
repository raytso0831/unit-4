#Ray Tso
#3/19/18
#colorChangeWindow.py
from random import randint
from g game import*
def mouseClick(event):
    
    red=Color(0xFF0000,1) #this is the color red
    green=Color(0x00FF00,1)
    blue=Color(0x0000FF,1)
    black=Color(0x000000,1)
    num=randint(1,4)

if num==1:
    color= red

elif num==2:
    color=green
    
elif num==3:
    color=blue

else:
    color=black

Outline=LineStyle(1, color)
Square=SquareAsset(1000,1000,Outline,color) #width, height, outline, fill
