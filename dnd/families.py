"""Classes for presenting monster type"""
from dataclasses import dataclass
from enum import Enum


@dataclass
class FamilyDescriptor:
    """Monster type description"""
    name:str
    description:str

class Family(Enum):
    """Monster types"""
    ABERRATION = FamilyDescriptor('Aberration', 'Alien entities, often with powers drawn from their minds')
    BEAST = FamilyDescriptor('Beast', 'Beasts are nonhumanoid creatures that are part of the natural world. Some have magic powers, but generally low intelligence.')
    CELESTIAL = FamilyDescriptor('Celestial', 'Creatures native to the Upper Planes, good by nature.')
    CONSTRUCT = FamilyDescriptor('Construct', 'Created artificially, such as golems.')
    DRAGON = FamilyDescriptor('Dragon', 'Dragons')
    ELEMENTAL = FamilyDescriptor('Elemental', 'Creatures from the elemental planes')
    FEY = FamilyDescriptor('Fey', 'Creatures of magic with a connection to nature.')
    FIEND = FamilyDescriptor('Fiend', 'Creatures native to the Lower Planes, evil by nature.')
    GIANT = FamilyDescriptor('Giant', 'Human-like but larger than humans.')
    HUMANOID = FamilyDescriptor('Humanoid', 'Main people of most worlds, bipeds with culture and few magical abilities.')
    MONSTROSITY = FamilyDescriptor('Monstrosity', 'Monstrosities are unnatural creatures from a variety of origins, including curses and magical experimentation. A catch-all category')
    OOZE = FamilyDescriptor('Ooze', 'Oozes are gelatinous creatures with no fixed form.')
    PLANT = FamilyDescriptor('Plant', 'Plants include both vegetable and fungal creatures.')
    UNDEAD = FamilyDescriptor('Undead', 'Undead creatures were once alive, and have been reanimated by unnatural forces.')