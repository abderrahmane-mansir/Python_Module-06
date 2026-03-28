from alchemy.transmutation import (
    elixir_of_life,
    lead_to_gold,
    philosophers_stone,
    stone_to_gem,
)
import alchemy.transmutation as transmutation


def main() -> None:
    print("\n=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}\n")

    print("\nTesting Package Access:")
    print(
        "alchemy.transmutation.lead_to_gold(): "
        f" {transmutation.lead_to_gold()}"
        )
    print(
        "alchemy.transmutation.philosophers_stone():"
        f" {transmutation.philosophers_stone()}"
    )
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
