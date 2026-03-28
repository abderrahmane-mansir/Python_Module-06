from alchemy.grimoire import record_spell, validate_ingredients


def main():
    print("\n=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    validated = "fire air"
    print(f"validate_ingredients(\"{validated}\"): ",
          validate_ingredients(validated))
    unvalidated = "dragon scales"
    print(f"validate_ingredients(\"{unvalidated}\"): ",
          validate_ingredients(unvalidated))

    print("\nTesting spell recording with validation:")
    spell_name = "Fireball"
    ingredients = "fire air"
    print(f"record_spell(\"{spell_name}\", \"{ingredients}\"): "
          f"{record_spell(spell_name, ingredients)}")
    invalid_spell_name = "Dark Magic"
    invalid_ingredients = "shadow"
    print(f"record_spell(\"{invalid_spell_name}\", \"{invalid_ingredients}\"):"
          f" {record_spell(invalid_spell_name, invalid_ingredients)}")

    print("\nTesting late import technique:")
    spell_name = "Lightning"
    ingredients = "air"
    print(f"record_spell(\"{spell_name}\", \"{ingredients}\"): "
          f"{record_spell(spell_name, ingredients)}")
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
