"""update_monster_calculator function"""
import dash
import components as comp


def update_monster_calculator(challenge_rating: int) -> list:
    """
    Generate the reactive components for the monster calculator page

    Args:
        challenge_rating (int): Monster's challenge rating

    Returns:
        list: List of html components
    """
    return [
        comp.controls.Monster.CR.value.to_html(challenge_rating),
        dash.html.Div(f"Monster CR: {challenge_rating}"),
    ]
