"""update_monster_calculator function"""
import dash

import components as comp
import dnd
from components import controls


def update_monster_calculator(name: str, challenge_rating: str, family: str, size: str) -> list:
    """
    Generate the reactive components for the monster calculator page

    Args:
        challenge_rating (int): Monster's challenge rating

    Returns:
        list: List of html components
    """
    cr_int = 0
    if challenge_rating.isnumeric():
        cr_int = int(challenge_rating)

    monster = dnd.Monster(
        name,
        challenge_rating =cr_int,
        family = dnd.Families[family],
        size = dnd.Sizes[size],
        armour = dnd.Armours.HEAVY,
    )

    return [
        comp.card_section(
            [
                controls.ShortTexts.NAME.to_html(name),
                comp.card_element_row(
                    [
                        controls.Dropdowns.SIZE.to_html(size),
                        controls.Dropdowns.FAMILY.to_html(family),
                    ]
                ),
                
                controls.Sliders.CR.to_html(challenge_rating),
                
                dash.html.Div(f"{monster.family.description}", className="dnd-hint"),
            ],
        ),
        comp.card_section(
            [
                comp.card_element("Prof bonus:",str(monster.proficiency_bonus)),
                comp.card_element("Save DC:",str(monster.save_dc)),
                comp.card_element("Dex Mod:",str(monster.dex)),
                comp.card_element("AC:",str(monster.armour_class)),
            ]
        ),
    ]
