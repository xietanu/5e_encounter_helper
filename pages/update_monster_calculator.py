"""update_monster_calculator function"""
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

    monster = dnd.Monster.from_query_string_kwargs(**kwargs)

    traits = kwargs["traits_block"].split("\n")
    traits_elements = []
    for trait in traits:
        if trait.count(".") == 0:
            traits_elements.append(comp.trait(trait + ".", ""))
        else:
            trait_name, trait_value = trait.split(".", 1)
            traits_elements.append(comp.trait(trait_name + ".", trait_value))

    return [
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
                    "Speed", ", ".join(str(speed) for speed in monster.speeds)
                ),
            ]
        ),
        comp.card_section(
            [
                comp.card_element_row(
                    [attribute.to_html() for attribute in monster.attributes]
                )
            ]
        ),
        comp.card_section(
            [
                comp.card_element("Prof bonus:", str(monster.proficiency_bonus)),
                comp.card_element("Save DC:", str(monster.save_dc)),
                comp.card_element(
                    "Challenge",
                    f"{formatting.format_challenge_rating(monster.core.challenge_rating)} "
                    f"({monster.experience_points:,} XP)",
                ),
            ]
        ),
        comp.card_section(traits_elements) if len(traits_elements) > 0 else None,
    ]
