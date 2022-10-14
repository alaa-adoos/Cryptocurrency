import pytest
from crypto.crypto import crypto
def test_get_name(set_data):
    actual = crypto.get_name()
    expected = "Bitcoin"
    assert actual == expected
@pytest.mark.skip("todo")
#the price change every second so the test need update before you do it
def test_get_price(set_data):
    actual = crypto.get_price()
    expected = 19310.82
    assert round(actual) == round(expected)
def test_max_supply(set_data):
    actual = crypto.get_max_supply()
    expected = 21000000
    assert actual == expected
def test_categories(set_data):
    actual = crypto.get_categories()
    expected = "mineable - pow - sha-256"
    assert actual == expected
def test_rank(set_data):
    actual = crypto.get_rank()
    expected = 1
    assert actual == expected
@pytest.fixture
def set_data():
    crypto.set_symbol('BTC')
    crypto.get_data()
    crypto.get_coin()