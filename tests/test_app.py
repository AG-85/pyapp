import src.pyapp.app as app
import pytest


def test_addition():
    assert app.addition([1,4,5]) == 10
    #assert app.addition([-1,1,0]) == 0


def test_subtraction():
    assert app.subtraction([5,3,2]) == 0
    #assert app.subtraction([-9,1,0]) == -10


def test_multiplication():
    assert app.multiplication([1,4,5]) == 20
    #assert app.multiplication([-1,1,0]) == 0


def test_division():
    assert app.division([1,4,5]) == 0.05
    #assert app.division([-1,-2,-5]) == -0.1






