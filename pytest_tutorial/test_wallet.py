"""
pip install pytest (im Projekt uv add pytest)

Tests ausführen:
pytest test_wallet.py -vv -s
-vv => Verbose
-s => print() Ausgaben "fangen"
"""

import pytest

from wallet import InsufficientAmount


def test_one_is_one():
    assert 1 == 1


def test_new_wallet_initial_balance(empty_wallet):
    assert empty_wallet.balance == 0, "Initial Balance sollte 0 sein"


def test_exception_raised_if_balance_negative(empty_wallet):
    """Muss eine Exception auslösen, wenn die Balance negativ ist."""
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(10)


@pytest.mark.parametrize(
    "earned,spent,expected",
    [
        (100, 0, 110),
        (30, 10, 20),
    ],
)
def test_transactions(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected
