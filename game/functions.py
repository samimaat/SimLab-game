from elements import *

# Universal Functions
def choose_element():
    # Add a loop for not choosing an element to study. i.e. There is no such element!
    while True:
        element_name = input("Choose an element to investigate: ")
        if element_name not in dict_of_elements:
            print("Hey! There is no such element in the list. Try again.\n")
        else:
            return dict_of_elements[element_name]

def continue_with_instrument():
    
    ans = ""
    while ans != "y" and ans != "n":
        ans = input("Do you wish to continue with the same instrument? Answer yes [y] or no [n]: ")
    return ans

def choose_instrument(element):
    print(list(dict_of_instruments.keys()))
    while True:
        instrument = input("Choose an instrument to use: ")
        if instrument.capitalize() not in dict_of_instruments: 
            print("Hey! There is no such instrument in the list. Try again.")
        else:
            return dict_of_instruments[instrument](element) # Selects a function to use from the dictionary [...] and with the argument (...)

# Main Instrument Functions
def lightbox(element):
    element_name = element["Name"]

    print(element_name.capitalize() + f" is now placed in a box. You can see inside only when you have defined a color of the light inside.\nYou can do so by changing the color of the light inside the box.\n")

    cont = "y"    
    while cont == "y":
        color = input("Give a color of the light to use in the box. Your options are red, orange, yellow, green, cyan, blue and violet: ")

        print(f"With the {color} light you can see that {element_name} is {appearance(color, element)}.\n")
        cont = continue_with_instrument()
    
    if cont == "n":
        choose_instrument(element)
        print("\n")

# Subfunction for Lightbox
def appearance(color, element):
    # Add functionality to have combined colors. Should be complicated enough.
    ## For example what would I have to do to make the object look white? Or to have black as an option?
    element_color = element["Color"]

    if color.lower() == element_color.lower():
        appearance = color
    else:
        appearance = "black"
    
    return appearance


def heatbox(element):
    element_name = element["Name"]

    print(element_name.capitalize() + f" is now placed in a box. You can see inside and you can change the temperature of the box.\nDetermine the melting point and the boiling point of {element_name}.\nYou can do so by changing the temperature inside the box.\n")

    cont = "y"    
    while cont == "y":
        while True:
            temp = int(input("Give a temperature which to use in the box: "))
            if temp < -273.15:
                print("Hey! That's below absolute zero. The instrument can't go that low. Try again.\n")
            else:
                break

        print(f"At temperature {temp} you can see that {element_name} is {phase(temp, element)}.\n")
        cont = continue_with_instrument()
    
    if cont == "n":
        choose_instrument(element)
        print("\n")
        
# Subfunction for Heatbox
def phase(temp, element):
    element_bp = element["Boiling point"]
    element_mp = element["Melting point"]

    # Include funny text for below the absolute zero point!
    if temp <= element_mp:
        phase = "solid"
    elif element_mp < temp < element_bp:
        phase = "liquid"
    else:
        phase = "gas"

    return phase

# Dictionary of functions
# Can these be moved somewhere else? They have to be called after the functions have been defined.
dict_of_instruments = {"Heatbox": heatbox,
                       "Lightbox": lightbox}