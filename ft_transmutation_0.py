import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("using file alchemy.trasmutation/recipes.py directly")
    print(
        f"Testing lead to gold: {alchemy.transmutation.recipes.lead_to_gold()}"
        )


if __name__ == "__main__":
    main()
