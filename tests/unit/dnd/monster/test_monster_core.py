"""Tests for the monster core class"""
from dnd.monster import core, sizes,families


def test_core_to_dict_basic():
    """Test core to_dict method with default arguments."""
    test_core = core.MonsterCoreData()

    expected = {
        "name": "Unnamed monster",
        "challenge_rating": "1",
        "size": "MEDIUM",
        "family": "HUMANOID",
        "traits": "Example. Example trait.",
    }

    actual = test_core.to_dict()

    assert expected == actual

def test_core_to_dict_non_default_values():
    """Test core to_dict method with non-default arguments."""
    test_core = core.MonsterCoreData(
        name = "Test",
        challenge_rating = -1,
        size = sizes.Sizes.LARGE.name,
        family = families.Families.BEAST.name,
        traits = "Trait 1. Example text.\nTrait 2. Another trait. Second sentence."
    )

    expected = {
        "name": "Test",
        "challenge_rating": "-1",
        "size": "LARGE",
        "family": "BEAST",
        "traits": "Trait 1. Example text.\nTrait 2. Another trait. Second sentence.",
    }

    actual = test_core.to_dict()

    assert expected == actual
