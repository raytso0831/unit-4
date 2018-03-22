#Ray Tso
#3/22/18
#monkeyBanana.py- Best game ever

from ggame import *

#constants
ROWS=100
COLS=100
CELL_SIZE=100


if __name__=='__main__':
    
    
    #colors
    green=Color(0x006600,1)
    
    jungleBox=RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    
    Sprite(jungleBox)
    
    App().run()
