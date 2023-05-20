import pytest
from src import utils
from src import main

PATH = 'operations.json'
def test_Bank():
    assert type(utils.Bank(PATH).open_json(1)) == list
    assert type(utils.Bank(PATH).open_json(-2)) == list
    assert type(utils.Bank(PATH).open_json(0)) == str
    assert utils.Bank(PATH).sort_collection([], 1) == 'empty python_list'
    assert main.main(0) == 'zero-PATH incoming'
    assert main.main(PATH) == 'complited'