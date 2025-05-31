"""
1. Sales Bonus
==============
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Algorithm:
PERCENTAGE_CONVERSION = 100
SALE_THRESHOLD = 1000
LOW_BONUS = 10
HIGH_BONUS = 15
get user_sale
if user_sale less than SALE_THRESHOLD
    user_bonus = user_sale x LOW_BONUS/PERCENTAGE_CONVERSION
else
    user_bonus = user_sale x HIGH_BONUS/PERCENTAGE_CONVERSION
display user_bonus
"""
# PERCENTAGE_CONVERSION = 100
# SALE_THRESHOLD = 1000
# LOW_BONUS = 10
# HIGH_BONUS = 15
#
# user_sale = float(input("Enter sales: $"))
# if user_sale < SALE_THRESHOLD:
#     user_bonus = user_sale * LOW_BONUS/PERCENTAGE_CONVERSION
# else:
#     user_bonus = user_sale * HIGH_BONUS/PERCENTAGE_CONVERSION
#
# print(f"User Bonus: ${user_bonus}")

"""
PERCENTAGE_CONVERSION = 100
SALE_THRESHOLD = 1000
LOW_BONUS = 10
HIGH_BONUS = 15

get user_sale
while user_sale greater than or equal to 0
    if user_sale less than SALE_THRESHOLD
        user_bonus = user_sale x LOW_BONUS/PERCENTAGE_CONVERSION
    else
        user_bonus = user_sale x HIGH_BONUS/PERCENTAGE_CONVERSION
    display user_bonus
    get user_sale
        
"""
PERCENTAGE_CONVERSION = 100
SALE_THRESHOLD = 1000
LOW_BONUS = 10
HIGH_BONUS = 15

user_sale = float(input("Enter sales: $"))
while user_sale >= 0:
    if user_sale < SALE_THRESHOLD:
        user_bonus = user_sale * LOW_BONUS / PERCENTAGE_CONVERSION
    else:
        user_bonus = user_sale * HIGH_BONUS / PERCENTAGE_CONVERSION

    print(f"User Bonus: ${user_bonus}")
    user_sale = float(input("Enter sales: $"))
