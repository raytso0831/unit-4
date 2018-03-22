#Ray Tso
#3/22/18
#monkeyBanana.py- Best game ever

from ggame import *

if __name__=='__main__':
    
    
    #colors
    green=Color(0x006600,1)
    
    jungleBox=RectangleAsset(1000,1000,LineStyle(1,green),green)
    
    Sprite(jungleBox)
    
    App().run()
