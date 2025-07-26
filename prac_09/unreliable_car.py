import random
from prac_09.car import Car

class UnreliableCar(Car):
    """Car that only drives if a random choice is below reliability"""
    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar with name,fuel and reliability"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive only if random chance < reliability, else don't drive"""
        chance = random.uniform(0, 100)
        if chance < self.reliability:
            return super().drive(distance)
        else:
            return 0