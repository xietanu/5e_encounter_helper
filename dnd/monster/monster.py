"""Monster class"""
import dataclasses
from dnd import dice, constants
from dnd.monster import armours, attributes, core, speed


BASE_DC = 11
BASE_PROF_BONUS = 2
BASE_AC = 13


class Monster:
    """
    Monster stat block
    """

    def __init__(
        self,
        core: core.MonsterCoreData,
        base_attributes: attributes.Attributes,
        speeds: speed.Speeds,
        armour: armours.Armour,
    ):
        self.core = core
        self.armour = armour

        self.attributes = base_attributes
        for attribute_name in [attribute.value for attribute in attributes.AttributeNames]:
            if (
                self.core.family.stat_modifiers
                and attribute_name in self.core.family.stat_modifiers
            ):
                attribute = getattr(self.attributes, attribute_name)
                attribute.base_modifier += self.core.family.stat_modifiers[attribute_name]

        self.attributes.update_dex(
            self._expected_armour_class, armour.armour_type, armour.bonus
        )
        self.speeds = speeds

    @classmethod
    def from_query_string_kwargs(cls, **kwargs):
        """Create a monster from the keyword arguments found in the query string"""
        core_kwargs = {
            key: value
            for key, value in kwargs.items()
            if key
            in [
                field.name for field in dataclasses.fields(core.MonsterCoreData)
            ]
        }
        attribute_kwargs = {
            key: value
            for key, value in kwargs.items()
            if key in [attribute.value for attribute in attributes.AttributeNames]
        }
        speed_kwargs = {
            key: value
            for key, value in kwargs.items()
            if key in [speed.value for speed in speed.SpeedNames]
        }
        armour_kwargs = {
            key: value
            for key, value in kwargs.items()
            if key in [field.name for field in dataclasses.fields(armours.Armour)]
        }

        return cls(
            core=core.MonsterCoreData(**core_kwargs),
            base_attributes=attributes.Attributes(**attribute_kwargs),
            speeds=speed.Speeds(**speed_kwargs),
            armour=armours.Armour(**armour_kwargs),
        )

    @property
    def experience_points(self) -> int:
        """
        Get the number of experience points associated with the challenge rating of the monster.

        Returns:
            int: Experience points
        """
        return constants.XP_FROM_CR[self.core.challenge_rating]

    @property
    def proficiency_bonus(self) -> int:
        """
        Monster's proficiency bonus for adding to skills/checks it is proficient in.

        Returns:
            int: Monster's proficiency bonus
        """
        return max((self.core.challenge_rating - 1), 0) // 4 + BASE_PROF_BONUS

    @property
    def save_dc(self) -> int:
        """
        Standard difficulty of saves required from the monster's actions.

        Returns:
            int: Stanard difficulty class.
        """
        return BASE_DC + ((self.core.challenge_rating + 1) // 2)

    @property
    def _expected_armour_class(self) -> int:
        """
        Expected armour class of the monster based on challenge rating.

        Returns:
            int: Expected armour class
        """
        return BASE_AC + (self.core.challenge_rating // 2)

    @property
    def armour_class(self) -> int:
        """
        Expected armour class of the monster based on challenge rating.

        Returns:
            int: Expected armour class
        """
        return (
            self.armour.armour_type.base_ac
            + min(
                self.attributes.dexterity.modifier, self.armour.armour_type.max_dex_mod
            )
            + self.armour.bonus
        )

    @property
    def _expected_hp(self) -> int:
        """
        Expected hp based on the creature's challenge rating and AC.

        Returns:
            int: expected hit points.
        """
        modifidied_challenge_rating = self.core.challenge_rating + (
            (self._expected_armour_class - self.armour_class) // 2
        )
        if modifidied_challenge_rating <= 0:
            return {-3: 3, -2: 9, -1: 15, 0: 24}[max(modifidied_challenge_rating, -3)]
        if modifidied_challenge_rating <= 7:
            return modifidied_challenge_rating * 15 + 15
        return modifidied_challenge_rating * 15

    @property
    def hit_points(self) -> dice.DiceFormula:
        """
        Number of hit points the monster has, as a dice formula.

        Returns:
            dice.DiceFormula: Monster hit points
        """
        hp_level = round(
            self._expected_hp
            / (self.core.size.die.average_value + self.attributes.constitution.modifier)
        )
        return dice.DiceFormula(
            hp_level,
            self.core.size.die,
            hp_level * self.attributes.constitution.modifier,
        )
    
    def to_dict(self) -> dict[str,dict]:
        """
        Convert this monster's configuration to a dictionary

        Returns:
            dict[str,dict]: The dictionary representing the monster's configuration.
        """
        return {
            'core': self.core.to_dict(),
            'base_attributes': self.attributes.to_dict(),
            'speeds': self.speeds.to_dict(),
            'armour': self.armour.to_dict(),
        }
