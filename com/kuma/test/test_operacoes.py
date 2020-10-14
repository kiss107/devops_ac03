import pytest

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicacao(n1,n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

def test_soma():
    assert somar(4,6) == 10

def test_subtrair():
    assert subtrair(10,5) == 5

def test_multiplicacao():
    assert multiplicacao(20,3) == 60

def  test_divisao():
    assert divisao(20,5) == 4