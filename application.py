"""Command line application for searching cocktails"""

import click
import requests
import json
from config import *

@click.command()
@click.option('-i', '--ingredients', 'ingredients', is_flag=False,
              default='banana,honey,milk', show_default=True,
              type=click.STRING, help='Comma-separated list of ingredients')
def start_app(ingredients : str):
    """
    Search the cocktaildb for cocktails that contain the supplied ingredients only.
    Main application thread.
    :param ingredients: str: comma-separated list of ingredients
    :return: None
    """

    # Remove case and any duplicate ingredients supplied via CLI
    ingredients_set = set([i.strip().lower() for i in ingredients.split(',')])
    print(f"Ingredient(s) available: {ingredients_set}")

    # Cocktails that contain any of the ingredients supplied via command line
    cocktails = []
    for i in ingredients_set:
        cocktail_request = requests.get(f"{INGREDIENT_FILTER_URL}{i}")
        # Check we have at least one recipe containing said ingredient
        if cocktail_request.text:
            cocktail_data = json.loads(cocktail_request.text)
            cocktails += [c[DRINK_NAME_KEY] for c in cocktail_data[DRINK_KEY]]
    # Remove any duplicate cocktails
    cocktails_set = set(cocktails)

    # Which of these cocktails are possible using ONLY the ingredients available
    cocktails_possible = []
    for c in cocktails_set:
        have_all_ingredients = True
        ingredients_request = requests.get(f"{COCKTAIL_SEARCH_URL}{c}")
        # Check whether additional ingredients are required
        if ingredients_request.text:
            ingredients_data = json.loads(ingredients_request.text)
            # Schema has strIngredient1 through strIngredient15
            for i in range(1, MAX_INGREDIENTS + 1):
                key_i = INGREDIENT_KEY + str(i)
                ingredient_i = ingredients_data[DRINK_KEY][0][key_i]
                # Only validate non-null ingredients
                if ingredient_i:
                    # Ignore case sensitivity
                    if ingredient_i.lower() not in ingredients_set:
                        have_all_ingredients = False
        # All ingredients available, append to final list
        if have_all_ingredients:
            cocktails_possible.append([c, f"{COCKTAIL_SEARCH_URL}{c}"])

    if cocktails_possible:
        print("With these ingredients you can make:")
        # Print them on individual lines
        for c in cocktails_possible:
            print(f"{c[0]}, '{c[1]}'")
    else:
        print("No cocktails can be made from the ingredients available :(")


if __name__ == '__main__':  # pragma: no cover
    start_app()
