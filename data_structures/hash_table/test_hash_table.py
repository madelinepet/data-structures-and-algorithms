from .hash_table import HashTable
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
