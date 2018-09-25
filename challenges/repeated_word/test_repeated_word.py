from .repeated_word import repeated_word
import pytest


def test_word_appears_twice():
    assert repeated_word('The quick brown fox jumped over the lazy dog') == 'the'


def test_word_appears_thrice():
    assert repeated_word('The quick the brown fox jumped over the lazy dog') == 'the'


def test_all_words_only_once():
    assert repeated_word('The quick brown fox jumped over lazy dog') == []


def test_repeated_word_first_word():
    assert repeated_word('The the quick brown fox jumped over lazy dog') == 'the'


def test_repeated_word_last_word():
    assert repeated_word('The quick brown fox jumped over lazy dog dog') == 'dog'


def test_empty_string_given():
    assert repeated_word('') == []
