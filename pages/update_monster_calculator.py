"""update_monster_calculator function"""
import components as comp
import dnd


def update_monster_calculator(challenge_rating: str) -> list:
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
        comp.controls.Monster.CR.value.to_html(challenge_rating)
    ] + monster.generate_stat_block()
