from elements import *
from functions import *

# SimLab game

thing_to_investigate = "A THING"

# List of instruments
# ... make it

### START OF UI AND GAME


print(f"Choose {thing_to_investigate} you wish to investigate from the list: ")
print(list(dict_of_elements.keys()))
print() # empty line, find a better to way add it
element = choose_element()
# element = unknownium

print("You have chosen '" + element.get("Name") + "' to investigate. Good luck.\n")

# Add the list of different instruments.
# print("Choose an instrument from the list to use for investigation.")


# Choose an instrument to use.
heatbox(element)


## Probably every instrument is a function.