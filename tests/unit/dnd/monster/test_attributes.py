"""Test attributes class"""
from dnd.monster import attributes


def test_attributes_to_dict_basic():
    """Test to_dict method under default values"""
    test_attributes = attributes.Attributes()

    expected = {
        attribute_name.value: "0" for attribute_name in attributes.AttributeNames
    }

    actual = test_attributes.to_dict()

    assert expected == actual


def test_attributes_to_dict_set_strength():
    """Test to_dict method with one attribute set"""
    test_attributes = attributes.Attributes(strength=1)

    expected = {
        attribute_name.value: "0"
        for attribute_name in attributes.AttributeNames
        if attribute_name.value != "strength"
    }
    expected["strength"] = "1"

    actual = test_attributes.to_dict()

    assert expected == actual


def test_attributes_to_dict_set_multiple_attributes():
    """Test to_dict method with multiple attributes set"""
    test_attributes = attributes.Attributes(strength=1, dexterity=2, constitution=-3)

    expected = {
        attribute_name.value: "0"
        for attribute_name in attributes.AttributeNames
        if not attribute_name.value in ["strength", "dexterity", "constitution"]
    }
    expected["strength"] = "1"
    expected["dexterity"] = "2"
    expected["constitution"] = "-3"

    actual = test_attributes.to_dict()

    assert expected == actual
