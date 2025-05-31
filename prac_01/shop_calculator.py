"""
4. Shop Calculator
==================

algorithm:
DISCOUNT = 10/100
total_price = 0

get number_of_items
while number_of_items < 0
    display error msg
    get number_of_items
for i in range(1, number_of_items + 1)
    get price_of_items
    total_price = total_price + price_of_items
if total_price > 100
    total_price = total_price - (total_price * DISCOUNT)
display number_of_items, total_price
"""
DISCOUNT = 10/100
total_price = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(1, number_of_items + 1):
    price_of_items = float(input("Price of item: "))
    total_price += price_of_items
if total_price > 100:
    total_price = total_price - (total_price * DISCOUNT)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")