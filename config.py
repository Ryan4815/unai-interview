# URL constants
API_KEY="1"
COCKTAIL_DB_URL = "https://www.thecocktaildb.com/api/json/v1/" + API_KEY
INGREDIENT_FILTER_URL = COCKTAIL_DB_URL + "/filter.php?i="
COCKTAIL_SEARCH_URL = COCKTAIL_DB_URL + "/search.php?s="
# Schema constants
DRINK_KEY = "drinks"
DRINK_NAME_KEY = "strDrink"
INGREDIENT_KEY = "strIngredient"
MIN_INGREDIENTS = 1  # CocktailDB minimum number of ingredients in a drink
MAX_INGREDIENTS = 15  # CocktailDB maximum number of ingredients in a drink (15 keys)
