"""
Guitar class for storing details about guitars.
Estimate: 20 minutes
Actual: 15 minutes
"""

import datetime


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        return  self.year < other.year
