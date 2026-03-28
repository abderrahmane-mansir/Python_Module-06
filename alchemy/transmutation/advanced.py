from .basic import lead_to_gold
from ..potions import healing_potion


ltg_result = lead_to_gold()
heal_result = healing_potion()


def philosophers_stone() -> str:
    return (
        "Philosopher’s stone created using"
        f" {ltg_result} and {heal_result}"
    )


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
