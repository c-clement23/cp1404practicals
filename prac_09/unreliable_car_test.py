from unreliable_car import UnreliableCar

def main():
    car = UnreliableCar("ManualTestCar", 100, 30)

    driven_times = 0
    attempts = 20

    for i in range(attempts):
        distance = car.drive(10)
        if distance > 0:
            driven_times += 1
            print(f"Attempt {i+1}: Drove {distance} km")
        else:
            print(f"Attempt {i+1}: Did not drive")

    print(f"Driven {driven_times} out of {attempts} attempts")
if __name__ == "__main__":
    main()