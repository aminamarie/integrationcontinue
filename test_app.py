# test_app.py
from app import addition, soustraction

def test_addition():
    assert addition(2, 3) == 5

def test_soustraction():
    assert soustraction(5, 2) == 2
