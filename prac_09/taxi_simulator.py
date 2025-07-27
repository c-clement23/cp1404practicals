from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    taxis =[Taxi("Prius", 100),
            SilverServiceTaxi("Limo", 100, 2),
            SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = None
    total_bill = 0.0

    MENU = "q)uit, c)hoose taxi, d)rive"

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            pass
        elif choice == "d":
            pass
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")

        print(MENU)
        choice = input(">>> ").lower()




