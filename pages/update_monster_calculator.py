"""update_monster_calculator function"""
import os
import components as comp
import dnd
import formatting


def update_monster_calculator(
    **kwargs,
) -> list:
    """
    Generate the reactive components for the monster calculator page

    Args:
        challenge_rating (int): Monster's challenge rating

    Returns:
        list: List of html components
    """

    monster = dnd.monster.Monster.from_query_string_kwargs(**kwargs)

    monster_filenames = os.listdir("data/monsters")
    monster_filenames_labels = (
        tuple(
            monster_file.replace("_", " ").replace(".json", "")
            for monster_file in monster_filenames
        )
        if monster_filenames
        else tuple(["No saved monsters"])
    )
    monster_filenames_values = tuple(monster_filenames) if monster_filenames else tuple("")

    return [
        comp.card_row(
            comp.card(
                [
                    comp.controls.DropdownControl(
                        identifier="monster-load-filename",
                        label="Load monster",
                        default_value="",
                        options_labels=monster_filenames_labels,
                        options_values=monster_filenames_values,
                    ).to_html()
                ]
            )
        ),
        comp.card_row(
            comp.card(
                [
                    comp.card_section(
                        [
                            comp.section_title(monster.core.name),
                            comp.subtitle(
                                f"{monster.core.size.label} {monster.core.family.label.lower()}"
                            ),
                        ],
                    ),
                    comp.card_section(
                        [
                            comp.card_element(
                                "Armor Class",
                                f"{monster.armour_class}"
                                + (
                                    f" ({monster.armour.armour_type.label.lower()} armor)"
                                    if monster.armour.armour_type.label != "Natural"
                                    or monster.armour.bonus > 0
                                    else ""
                                ),
                            ),
                            comp.card_element(
                                "Hit Points",
                                f"{monster.hit_points.average_value} ({monster.hit_points})",
                            ),
                            comp.card_element(
                                "Speed",
                                ", ".join(str(speed) for speed in monster.speeds),
                            ),
                        ]
                    ),
                    comp.card_section(
                        [
                            comp.card_element_row(
                                [
                                    attribute.to_html()
                                    for attribute in monster.attributes
                                ]
                            )
                        ]
                    ),
                    comp.card_section(
                        [
                            comp.card_element(
                                "Prof bonus:", str(monster.proficiency_bonus)
                            ),
                            comp.card_element("Save DC:", str(monster.save_dc)),
                            comp.card_element(
                                "Challenge",
                                f"{formatting.format_challenge_rating(monster.core.challenge_rating)} "
                                f"({monster.experience_points:,} XP)",
                            ),
                        ]
                    ),
                    comp.card_section(
                        [
                            comp.trait(title, value)
                            for title, value in monster.core.traits.items()
                        ]
                    )
                    if monster.core.traits
                    else None,
                ]
            ),
            stat_block=True,
        ),
    ]
