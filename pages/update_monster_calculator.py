"""update_monster_calculator function"""
import dash

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
                comp.card_element(
                    "CR:", formatting.format_challenge_rating(monster.challenge_rating)
                ),
                dash.html.Div(f"A {monster.size.label} {monster.family.label}"),
            ],
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
                comp.card_element("AC:", str(monster.armour_class)),
            ]
        ),
    ]
