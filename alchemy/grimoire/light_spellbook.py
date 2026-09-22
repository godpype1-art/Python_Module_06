import alchemy.grimoire


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    allowed: str = alchemy.grimoire.validate_ingredients(ingredients)
    if allowed.endswith("INVALID"):
        return "Spell Rejected"
    else:
        return f"Spell Recorded: {spell_name} ({allowed})"
