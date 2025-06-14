"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32

    return fahrenheit


def convert_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)

    return celsius

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = convert_to_fahrenheit(celsius)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
        fahrenheit = float(input("Fahrenheit: "))
        celsius = convert_to_celsius()
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")