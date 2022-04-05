"""update_monster_calculator function"""
import components as comp
import dnd


def update_monster_calculator(challenge_rating: int) -> list:
    """
    Generate the reactive components for the monster calculator page

    Args:
        challenge_rating (int): Monster's challenge rating

    Returns:
        list: List of html components
    """
    monster = dnd.Monster("Gelatinous Cube", challenge_rating, dnd.Family.OOZE.value)

    return [
        comp.controls.Monster.CR.value.to_html(challenge_rating)
    ] + monster.generate_stat_block()
