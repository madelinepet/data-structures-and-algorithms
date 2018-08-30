import pytest
from .multi_bracket_validation import multi_bracket_validation


def test_when_input_not_str():
    expected = False
    actual = multi_bracket_validation(7)
    assert expected == actual


def test_returns_false_if_no_opening_bracket_to_match_closing():
    expected = False
    actual = multi_bracket_validation(']')
    assert expected == actual


def test_returns_false_if_no_closing_bracket_to_match_opening():
    expected = False
    actual = multi_bracket_validation('{')
    assert expected == actual


def test_returns_true_if_all_have_match():
    expected = True
    actual = multi_bracket_validation('[]')
    assert expected == actual
