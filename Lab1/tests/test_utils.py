import pytest
from src.utils import add, substract

def test_add_positive_numbers():
    assert add(1, 2, 3) == 6   
    assert add(10, 2, 51, 7) == 70
    assert add(0, 0, 0) == 0
    
def test_add_negative_numbers():
    assert add(-1, -2, -3) == -6
    assert add(-10, -2, -51, -7) == -70
    assert add(-5, 5) == 0

def test_substract_positive_numbers():
    assert substract(10, 2, 3) == 5   
    assert substract(100, 20, 30, 10) == 40
    assert substract(0, 0, 0) == 0
    
def test_substract_negative_numbers():
    assert substract(-10, -2, -3) == -5
    assert substract(-100, -20, -30, -10) == -40
    assert substract(-5, 5) == -10
    
def test_substract_mixed_numbers():
    assert substract(10, -2, 3) == 9
    assert substract(-10, 2, -3) == -9
    assert substract(0, -5, 5) == 0
    
def test_add_no_arguments():
    assert add() == 0

def test_substract_single_argument():
    assert substract(10) == 10
    assert substract(-5) == -5
    assert substract(0) == 0
