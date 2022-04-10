"""update_monster_calculator function"""
import components as comp
import dnd
import formatting


def update_monster_calculator(
    monster_name, size, family, challenge_rating, armour, armour_class_bonus
) -> list:
    """
    Generate the reactive components for the monster calculator page

    Args:
        challenge_rating (int): Monster's challenge rating

    Returns:
        list: List of html components
    """
    monster = dnd.Monster(
        name=monster_name,
        challenge_rating=int(challenge_rating)
        if formatting.is_intlike(challenge_rating)
        else 0,
        family=dnd.Families[family],
        size=dnd.Sizes[size],
        armour=dnd.Armours[armour],
        armour_class_bonus=int(armour_class_bonus)
        if armour_class_bonus.isnumeric()
        else 0,
    )

    return [
        comp.card_section(
            [
                comp.section_title(monster.name),
                comp.subtitle(f"{monster.size.label} {monster.family.label.lower()}"),
            ],
        ),
        comp.card_section(
            [
                comp.card_element("Armor Class", str(monster.armour_class)),
                comp.card_element(
                    "Hit Points",
                    f"{monster.hit_points.average_value} ({monster.hit_points})",
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
                    f"{formatting.format_challenge_rating(monster.challenge_rating)} "
                    f"({monster.experience_points:,} XP)",
                ),
            ]
        ),
    ]
