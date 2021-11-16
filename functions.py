from elements import *

# Universal Functions
def choose_element():
    # Add a loop for not choosing an element to study. i.e. There is no such element!
    element_name = input("Choose an element to investigate: ")
    return dict_of_elements.get(element_name)

def continue_with_instrument():
    ans = input("Do you wish to continue with the same instrument? Answer yes [y] or no [n]: ")
    return ans


# Main Instrument Functions
def lightbox(element):
    element_name = element.get("Name")

    print(element_name.capitalize() + f" is now placed in a box. You can see inside only when you have defined a color of the light inside.\nDetermine color of {element_name}.\nYou can do so by changing the color of the light inside the box.")

    cont = "y"    
    while cont == "y":
        color = input("Give a color of the light to use in the box. Your options are red, orange, yellow, green, cyan, blue and violet: ")

        print(f"With the {color} light you can see that {element_name} is {appearance(color, element)}.\n")
        cont = continue_with_instrument()

# Subfunction for Lightbox
def appearance(color, element):
    # Add functionality to have combined colors. Should be complicated enough.
    ## For example what would I have to do to make the object look white? Or to have black as an option?
    element_name = element.get("Name")
    element_color = element.get("Color")

    if color.lower() == element_color.lower():
        appearance = color
    else:
        appearance = "black"
    
    return appearance


def heatbox(element):
    element_name = element.get("Name")

    print(element_name.capitalize() + f" is now placed in a box. You can see inside and you can change the temperature of the box.\nDetermine the melting point and the boiling point of {element_name}.\nYou can do so by changing the temperature inside the box.")

    cont = "y"    
    while cont == "y":
        temp = int(input("Give a temperature which to use in the box: "))

        print(f"At temperature {temp} you can see that {element_name} is {phase(temp, element)}.\n")
        cont = continue_with_instrument()
        
# Subfunction for Heatbox
def phase(temp, element):
    element_mp = element.get("Melting point")
    element_bp = element.get("Boiling point")

    # Include funny text for below the absolute zero point!
    if temp <= element_mp:
        phase = "solid"
    elif element_mp < temp < element_bp:
        phase = "liquid"
    else:
        phase = "gas"

    return phase