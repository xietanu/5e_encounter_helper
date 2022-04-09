"""Classes for presenting monster type"""
from dataclasses import dataclass
from enum import Enum


@dataclass
class FamilyData:
    """Monster type description"""

    label: str
    description: str


class Families(FamilyData, Enum):
    """Monster types"""

    ABERRATION = (
        "Aberration", "Alien entities, often with powers drawn from their minds"
    )
    BEAST = (
        "Beast",
        "Beasts are nonhumanoid creatures that are part of the natural world. "
        "Some have magic powers, but generally low intelligence.",
    )
    CELESTIAL = (
        "Celestial", "Creatures native to the Upper Planes, good by nature."
    )
    CONSTRUCT = ("Construct", "Created artificially, such as golems.")
    DRAGON = ("Dragon", "Dragons")
    ELEMENTAL = ("Elemental", "Creatures from the elemental planes")
    FEY = ("Fey", "Creatures of magic with a connection to nature.")
    FIEND = (
        "Fiend", "Creatures native to the Lower Planes, evil by nature."
    )
    GIANT = ("Giant", "Human-like but larger than humans.")
    HUMANOID = (
        "Humanoid",
        "Main people of most worlds, bipeds with culture and few magical abilities.",
    )
    MONSTROSITY = (
        "Monstrosity",
        "Monstrosities are unnatural creatures from a variety of origins, including curses "
        "and magical experimentation. A catch-all category",
    )
    OOZE = (
        "Ooze", "Oozes are gelatinous creatures with no fixed form."
    )
    PLANT = (
        "Plant", "Plants include both vegetable and fungal creatures."
    )
    UNDEAD = (
        "Undead",
        "Undead creatures were once alive, and have been reanimated by unnatural forces.",
    )
