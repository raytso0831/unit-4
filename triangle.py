#Ray Tso
#4/1/18
#triangle.py


from math import sqrt

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))
x3 = float(input('Enter x3: '))
y3 = float(input('Enter y3: '))


def distance(a, b, c, d):
    return (sqrt(((d-c)**2)+((b-a)**2)))
    
sideA = distance(x1, x2, y1, y2)
sideB = distance(x2, x3, y2, y3)
sideC = distance(x3, x1, y3, y1)

def semiperimeter():
    return 0.5*(sideA+sideB+sideC)

def area():
    return sqrt(semiperimeter()*(semiperimeter()-sideA)*(semiperimeter()-sideB)*(semiperimeter()-sideC))

print('The area is',area())


