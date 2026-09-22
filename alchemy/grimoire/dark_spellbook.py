from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    allowed: str = validate_ingredients(ingredients)
    if allowed.endswith("INVALID"):
        return "Spell Rejected"
    else:
        return f"Spell Recorded: {spell_name} ({allowed})"
