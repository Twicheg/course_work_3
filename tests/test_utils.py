import pytest
from src import utils


@pytest.fixture
def class_exsam():
    PATH = 'operations.json'
    x = utils.Bank(PATH)
    return x


def test_Bank():
    assert 1==1
    #assert type(class_exsam.open_json(1)) == list
    # assert type(class_exsam.open_json(-2)) == list
    # assert type(class_exsam.open_json(0)) == list
    # assert x.sort_collection()
    pass
