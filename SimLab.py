# SimLab game

thing_to_investigate = "A THING"

# Element dictionaries

unknownium = {
    "Name": "unknownium",
    "Phase at STP": "Liquid",
    "Melting point": 0,
    "Boiling point": 100,
    "Taste": "Tasteless",
    "Smell": "Odorless",
    "Transparency": "Transparent" # What if I want to change transparency at different temperatures?



}


# The dictionaries as a list.
list_of_investigables = ["unknownium"]

# Functions
def continue_with_instrument():
    ans = input("Do you wish to continue with the same instrument? Answer yes [y] or no [n]: ")
    return ans

def choose_element():
    # Add a loop for not choosing an element to study. i.e. There is no such element!
    element = input("Choose an element to investigate: ")
    return element

def heatbox(element):
    element_name = element.get("Name")

    print(element_name.capitalize() + f" is now placed in a box. You can see inside and you can change the temperature of the box.\nDetermine the melting point and the boiling point of {element_name}.\nYou can do so by changing the temperature inside the box.")

    cont = "y"    
    while cont == "y":
        temp = int(input("Give a temperature which to use in the box: "))

        print(f"At temperature {temp} you can see that {element_name} is {phase(temp, element)}.\n")
        cont = continue_with_instrument()
        

def phase(temp, element):
    element_mp = element.get("Melting point")
    element_bp = element.get("Boiling point")

    if temp <= element_mp:
        phase = "solid"
    elif element_mp < temp < element_bp:
        phase = "liquid"
    else:
        phase = "gas"

    return phase

# List of instruments
# ... make it

### START OF UI AND GAME


print(f"Choose {thing_to_investigate} you wish to investigate from the list: ")
print(list_of_investigables)
# element = choose_element()
element = unknownium

print("You have chosen " + element.get("Name") + " to investigate. Good luck.")

# Add the list of different instruments.
# print("Choose an instrument from the list to use for investigation.")



# Choose an instrument to use.
heatbox(element)


## Probably every instrument is a function.