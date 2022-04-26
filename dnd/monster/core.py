"""Class to hold core data about monsters"""
from dataclasses import dataclass
from typing import Optional, Union

from dnd.monster import families, sizes
import formatting


@dataclass
class MonsterCoreData:
    """Holds core information about the type of the monster"""

    name: str = "Unnamed monster"
    challenge_rating: int = 1
    size: sizes.Sizes = sizes.Sizes.MEDIUM
    family: families.Families = families.Families.HUMANOID
    traits: Optional[dict[str, str]] = None

    def __init__(
        self,
        name: str = "Unnamed monster",
        challenge_rating: Union[str, int] = 1,
        size: str = "MEDIUM",
        family: str = "HUMANOID",
        traits: str = "Example. Example trait.",
    ):
        self.name = name
        self.challenge_rating = (
            int(challenge_rating) if formatting.is_intlike(challenge_rating) else 1
        )
        self.size = sizes.Sizes[size]
        self.family = families.Families[family]

        self.traits = {}
        if traits:
            trait_lines = traits.split("\n")
            for trait in trait_lines:
                if trait.count(".") == 0:
                    self._add_trait(trait, "")
                else:
                    trait_name, trait_value = trait.split(".", 1)
                    self._add_trait(trait_name, trait_value)

    def _add_trait(self, title: str, value: str) -> None:
        if self.traits is None:
            return

        title_repeat = 1
        unique_title = title + "."
        while unique_title in self.traits:
            title_repeat += 1
            unique_title = f"{title} ({title_repeat})."

        self.traits[unique_title] = value

    def to_dict(self) -> dict[str, str]:
        """
        Creates a dictionary containing configuration of the monster core for saving.

        Returns:
            dict[str, str]: The dictionary containing the configuration.
        """
        trait_lines = (
            "\n".join(f"{name}{value}" for name, value in self.traits.items())
            if self.traits is not None
            else ""
        )
        return {
            "name": self.name,
            "challenge_rating": str(self.challenge_rating),
            "size": self.size.name,
            "family": self.family.name,
            "traits": trait_lines,
        }
