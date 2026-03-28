def validate_ingredients(ingredients: str) -> str:
    if not ingredients:
        raise ValueError("Ingredients cannot be empty.")
    ingredients_list = ["fire", "water", "earth", "air"]
    ingredients_check = ingredients.split(" ")
    for ingredient in ingredients_check:
        if ingredient not in ingredients_list:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
