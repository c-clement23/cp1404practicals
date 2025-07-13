"""
Read, sort, update, and save guitar data from guitars.csv
Estimate: 25 minutes
Actual: 40 minutes
"""

import csv
from guitar import Guitar


FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)

    print("These are the guitars loaded from file:")
    display_guitars(guitars)

    add_new_guitars(guitars)

    guitars.sort()

    print("\nThese are the guitars sorted by year:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from a CSV file"""
    guitars = []
    with open(filename, 'r') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
        return guitars

def display_guitars(guitars):
    """Print all guitars in a formatted list"""
    max_name_length = max(len(guitar.name) for guitar in guitars)

    for i, guitar in enumerate(guitars, 1):
        vintage_tag = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}),"
              f"worth ${guitar.cost:10,.2f}{vintage_tag}")

def add_new_guitars(guitars):
    """Prompt user to add new guitars"""
    print("Add new guitars:")
    name = input("Name: ")
    while name:
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost:,.2f} added.")
        except ValueError:
            print("Invalid input. Try again.")
        name = input("Name: ")

def save_guitars(filename, guitars):
    """Save the updated list of guitars to CSV."""
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])
    print(f"\nGuitars saved to {filename}.")


if __name__ == "__main__":
    main()