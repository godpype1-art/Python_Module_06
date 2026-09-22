import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    ingredients: str = "Earth, wind and fire"
    print("Testing recording light spell: ", end="")
    print(f"{alchemy.grimoire.light_spell_record("Fantasy", ingredients)}")


if __name__ == "__main__":
    main()
