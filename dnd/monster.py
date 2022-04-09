"""Monster class"""

from dataclasses import dataclass
from dnd import families, size, armour


BASE_DC = 11
BASE_PROF_BONUS = 2
BASE_AC = 13


@dataclass
class Monster:
    """
    Monster stat block
    """

    name: str
    challenge_rating: int
    family: families.FamilyData
    size: size.SizeData
    armour: armour.ArmourData
    armour_class_bonus: int = 0

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
        return BASE_DC + (self.challenge_rating // 2)

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
            + (
                min(self.dex, self.armour.max_dex_mod)
                if self.armour.max_dex_mod is not None
                else self.dex
            )
            + self.armour_class_bonus
        )

    @property
    def dex(self) -> int:
        return (
            min(
                self._expected_armour_class
                - self.armour_class_bonus
                - self.armour.base_ac,
                self.armour.max_dex_mod,
            )
            if self.armour.max_dex_mod is not None
            else self._expected_armour_class
            - self.armour_class_bonus
            - self.armour.base_ac
        )
