from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised Taxi with higher price based on fanciness"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return fare including flagfall"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation with flagfall"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
