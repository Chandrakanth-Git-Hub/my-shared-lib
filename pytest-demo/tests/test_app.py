import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import add, is_even


def test_add():
    assert add(2, 3) == 5

def test_is_even_true():
    assert is_even(4) == True

def test_is_even_false():
    assert is_even(3) == False
