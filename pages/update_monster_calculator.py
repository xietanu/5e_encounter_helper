"""update_monster_calculator function"""
import dash

import components as comp
import dnd
from components import controls


def update_monster_calculator(challenge_rating: str, family: str) -> list:
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

    monster = dnd.Monster("Gelatinous Cube", cr_int, dnd.Family.OOZE.value)

    return [
        comp.card_section(
            [
                comp.card_element("Name:", monster.name),
                controls.Monster.CR.value.to_html(challenge_rating),
                dash.html.Div(controls.Monster.FAMILY.value.to_html(family)),
                dash.html.Div(f"{monster.family.description}", className="dnd-hint"),
            ],
        ),
        comp.card_section(
            [
                dash.html.Div(f"Prof bonus: {monster.proficiency_bonus}"),
                dash.html.Div(f"Save DC: {monster.save_dc}"),
            ]
        ),
    ]
