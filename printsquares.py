#Ray Tso
#3/28/18
#printsquare.py

def printSquares(num1,num2):
    for i in range(1,num1+1):
        print('+--'*num2+'+')
        print('|  '*num2+'|')
    print('+--'*num2+'+')
    
printSquares(2,4)
