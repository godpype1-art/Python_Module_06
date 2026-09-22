import alchemy.grimoire


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = alchemy.grimoire.light_spell_allowed_ingredients()
    for ingredient in allowed:
        if ingredient in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
