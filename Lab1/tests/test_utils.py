import pytest
from src.utils import add, substract, multiply, divide

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

def test_multiply_positive_numbers():
    assert multiply(2, 3, 4) == 24
    assert multiply(1, 5, 10) == 50
    assert multiply(0, 100, 200) == 0

def test_multiply_negative_numbers():
    assert multiply(-2, -3, -4) == -24
    assert multiply(-1, -5, -10) == -50
    assert multiply(-1, 5, -10) == 50

def test_multiply_mixed_numbers():
    assert multiply(2, -3, 4) == -24
    assert multiply(-1, 5, 10) == -50
    assert multiply(1, -5, -10) == 50   
    
def test_multiply_single_argument():
    assert multiply(10) == 10
    assert multiply(-5) == -5
    assert multiply(0) == 0
    
def test_multiply_no_arguments():
    with pytest.raises(IndexError):
        multiply()
    
def test_divide_positive_numbers():
    assert divide(100, 2, 5) == 10
    assert divide(50, 5, 2) == 5
    assert divide(0, 1, 2) == 0
    
def test_divide_negative_numbers():
    assert divide(-100, -2, -5) == -10
    assert divide(-50, -5, -2) == -5
    assert divide(-100, 2, -5) == 10
    
def test_divide_mixed_numbers():
    assert divide(100, -2, 5) == -10
    assert divide(-50, 5, -2) == 5
    assert divide(100, -5, -2) == 10
    
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(100, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(0, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(50, 5, 0)
        
def test_divide_single_argument():
    assert divide(10) == 10
    assert divide(-5) == -5
    assert divide(0) == 0
    
def test_divide_no_arguments():
    with pytest.raises(IndexError):
        divide()

def test_divide_float_numbers():
    assert divide(5.0, 2.0) == 2.5
    assert divide(-5.0, 2.0) == -2.5
    assert divide(5.0, -2.0) == -2.5
    assert divide(-5.0, -2.0) == 2.5

def test_divide_resulting_in_float():
    assert divide(7, 2) == 3.5
    assert divide(10, 4) == 2.5
    assert divide(1, 3) == pytest.approx(0.3333, rel=1e-4)
