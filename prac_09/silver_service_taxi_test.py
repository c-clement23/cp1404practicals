from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Hummer", 200, 2)

    taxi.start_fare()
    taxi.drive(18)

    fare = taxi.get_fare()
    print(f"Current fare: ${taxi.get_fare():.2f}")
    assert round(fare,2) == 48.78, f"Expected $48.78, got ${fare:.2f}"

if __name__ == "__main__":
    main()