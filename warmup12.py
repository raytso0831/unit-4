#Ray Tso
#3/29/18
#warmup12.py

def GCF(num1,num2):
    for i in range(num1,0,-1):
        if num1%i == 0 and num2%i == 0:
            return i

print(GCF(12,16))
