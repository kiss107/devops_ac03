import pytest

from com.kuma.test.principal import *

def test_somar():
        assert somar(5,6) == 11

def test_subtrair():
        assert subtrair(8,3) == 5 

def test_multiplicacao():
        assert multiplicacao(50,8)

def test_divisao():
        assert divisao(60,6)