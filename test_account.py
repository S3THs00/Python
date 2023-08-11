import pytest
from account import Account

def test_init():
    account = Account("John")
    assert account.get_name() == "John"
    assert account.get_balance() == 0.0

def test_deposit():
    account = Account("Alice")
    assert account.deposit(100) is True
    assert account.get_balance() == 100.0

def test_withdraw():
    account = Account("Bob")
    account.deposit(200)
    assert account.withdraw(150) is True
    assert account.get_balance() == 50.0
    assert account.withdraw(100) is False  # Cannot withdraw more than balance
    assert account.withdraw(0) is False    # Cannot withdraw zero amount
    assert account.withdraw(-50) is False  # Cannot withdraw negative amount
