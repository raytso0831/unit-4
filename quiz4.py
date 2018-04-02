#Ray Tso
#4/2/18
#quiz.py

def count(num1):
    for i in range(1,num1+1):
        print(i)

count(7)

def excitedPrint(string):
    print(string.upper(), '!!!')

excitedPrint("i love <3 comp programming")

def firstLetter(word):
    for i in word:
        return(i)
        
print(firstLetter("Ray"))

def repeats(num1,num2,num3):
    if num1 == num2 or num2 == num3 or num1 == num3:
        return True
    else:
        return False



print(repeats(3,4,5))
print(repeats(1,0,1))
