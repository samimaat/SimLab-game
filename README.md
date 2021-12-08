# What's the Game about?

The game is inspired by Andy Weir's Hail Mary Project where the protagonist Ryland Grace exhibits the basic instincts and curiosity of a scientist encountering new life.

I wish to recreate a simulated scientific laboratory environment where you are tasked with finding out properties of unknown elements, substances and possibly life.

## The Gameplay Loop

Choose element ↔ choose equipment ↔ perform experiment and record properties

# Progress

At the moment the game contains one unknown substance 'unknownium'. It has several properties such as 
- melting point
- boiling point
- 'appearance' as in what color it is in pure white light

You can cycle between different instruments.

The game has following instruments:
- Heatbox: You can place the substance inside and change **the temperature** to see what happens to the phase of the substance.
- Lightbox: You can place the substance inside and change **the color of the light** inside the box and figure out the color of the substance.

# UI elements

- command line
- choose which element or biological thing to study
    - element is a basically a dictionary of properties
        - how temperature affects it: freezing point, melting point, boiling point → leads to finding it out
        - how radiation affects it: ...
        - how light affects it, is it see through, opaque does it reflect light, which wave lengths
        - smell?
        - mass?
        - magnetism: is it a metal? or not?
        - conductivity?
        - pressure
        - pH level (acidity, base)
        - crystal structure (8 different kinds)
        - wikipedia for more properties: [https://en.wikipedia.org/wiki/Chemical_element#Properties](https://en.wikipedia.org/wiki/Chemical_element#Properties)
    - you must be able to change the dictionary values
- choose which lab equipment to use: [https://en.wikipedia.org/wiki/Scientific_instrument](https://en.wikipedia.org/wiki/Scientific_instrument)
    - physics: [https://www.labkafe.com/blog/physics-laboratory-equipment-a-complete-list-of-important-equipment-and-their-uses](https://www.labkafe.com/blog/physics-laboratory-equipment-a-complete-list-of-important-equipment-and-their-uses)
        - multimeter (voltage, current, resistance)
        - magnet
        - bunsen burner (to raise the temperature)
        - a timer
        - calorimeter
        - thermometer
        - interferometer
        - geiger counter
    - chemistry
        - scale
        - centrifuge
        - spectrometer
        - spectrogram
        - NMR spectrometer
        - mass spectrometer
        - microscope

