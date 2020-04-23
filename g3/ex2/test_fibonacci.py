import pytest
from fibonacci import fibonacci

def test_inferior_1():
    print("Testa comportamento com n < 1")
    assert fibonacci(0) == [0]
    assert fibonacci(-1) == []

def test_n_1():
    print("Testa comportamento com n = 1")
    assert fibonacci(1) == [0,1]

def test_n_2():
    print("Testa comportamento com n = 2")
    assert fibonacci(2) == [0,1,1]

def test_n_5():
    print("Testa comportamento com n = 5")
    assert fibonacci(5) == [0,1,1,2,3,5]

def test_n():
    print("Testa comportamento de n=0 até n=100")
    for n in range(0,101):
        assert len(fibonacci(n)) == n+1