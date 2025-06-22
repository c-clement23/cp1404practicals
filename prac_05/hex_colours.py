COLOR_TO_HEX = {
    "abosolutezero": "#0048ba",
    "acidgreen": "#b0bf1a",
    "aliceblue": "#f0f8ff",
    "alizarincrimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antiquewhite": "#faebd7",
    "antiquewhite1": "#ffefdb",
    "antiquewhite2": "#eedfcc"
}

max_length = max(len(color_name.title()) for color_name in COLOR_TO_HEX)
print(max_length)
print("Available Colors: ")
for name, hex_code in COLOR_TO_HEX.items():
    print(f"{name.title():<{max_length}} is {hex_code}")

color_code = input("Enter short state: ")
while color_code != "":
    if color_code in COLOR_TO_HEX:
        print(color_code, "is", COLOR_TO_HEX[color_code])
    else:
        print("Invalid code")
    state_code = input("Enter color code: ")