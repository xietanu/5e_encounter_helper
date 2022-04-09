"""Monster class"""

from dnd import armours, families, sizes, attributes


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
