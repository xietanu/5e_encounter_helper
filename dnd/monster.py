"""Monster class"""

from dnd import armours, constants, families, sizes, attributes, dice


BASE_DC = 11
BASE_PROF_BONUS = 2
BASE_AC = 13


class Monster:
    """
    Monster stat block
    """

    def __init__(
        self,
        name: str,
        challenge_rating: int,
        family: families.FamilyData,
        size: sizes.SizeData,
        armour: armours.ArmourData,
        armour_class_bonus: int = 0,
    ):
        self.name = name
        self.challenge_rating = challenge_rating
        self.family = family
        self.size = size
        self.armour = armour
        self.armour_class_bonus = armour_class_bonus

        self.attributes = attributes.Attributes()

        self.attributes.update_dex(
            self._expected_armour_class, armour_class_bonus, armour
        )

    @property
    def experience_points(self) -> int:
        """
        Get the number of experience points associated with the challenge rating of the monster.

        Returns:
            int: Experience points
        """
        return constants.XP_FROM_CR[self.challenge_rating]

    @property
    def proficiency_bonus(self) -> int:
        """
        Monster's proficiency bonus for adding to skills/checks it is proficient in.

        Returns:
            int: Monster's proficiency bonus
        """
        return max((self.challenge_rating - 1), 0) // 4 + BASE_PROF_BONUS

    @property
    def save_dc(self) -> int:
        """
        Standard difficulty of saves required from the monster's actions.

        Returns:
            int: Stanard difficulty class.
        """
        return BASE_DC + ((self.challenge_rating + 1) // 2)

    @property
    def _expected_armour_class(self) -> int:
        """
        Expected armour class of the monster based on challenge rating.

        Returns:
            int: Expected armour class
        """
        return BASE_AC + (self.challenge_rating // 2)

    @property
    def armour_class(self) -> int:
        """
        Expected armour class of the monster based on challenge rating.

        Returns:
            int: Expected armour class
        """
        return (
            self.armour.base_ac
            + min(self.attributes.dex.modifier, self.armour.max_dex_mod)
            + self.armour_class_bonus
        )

    @property
    def _expected_hp(self) -> int:
        modifidied_challenge_rating = self.challenge_rating + (
            (self._expected_armour_class - self.armour_class) // 2
        )
        if modifidied_challenge_rating <= 0:
            return {-3: 3, -2: 9, -1: 15, 0: 24}[max(modifidied_challenge_rating, -3)]
        elif modifidied_challenge_rating <= 7:
            return modifidied_challenge_rating * 15 + 15
        return modifidied_challenge_rating * 15

    @property
    def hit_points(self) -> dice.DiceFormula:
        hp_level = round(
            self._expected_hp
            / (self.size.die.average_value + self.attributes.con.modifier)
        )
        return dice.DiceFormula(
            hp_level, self.size.die, hp_level * self.attributes.con.modifier
        )
