import math

def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    if b == 0:
        return "error"
    else:
        return a/b

def resto(a,b):
    if b == 0:
        return "error"
    else:
        return a%b

def root(a):
    return math.sqrt(a)