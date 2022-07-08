"""Basic test cases executed via the command line using Click Runner"""

from click.testing import CliRunner

from application import start_app


runner = CliRunner()

def test_start_app_no_ingredients_supplied_recipe_found():
    ingredients = ["banana", "honey", "milk"]
    response = runner.invoke(start_app)
    # default ingredients of 'banana,honey,milk' will be used if none specified
    assert f"Ingredient(s) available: " in response.output
    for i in ingredients:
        assert i in response.output
    assert "With these ingredients you can make:" in response.output
    assert "Sweet Bananas" in response.output
    assert response.exit_code == 0

def test_start_app_one_ingredient_supplied_recipe_not_found():
    ingredients = ["banana"]
    response = runner.invoke(start_app, ["-i", ",".join(ingredients)])
    assert f"Ingredient(s) available: " in response.output
    for i in ingredients:
        assert i in response.output
    assert "No cocktails can be made from the ingredients available :(" in response.output
    assert response.exit_code == 0

def test_start_app_one_ingredient_supplied_recipe_not_found_verbose_flag():
    ingredients = ["banana"]
    response = runner.invoke(start_app, ["--ingredients", ",".join(ingredients)])
    assert f"Ingredient(s) available: " in response.output
    for i in ingredients:
        assert i in response.output
    assert "No cocktails can be made from the ingredients available :(" in response.output
    assert response.exit_code == 0

def test_start_app_multiple_ingredients_supplied_recipe_not_found():
    ingredients = ["banana", "strawberry"]
    response = runner.invoke(start_app, ["-i", ",".join(ingredients)])
    assert f"Ingredient(s) available: " in response.output
    for i in ingredients:
        assert i in response.output
    assert "No cocktails can be made from the ingredients available :(" in response.output
    assert response.exit_code == 0

def test_start_app_multiple_ingredients_supplied_recipe_was_found():
    ingredients = ["banana","honey","milk"]
    response = runner.invoke(start_app, ["-i", ",".join(ingredients)])
    assert f"Ingredient(s) available: " in response.output
    for i in ingredients:
        assert i in response.output
    assert "With these ingredients you can make:" in response.output
    assert "Sweet Bananas" in response.output
    assert response.exit_code == 0

def test_start_app_multiple_ingredients_with_spaces():
    ingredients = ["tequila", "lime juice", "agave syrup"]
    response = runner.invoke(start_app, ["-i", ",".join(ingredients)])
    assert f"Ingredient(s) available: " in response.output
    for i in ingredients:
        assert i in response.output
    assert "With these ingredients you can make:" in response.output
    assert "Margarita" in response.output
    assert response.exit_code == 0

def test_start_app_multiple_ingredients_multiple_recipes_found():
    ingredients = ["banana", "honey", "milk", "tequila", "lime juice", "agave syrup"]
    response = runner.invoke(start_app, ["-i", ",".join(ingredients)])
    assert f"Ingredient(s) available: " in response.output
    for i in ingredients:
        assert i in response.output
    assert "With these ingredients you can make:" in response.output
    assert "Sweet Bananas" in response.output
    assert "Margarita" in response.output
    assert response.exit_code == 0

def test_start_app_help_command():
    response = runner.invoke(start_app, ["--help"])
    assert "Search the cocktaildb " in response.output
    assert response.exit_code == 0

def test_start_app_invalid_command():
    response = runner.invoke(start_app, ["-d"])
    assert "No such option: -d" in response.output
    assert response.exit_code == 2
