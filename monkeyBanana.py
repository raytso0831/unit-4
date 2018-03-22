#Ray Tso
#3/22/18
#monkeyBanana.py- Best game ever

from ggame import *

#constants
ROWS=200
COLS=40
CELL_SIZE=20

def moveRight(event):
    monkey.x+=CELL_SIZE
def moveLeft(event):
    monkey.x-=CELL_SIZE
def moveUp(event):
    monkey.y-=CELL_SIZE
def moveDown(event):
    monkey.y+=CELL_SIZE
    
    
if __name__=='__main__':
    
    
    #colors
    green=Color(0x006600,1)
    brown=Color(0x8B4513,1)
    
    jungleBox=RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    monkeyBox=RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    
    Sprite(jungleBox)
    monkey=Sprite(monkeyBox)

    App().listenKeyEvent('keydown','right arrow', moveRight)
    App().listenKeyEvent('keydown','left arrow', moveLeft)
    App().listenKeyEvent('keydown','up arrow', moveUp)
    App().listenKeyEvent('keydown','down arrow', moveDown)

    App().run()
