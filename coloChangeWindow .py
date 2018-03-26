#Ray Tso
#3/19/18
#colorChangeWindow.py
from random import randint
from ggame import*
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
        color=black
    
    else:
        color=blue

    line = LineStyle(1,color)
    square = RectangleAsset(1000,1000,line,color)
    Sprite(square)

    

App().listenMouseEvent('click',mouseClick)
App().run()