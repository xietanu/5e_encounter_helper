"""Monster class"""

from components import titles
from dnd import families
import dash


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
    
    def generate_stat_block(self) -> list:
        return [
            titles.section_title("Monster"),
            dash.html.Div(f"Type: {self.family.name} - {self.family.description}"),
            dash.html.Div(f"CR: {self.challenge_rating}"),
            dash.html.Div(f"Prof bonus: {self.proficiency_bonus}"),
            dash.html.Div(f"Save DC: {self.save_dc}"),
        ]
