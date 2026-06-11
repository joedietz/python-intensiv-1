import pytest

from wallet import Wallet


@pytest.fixture
def empty_wallet():
    """Ein pytest fixture kann als Parameter in Testfunktionen übernommen werden."""
    return Wallet()
