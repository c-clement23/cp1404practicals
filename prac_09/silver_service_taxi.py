from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised Taxi with higher price based on fanciness"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness