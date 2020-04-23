import pytest, random, math
from ops import soma,sub,mult,div,resto,root

def test_soma():
    print("a testar a soma")
    a = float(random.random()*100)
    b = float(random.random()*100)

    if a < b:
        temp = a
        a = b
        b = temp
    
    assert (soma(a,a) == 2*a and soma(a,a) > 0)
    assert (soma(a,b) == a+b and soma(a,b) > 0)
    assert (soma(a,-a) == 0 )
    assert (soma(a,-b) == a-b and soma(a,-b) > 0)

    assert (soma(b,a) == b+a and soma(b,a) > 0)
    assert (soma(b,b) == 2*b and soma(b,b) > 0)
    assert (soma(b,-a) == b-a and soma(b,-a) < 0)
    assert (soma(b,-b) == 0)
    
    assert (soma(-a,a) == 0)
    assert (soma(-a,b) == b-a and soma(-a,b) < 0)
    assert (soma(-a,-a) == -2*a and soma(-a,-a) < 0)
    assert (soma(-a,-b) == -(a+b) and soma(-a,-b) < 0)

    assert (soma(-b,a) == a-b and soma(-b,a) > 0)
    assert (soma(-b,b) == 0)
    assert (soma(-b,-a) == -(a+b) and soma(-b,-a) <0)
    assert (soma(-b,-b) == -2*b and soma(-b,-b) < 0)

    assert soma(a,0) == a
    assert soma(b,0) == b
    assert soma(-a,0) == -a
    assert soma(-b,0) == -b
    assert soma(0,a) == a
    assert soma(0,b) == b
    assert soma(0,-a) == -a
    assert soma(0,-b) == -b

def test_sub():
    print("a testar a subtração")
    a = float(random.random()*100)
    b = float(random.random()*100)

    if a < b:
        temp = a
        a = b
        b = temp
    
    assert (sub(a,a) == 0)
    assert (sub(a,b) == a-b and sub(a,b) > 0)
    assert (sub(a,-a) == 2*a and sub(a,-a) > 0)
    assert (sub(a,-b) == a+b and sub(a,-b) > 0)

    assert (sub(b,a) == b-a and sub(b,a) < 0)
    assert (sub(b,b) == 0)
    assert (sub(b,-a) == b+a and sub(b,-a) >0)
    assert (sub(b,-b) == 2*b and sub(b,-b) > 0)
    
    assert (sub(-a,a) == -2*a and sub(-a,a) < 0)
    assert (sub(-a,b) == -(a+b) and sub(-a,b) < 0)
    assert (sub(-a,-a) == 0)
    assert (sub(-a,-b) == b-a and sub(-a,-b) < 0)

    assert (sub(-b,a) == -(b+a) and sub(-b,a) < 0)
    assert (sub(-b,b) == -2*b and sub(-b,b) < 0 )
    assert (sub(-b,-a) == a-b and sub(-b,-a) > 0)
    assert (sub(-b,-b) == 0)

    assert sub(a,0) == a
    assert sub(b,0) == b
    assert sub(-a,0) == -a
    assert sub(-b,0) == -b
    assert sub(0,a) == -a
    assert sub(0,b) == -b
    assert sub(0,-a) == a
    assert sub(0,-b) == b

def test_mult():
    print("a testar a multiplicação")

    a = float(random.random()*100)
    b = float(random.random()*100)

    if a < b:
        temp = a
        a = b
        b = temp
    
    assert (mult(a,a) == a*a and mult(a,a) > 0)
    assert (mult(a,b) == a*b and mult(a,b) > 0)
    assert (mult(a,-a) == -a*a and mult(a,-a) < 0)
    assert (mult(a,-b) == -b*a and mult(a,-b) < 0)

    assert (mult(b,a) == b*a and mult(b,a) > 0)
    assert (mult(b,b) == b*b and mult(b,b) > 0)
    assert (mult(b,-a) == b*-a and mult(b,-a) < 0)
    assert (mult(b,-b) == -b*b and mult(b,-b) < 0)
    
    assert (mult(-a,a) == -a*a and mult(-a,a) < 0)
    assert (mult(-a,b) == -a*b and mult(-a,b)  < 0)
    assert ( mult(-a,-a) == a*a and mult(-a,-a) > 0 )
    assert (mult(-a,-b) == a*b and mult(-a,-b) > 0 )

    assert (mult(-b,a) == -b*a and mult(-b,a) < 0)
    assert (mult(-b,b) == -b*b and mult(-b,b) < 0)
    assert (mult(-b,-a) == a*b and mult(-b,-a) > 0)
    assert (mult(-b,-b) == b*b and mult(-b,-b) > 0)

    assert mult(a,0) == 0
    assert mult(b,0) == 0
    assert mult(-a,0) == 0
    assert mult(-b,0) == 0
    assert mult(0,a) == 0
    assert mult(0,b) == 0
    assert mult(0,-a) == 0
    assert mult(0,-b) == 0

    assert mult(a,1) == a
    assert mult(b,1) == b
    assert mult(-a,1) == -a
    assert mult(-b,1) == -b
    assert mult(1,a) == a
    assert mult(1,b) == b
    assert mult(1,-a) == -a
    assert mult(1,-b) == -b


def test_div():
    print("a testar a divisão")

    a = float(random.random()*100)
    b = float(random.random()*100)

    if a < b:
        temp = a
        a = b
        b = temp
    
    assert (div(a,a) == 1)
    assert (div(a,b) == a/b and div(a,b) > 0)
    assert (div(a,-a) == -1)
    assert (div(a,-b) == -a/b and div(a,-b) < 0)

    assert (div(b,a) == b/a and div(b,a) > 0)
    assert (div(b,b) == 1)
    assert (div(b,-a) == -b/a and div(b,-a) < 0)
    assert (div(b,-b) == -1)
    
    assert (div(-a,a) == -1)
    assert (div(-a,b) == -a/b and div(-a,b) < 0)
    assert (div(-a,-a) == 1)
    assert (div(-a,-b) == a/b and div(-a,-b) > 0)

    assert (div(-b,a) == -b/a and div(-b,a) < 0)
    assert (div(-b,b) == -1)
    assert (div(-b,-a) == b/a and div(-b,-a) > 0)
    assert (div(-b,-b) == 1)

    assert div(a,0) == "error"
    assert div(b,0) == "error"
    assert div(-a,0) == "error"
    assert div(-b,0) == "error"
    assert div(0,a) == 0
    assert div(0,b) == 0
    assert div(0,-a) == 0
    assert div(0,-b) == 0

    assert div(a,1) == a
    assert div(b,1) == b
    assert div(-a,1) == -a
    assert div(-b,1) == -b
    assert div(1,a) == 1/a
    assert div(1,b) == 1/b
    assert div(1,-a) == -1/a
    assert div(1,-b) == -1/b

def test_resto():
    print("a testar o resto")

    a = float(random.random()*100)
    b = float(random.random()*100)

    if a < b:
        temp = a
        a = b
        b = temp
    
    assert resto(a,a) == 0
    assert resto(a,b) == a%b and resto(a,b) > 0
    assert resto(a,-a) == 0
    assert resto(a,-b) == a%-b and resto(a,-b) < 0

    assert resto(b,a) == b%a and resto(b,a) > 0
    assert resto(b,b) == 0
    assert resto(b,-a) == b%-a and resto(b,-a) < 0
    assert resto(b,-b) == 0
    
    assert resto(-a,a) == 0
    assert resto(-a,b) == -a%b and resto(-a,b) > 0
    assert resto(-a,-a) == 0
    assert resto(-a,-b) == -a%-b and resto(-a,-b) < 0

    assert resto(-b,a) == -b%a and resto(-b,a) > 0
    assert resto(-b,b) == 0
    assert resto(-b,-a) == -b%-a and resto(-b,-a) < 0
    assert resto(-b,-b) == 0

    assert resto(a,0) == "error"
    assert resto(b,0) == "error"
    assert resto(-a,0) == "error"
    assert resto(-b,0) == "error"
    assert resto(0,a) == 0
    assert resto(0,b) == 0
    assert resto(0,-a) == 0
    assert resto(0,-b) == 0

    assert resto(a,1) == a%1
    assert resto(b,1) == b%1
    assert resto(-a,1) == -a%1
    assert resto(-b,1) == -b%1
    assert resto(1,a) == 1
    assert resto(1,b) == 1
    assert resto(1,-a) == 1%-a
    assert resto(1,-b) == 1%-b



def test_root():
    print("a testar a raíz quadrada")
    a = float(random.random()*100)

    assert root(a) == math.sqrt(a)