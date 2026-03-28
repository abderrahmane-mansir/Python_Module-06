from .elements import create_fire, create_water, create_earth, create_air


earth_result = create_earth()
air_result = create_air()
fire_result = create_fire()
water_result = create_water()


def healing_potion() -> str:
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion() -> str:
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion() -> str:
    return (
        f"Wisdom potion brewed with {earth_result}, {air_result}, "
        f"{fire_result}, and {water_result}"
    )
