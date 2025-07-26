class Band:
    """Band class representing a group of musicians"""

    def __init__(self, name=""):
        """Initialise Band with a name and an empty list of musicians"""
        self.name = name
        self.musicians = []