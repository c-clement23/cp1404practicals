"""
Read, sort, update, and save guitar data from guitars.csv
Estimate: 25 minutes
Actual:
"""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)



def load_guitars(filename):
    """Load guitars from a CSV file"""
    guitars = []
    with open(filename, 'r') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
        return guitars