from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    taxis =[Taxi("Prius", 100),
            SilverServiceTaxi("Limo", 100, 2),
            SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = None
    total_bill = 0.0

