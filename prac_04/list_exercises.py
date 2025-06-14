numbers = []
for i in range(0, 5):
    number_input = int(input("Number: "))
    numbers.append(number_input)
# print(numbers) # testing append
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the number is {sum(numbers) / len(numbers)}")