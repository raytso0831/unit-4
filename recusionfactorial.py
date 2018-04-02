#Ray Tso
#4/1/18
#recusionfactorial.py


def factorial(n):
    if n == 0:
        return 1
    else:
        return (n*factorial(n-1))
