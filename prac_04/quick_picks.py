import random

def main():
    NUMBERS_PER_PICK = 6
    MIN_NUMBER = 1
    MAX_NUMBER = 45
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        random_numbers_picked = generate_quick_pick(MIN_NUMBER,MAX_NUMBER, NUMBERS_PER_PICK)
        print(" ".join(f"{number}" for number in random_numbers_picked))

def generate_quick_pick(MIN_NUMBER,MAX_NUMBER, NUMBERS_PER_PICK):
    random_numbers = []
    while len(random_numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in random_numbers:
            random_numbers.append(number)
    random_numbers.sort()
    # print(random_numbers)
    return random_numbers

main()