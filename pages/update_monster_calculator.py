"""update_monster_calculator function"""
import components as comp
import dnd
import formatting


def update_monster_calculator(
    monster_name,
    size,
    family,
    challenge_rating,
    armour,
    armour_class_bonus,
    basic_speed,
    flying,
    hovering,
    burrowing,
    climbing,
    swimming,
    strength,
    dex,
    con,
    intelligence,
    wis,
    cha,
    traits_block,
) -> list:
    """
    Generate the reactive components for the monster calculator page

    Args:
        challenge_rating (int): Monster's challenge rating

    Returns:
        list: List of html components
    """
    speeds = {
        "basic_speed": int(basic_speed),
        "flying": int(flying),
        "hovering": int(hovering),
        "burrowing": int(burrowing),
        "climbing": int(climbing),
        "swimming": int(swimming),
    }

    base_attribute_modifiers = {
        "strength": int(strength),
        "dex": int(dex),
        "con": int(con),
        "intelligence": int(intelligence),
        "wis": int(wis),
        "cha": int(cha),
    }

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
        speeds=speeds,
        base_attribute_modifiers=base_attribute_modifiers,
    )
    
    traits = traits_block.split('\n')
    traits_elements = []
    for trait in traits:
        if trait.count('.') == 0:
            traits_elements.append(comp.trait(trait+'.',""))
        else:
            trait_name, trait_value = trait.split('.', 1)
            traits_elements.append(comp.trait(trait_name+'.',trait_value))

    return [
        comp.card_section(
            [
                comp.section_title(monster.name),
                comp.subtitle(f"{monster.size.label} {monster.family.label.lower()}"),
            ],
        ),
        comp.card_section(
            [
                comp.card_element(
                    "Armor Class",
                    f"{monster.armour_class}"
                    + (f" ({monster.armour.label.lower()} armor)"
                    if monster.armour.label != "Natural"
                    or monster.armour_class_bonus > 0
                    else ""),
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
                    f"{formatting.format_challenge_rating(monster.challenge_rating)} "
                    f"({monster.experience_points:,} XP)",
                ),
            ]
        ),
        comp.card_section(
            traits_elements
        ) if len(traits_elements) > 0 else None
    ]
