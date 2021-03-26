from data_structure.hash_table import HashTable


def test_insert():
    hash_table = HashTable()
    hash_table.insert(1, 2)
    assert hash_table.lookup(1) == 2


def test_remove():
    hash_table = HashTable()
    hash_table.insert(1, 2)
    assert hash_table.remove(1) == 2
    hash_table.insert(1, 2)
    assert hash_table.lookup(1) == 2
