from elements import *
from functions import *

# SimLab game

thing_to_investigate = "A THING"

### START OF UI AND GAME

print(f"Choose {thing_to_investigate} you wish to investigate from the list: ")
print(list(dict_of_elements.keys()))
print() # empty line, find a better to way add it
element = choose_element()
# element = unknownium

print("You have chosen '" + element.get("Name") + "' to investigate. Good luck.\n")

# Shows a list of instruments that you can choose from.
choose_instrument(element)


# Choose an instrument to use.
# lightbox(element)
# heatbox(element)