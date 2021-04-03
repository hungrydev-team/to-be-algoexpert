import pytest

from hash_table import NoSuchKeyException
from hash_table import HashTable


def test_lookup(table: HashTable):
    table.insert(11, 26)
    assert table.lookup(11) == 26


def test_remove(table: HashTable):
    table.insert(1, 2)
    table.remove(1)
    with pytest.raises(NoSuchKeyException):
        table.remove(1)

    with pytest.raises(NoSuchKeyException):
        table.lookup(1)


# def test_insert_multiple(table: HashTable):
#     table.insert(1, 2)
#     assert table.lookup(1) == 2
#     table.insert(1, 3)
#     assert table.lookup(1) == 3
def test_insert():
    assert False
