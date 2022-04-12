"""Tests for is_intlike"""
from formatting import type_test


def test_is_intlike_basic_ints():
    """Test for basic, positive integers"""
    assert type_test.is_intlike(1)
    assert type_test.is_intlike("1")
    assert type_test.is_intlike(1.1)
    assert type_test.is_intlike(True)


def test_is_intlike_negative_ints():
    """Tests for negative integers"""
    assert type_test.is_intlike(-1)
    assert type_test.is_intlike("-1")
    assert type_test.is_intlike(-1.1)


def test_is_intlike_not_ints():
    """Tests for things that are not integers"""
    assert not type_test.is_intlike("test")
    assert not type_test.is_intlike("1.0")
