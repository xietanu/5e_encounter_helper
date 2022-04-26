"""Tests for Armour class"""
from dnd.monster import armours


def test_armour_to_dict_basic():
    """
    Test to_dict method for default armour
    """
    test_armour = armours.Armour()

    expected = {"armour_type": "NATURAL", "bonus": "0"}

    actual = test_armour.to_dict()

    assert expected == actual


def test_armour_to_dict_heavy():
    """
    Test to_dict method for heavy armour
    """
    test_armour = armours.Armour(armours.ArmourTypes.HEAVY.name)

    expected = {"armour_type": "HEAVY", "bonus": "0"}

    actual = test_armour.to_dict()

    assert expected == actual


def test_armour_to_dict_bonus_1():
    """
    Test to_dict method for default armour with a bonus of 1
    """
    test_armour = armours.Armour(bonus=1)

    expected = {"armour_type": "NATURAL", "bonus": "1"}

    actual = test_armour.to_dict()

    assert expected == actual


def test_armour_to_dict_light_and_bonus_2():
    """
    Test to_dict method for light armour with a bonus of 2
    """
    test_armour = armours.Armour(armour_type=armours.ArmourTypes.LIGHT.name,bonus=2)

    expected = {"armour_type": "LIGHT", "bonus": "2"}

    actual = test_armour.to_dict()

    assert expected == actual
