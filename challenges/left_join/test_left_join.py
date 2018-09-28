from .left_join import left_join, HashTable
import pytest


def test_empty_table_set_works():
    """Test set works for an empty hash table"""
    ht = HashTable()
    ht.set('Potato', 'Head')
    assert ht.get('Potato') == 'Head'


def test_get_empty_hash():
    """Test get doesn't work if table empty"""
    ht = HashTable()
    assert ht.get('Potato') == 'Value not in table'


def test_remove_happy_path():
    """Test remove on a small ht"""
    ht = HashTable()
    ht.set('Potato', 'Head')
    assert ht.remove('Potato') == 'True'


def test_remove_empty_ht():
    """Test remove on empty ht"""
    ht = HashTable()
    assert ht.remove('Potato') == 'False'


def test_all_values_correspond():
    ht_synomym = HashTable()
    ht_antonym = HashTable()
    ht_synomym.set('Happy', 'Joyful')
    ht_antonym.set('Happy', 'Sad')
    ht_synomym.set('Sad', 'Sorrowful')
    ht_antonym.set('Sad', 'Happy')
    assert left_join(ht_synomym, ht_antonym) == [['Sad', 'Sorrowful', 'Happy'], ['Happy', 'Joyful', 'Sad']]


def test_extra_in_synonyms_gives_null_antonym():
    ht_synomym = HashTable()
    ht_antonym = HashTable()
    ht_synomym.set('Happy', 'Joyful')
    ht_antonym.set('Happy', 'Sad')
    ht_synomym.set('Sad', 'Sorrowful')
    ht_antonym.set('Sad', 'Happy')
    ht_synomym.set('extra', 'value')
    assert left_join(ht_synomym, ht_antonym) == [['Sad', 'Sorrowful', 'Happy'], ['extra', 'value', 'Null'], ['Happy', 'Joyful', 'Sad']]


def test_extra_in_antonym_ignored():
    ht_synomym = HashTable()
    ht_antonym = HashTable()
    ht_synomym.set('Happy', 'Joyful')
    ht_antonym.set('Happy', 'Sad')
    ht_synomym.set('Sad', 'Sorrowful')
    ht_antonym.set('Sad', 'Happy')
    ht_antonym.set('extra', 'value')
    assert left_join(ht_synomym, ht_antonym) == [['Sad', 'Sorrowful', 'Happy'], ['Happy', 'Joyful', 'Sad']]
