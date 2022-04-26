"""Test attributes class"""
from dnd.monster import speed


def test_speeds_to_dict_basic():
    """Test to_dict method under default values"""
    test_speeds = speed.Speeds()

    expected = {}

    actual = test_speeds.to_dict()

    assert expected == actual


def test_speed_to_dict_set_basic_speed():
    """Test to_dict method with one attribute set"""
    test_speeds = speed.Speeds(basic_speed=30)

    expected = {"basic_speed": "30"}

    actual = test_speeds.to_dict()

    assert expected == actual


def test_attributes_to_dict_set_multiple_attributes():
    """Test to_dict method with multiple attributes set"""
    test_speeds = speed.Speeds(basic_speed=45, fly=25, hover=15)

    expected = {"basic_speed": "45", "fly": '25', "hover": '15'}

    actual = test_speeds.to_dict()

    assert expected == actual
