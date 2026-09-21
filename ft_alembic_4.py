import alchemy

def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functuon can be reached")
    print("This will raise an excepition!")
    print("Testing the hidden create_earth: ", end="")
    print(f"{alchemy.create_earth()}")


if __name__ == "__main__":
    main()
