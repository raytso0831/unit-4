#Ray Tso
#3/9/18
#functionDemo.py

def hw():
    print("hello, world")
    

def double(thingToDouble):
    print(thingToDouble * 2)

def bigger(a,b):
    if a>b:
        print(a)
    else:
        print(b)

def slope(x1, y1, x2, y2):
    print((y2 - y1)/(x2 - x1))

slope(1,1,2,2)
slope(True,True,False,False) #sketchy
#bigger(3,4)
#bigger(4,3)
#bigger("Smedinghoff","Sam")
#bigger(True,False)
#double(12) #test of double function
#double('w') #test of double with a string input
#double(False) #test of double with a boolean