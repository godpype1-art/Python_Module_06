import elements as root
from .. import potions, elements

def lead_to_gold() -> str:
    return f"Recipe trasmuting Lead to Gold: brew {elements.create_air()} \
        and {potions.strength_potion()} mixed with {root.create_fire()}"