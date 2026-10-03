# Black Baron's First Python Library
A small library just for the purpose of testing how pip install interacts when downloading a custom library.

## Description
This simple repo only has two functions as of the time of writing of this description: 
- get_abs(number):
Prints a message to debug correct connection, returns absolute of provided number.
- add_form_control(form):
Runs through visible fields of a Django form and adds "form-control" class to fields widget attributes.

## Installation
Simply run in your venv the following:
```
python -m pip install git+https://github.com/BlackBaron94/black_barons_first_library.git
```

## Usage
To use functions import thusly:
```
from black_barons_first_library import get_abs, add_form_control
```
