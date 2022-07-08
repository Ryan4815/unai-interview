# unai-interview

Interview task for Unai Tech Lead role. 

Command line tool for querying cocktails based on ingredients available.

Input: a comma separated list of ingredients the user has available

Output: a list of cocktail names that can be made using the provided ingredients, one per line. The url for the full cocktail metadata is also supplied.

The tool will return a list of cocktails that can be made using any of the available ingredients exclusively.
I.e. not all of the ingredients must be used, but each cocktail must only have ingredients from the list provided.

## Assumptions
- One use case (as described above) can therefore be a single function call
- Fixed data schema (as per [TheCocktailDB](thecocktaildb.com))
- Ingredients must match as per [TheCocktailDB](thecocktaildb.com/api/json/v1/1/list.php?i=list) (no fuzzy matching)
- Test API Key "1" is used - multi-parameter queries are locked behind a Patreon pay wall and production API key
- No sorting applied to data client side
- Searching one field (ingredients)
- Searching is case-
- Single user - no concurrency required
- Command line only i.e. no front-end / UI required
- Run in a terminal environment with Python 3 and pip (ubuntu was used for development)

## Dependencies

Assumed python3 and pip installed. 

The following are installed with the requirements file.

- click - used for CLI docs
- pytest - for unit testing
- pytest-cov - testing coverage report

## Running the App

Open a terminal within the project directory.

First create a new virtual python environment:

```commandline
python3 -m venv venv
. venv/bin/activate
```

Then install dependencies:

```commandline
pip install -r requirements.txt
```

Run the application as follows

```commandline
python application.py -i banana,rum
```

Or

```commandline
python application.py --ingredients banana,rum
```

For CLI options and advice run the help command

```commandline
python application.py --help
```

The -i or --ingredients flag is used for available ingredients.

Specify ingredients within quotations for multi-word ingredients e.g. "southern comfort"

```commandline
python application.py -i "banana,southern comfort,rum"
```

## Running tests

Tests (and coverage report) can be run with:

```commandline
py.test tests.py --cov=.
```

## Future Improvements

- Reduce number of queries e.g. use of multi-paramater queries with paid production key
- Show images and instructions if requested (new command line options)
- Option to list the recipes the user can *almost* make, i.e those where they are 1 or 2 ingredients short. Tell them the missing ingredients.
- Option for local copy of database to reduce number of API calls/queries
- Front end displaying above information to the user graphically
- Tests using mock data rather than real API calls
- Split out logic as scope grows - i.e. separate classes and methods for distinct functionality
- This will allow more precise unit testing of specific functions