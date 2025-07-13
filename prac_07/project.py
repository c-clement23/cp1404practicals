"""
Project class for managing project data
Estimated time: 1.5 hours
"""

import datetime

class Project:
    """Represent a single project"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date() if isinstance(start_date, str) else start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%")

    def is_somplete(self):
        return self.completion_percentage == 100

    def __lt__(self, other):
        return self.priority < other.priority

    def update(self, new_percentage = None, new_priority = None):
        if new_percentage is not None:
            self.completion_percentage = new_percentage
        if new_priority is not None:
            self.priority = new_priority