"""Monster class"""

from dnd import families


BASE_DC = 11
BASE_PROF_BONUS = 2

class Monster:
    """
    Monster stat block
    """

    def __init__(self, name:str, challenge_rating: int, family: families.FamilyDescriptor):
        self.name = name
        self.challenge_rating = challenge_rating
        self.family = family

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

