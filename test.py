import pytest
from main import somar
from main import sub

def test_somar():
    assert somar(2,3)==5

def test_sub():
    assert sub(10,8)==2