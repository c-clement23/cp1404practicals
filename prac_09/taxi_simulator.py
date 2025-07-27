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
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input; please enter a number")

        elif menu_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))

        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")

        print(MENU)
        menu_choice = input(">>> ").lower()


if __name__ == '__main__':
    main()



