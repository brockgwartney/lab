import pytest
from account import *

def test__init__():
    John = Account('John')
    assert John.get_balance() == 0
    assert John.get_name() == 'John'

def test_deposit():
    Ted = Account('Ted')
    assert Ted.deposit(0) == False
    assert Ted.deposit(15) == True

def test_withdraw():
    Phil = Account('Phil')
    assert Phil.withdraw(10) == False
    Phil.deposit(1000)
    assert Phil.deposit(10) == True

