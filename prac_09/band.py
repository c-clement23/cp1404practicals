class Band:
    """Band class representing a group of musicians"""

    def __init__(self, name=""):
        """Initialise Band with a name and an empty list of musicians"""
        self.name = name
        self.musicians = []

    def add(self, musicians):
        """Add an instrument to musician's collection."""
        self.musicians.append(musicians)

    def __str__(self):
        """Return a string representation of the Band"""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Make all musicians in the band play"""

        return '\n'.join(musician.play() for musician in self.musicians)