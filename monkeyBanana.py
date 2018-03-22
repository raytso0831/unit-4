#Ray Tso
#3/22/18
#monkeyBanana.py- Best game ever

from ggame import *
from random import randint

#constants
ROWS=20
COLS=40
CELL_SIZE=20

def moveRight(event):
    monkey.x+=CELL_SIZE
    if monkey.x==banana.x and monkey.y==banana.y:
        moveBanana()
        data['score']+=10
        print(data['score'])


def moveLeft(event):
    if monkey.x>0:
        monkey.x-=CELL_SIZE
        if monkey.x==banana.x and monkey.y==banana.y:
             moveBanana()
             data['score']+=10
             print(data['score'])

    
def moveUp(event):
        if monkey.x>0:
            monkey.y-=CELL_SIZE
            if monkey.x==banana.x and monkey.y==banana.y:
             moveBanana()
             data['score']+=10
            print(data['score'])


def moveDown(event):
    monkey.y+=CELL_SIZE
    if monkey.x==banana.x and monkey.y==banana.y:
             moveBanana()
             data['score']+=10
             print(data['score'])

    
    
def moveBanana():
    banana.x=randint(0,COLS-1)*CELL_SIZE
    banana.y=randint(0,COLS-1)*CELL_SIZE


if __name__=='__main__':
    
    #hold variables in a dictionary
    data={}
    data['score']=0
    
    
    #colors
    green=Color(0x006600,1)
    brown=Color(0x8B4513,1)
    yellow=Color(0XFFFF00,1)
    
    jungleBox=RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    monkeyBox=RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananaBox=RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    
    Sprite(jungleBox)
    monkey=Sprite(monkeyBox)
    banana=Sprite(bananaBox,(CELL_SIZE*COLS/2, CELL_SIZE*ROWS/2))
    
    
    App().listenKeyEvent('keydown','right arrow', moveRight)
    App().listenKeyEvent('keydown','left arrow', moveLeft)
    App().listenKeyEvent('keydown','up arrow', moveUp)
    App().listenKeyEvent('keydown','down arrow', moveDown)

    App().run()
