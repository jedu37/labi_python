import pytest, random
from ops import soma,sub,mult,div,resto,root

def test_soma():
    print("a testar a soma")
    a = random.random()*100
    b = random.random()*100

    if a < b:
        temp = a
        a = b
        b = temp
    
    assert soma(a,a) == 2*a and soma(a,a) > 0
    assert soma(a,b) == a+b and soma(a,b) < 0
    assert soma(a,-a) == 0 
    assert soma(a,-b) == a-b and soma(a,-b) > 0

    assert soma(b,a) == b+a and soma(b,a) > 0
    assert soma(b,b) == 2*b and soma(b,b) > 0
    assert soma(b,-a) == b-a and soma(b,-a) < 0
    assert soma(b,-b) == 0
    
    assert soma(-a,a) == 0
    assert soma(-a,b) == b-a and soma(-a,b) < 0
    assert soma(-a,-a) == -2*a and soma(-a,-a) < 0
    assert soma(-a,-b) == -(a+b) and soma(-a,-b) < 0

    assert soma(-b,a) == a-b and soma(-b,a) > 0
    assert soma(-b,b) == 0
    assert soma(-b,-a) == -(a+b) and soma(-b,-a) >0
    assert soma(-b,-b) == -2*a and soma(-b,-b) < 0

def test_sub():
    print("a testar a subtração")
    a = random.random()*100
    b = random.random()*100

    if a < b:
        temp = a
        a = b
        b = temp
    
    assert sub(a,a) == 0
    assert sub(a,b) == a-b and sub(a,b) > 0
    assert sub(a,-a) == 2*a and sub(a,-a) > 0
    assert sub(a,-b) == a+b and sub(a,-b) > 0

    assert sub(b,a) == b-a and sub(b,a) < 0
    assert sub(b,b) == 0
    assert sub(b,-a) == b+a and sub(b,-a) >0
    assert sub(b,-b) == 2*b and sub(b,-b) > 0
    
    assert sub(-a,a) == 2*a and sub(-a,a) < 0
    assert sub(-a,b) == 2*a and sub(-a,b) < 0
    assert sub(-a,-a) == 0
    assert sub(-a,-b) == b-a and sub(-a,-b) < 0

    assert sub(-b,a) == -(b+a) and sub(-b,a) < 0
    assert sub(-b,b) == -2*b and sub(-b,b) < 0 
    assert sub(-b,-a) == 2*a and sub(a,a) ==
    assert sub(-b,-b) == 0

def test_mult():
    print("a testar a multiplicação")

    a = random.random()*100
    b = random.random()*100

    if a < b:
        temp = a
        a = b
        b = temp
    
    assert soma(a,a) == 2*a and soma(a,a) > 0
    assert soma(a,b) == a+b and soma(a,b) < 0
    assert soma(a,-a) == 0 and soma(a,a) ==
    assert soma(a,-b) == 2*a and soma(a,a) ==

    assert soma(b,a) == 2*a and soma(a,a) ==
    assert soma(b,b) == 2*a and soma(a,a) ==
    assert soma(b,-a) == 2*a and soma(a,a) ==
    assert soma(b,-b) == 2*a and soma(a,a) ==
    
    assert soma(-a,a) == 2*a and soma(a,a) ==
    assert soma(-a,b) == 2*a and soma(a,a) ==
    assert soma(-a,-a) == 2*a and soma(a,a) ==
    assert soma(-a,-b) == 2*a and soma(a,a) ==

    assert soma(-b,a) == 2*a and soma(a,a) ==
    assert soma(-b,b) == 2*a and soma(a,a) ==
    assert soma(-b,-a) == 2*a and soma(a,a) ==
    assert soma(-b,-b) == 2*a and soma(a,a) ==

def test_div():
    print("a testar a divisão")

    a = random.random()*100
    b = random.random()*100

    if a < b:
        temp = a
        a = b
        b = temp
    
    assert soma(a,a) == 2*a and soma(a,a) > 0
    assert soma(a,b) == a+b and soma(a,b) < 0
    assert soma(a,-a) == 0 and soma(a,a) ==
    assert soma(a,-b) == 2*a and soma(a,a) ==

    assert soma(b,a) == 2*a and soma(a,a) ==
    assert soma(b,b) == 2*a and soma(a,a) ==
    assert soma(b,-a) == 2*a and soma(a,a) ==
    assert soma(b,-b) == 2*a and soma(a,a) ==
    
    assert soma(-a,a) == 2*a and soma(a,a) ==
    assert soma(-a,b) == 2*a and soma(a,a) ==
    assert soma(-a,-a) == 2*a and soma(a,a) ==
    assert soma(-a,-b) == 2*a and soma(a,a) ==

    assert soma(-b,a) == 2*a and soma(a,a) ==
    assert soma(-b,b) == 2*a and soma(a,a) ==
    assert soma(-b,-a) == 2*a and soma(a,a) ==
    assert soma(-b,-b) == 2*a and soma(a,a) ==

def test_resto():
    print("a testar o resto")

    a = random.random()*100
    b = random.random()*100

    if a < b:
        temp = a
        a = b
        b = temp
    
    assert soma(a,a) == 2*a and soma(a,a) > 0
    assert soma(a,b) == a+b and soma(a,b) < 0
    assert soma(a,-a) == 0 and soma(a,a) ==
    assert soma(a,-b) == 2*a and soma(a,a) ==

    assert soma(b,a) == 2*a and soma(a,a) ==
    assert soma(b,b) == 2*a and soma(a,a) ==
    assert soma(b,-a) == 2*a and soma(a,a) ==
    assert soma(b,-b) == 2*a and soma(a,a) ==
    
    assert soma(-a,a) == 2*a and soma(a,a) ==
    assert soma(-a,b) == 2*a and soma(a,a) ==
    assert soma(-a,-a) == 2*a and soma(a,a) ==
    assert soma(-a,-b) == 2*a and soma(a,a) ==

    assert soma(-b,a) == 2*a and soma(a,a) ==
    assert soma(-b,b) == 2*a and soma(a,a) ==
    assert soma(-b,-a) == 2*a and soma(a,a) ==
    assert soma(-b,-b) == 2*a and soma(a,a) ==

def test_root():
    print("a testar a raíz quadrada")