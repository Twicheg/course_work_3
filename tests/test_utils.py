import pytest
from src import utils

PATH = 'operations.json'
def test_Bank():
    assert 1 == 1
    assert type(utils.Bank(PATH).open_json(1)) == list
    assert type(utils.Bank(PATH).open_json(-2)) == list
    assert type(utils.Bank(PATH).open_json(0)) == str
    assert utils.Bank(PATH).sort_collection([], 1) == 'empty python_list'
