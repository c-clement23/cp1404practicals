"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months):
    """Print Report with Totals after each month"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print_monthly_income_and_total(income, number_of_months, total)


def print_monthly_income_and_total(income, number_of_months, total):
    print(f"Month {number_of_months:2} - Income: ${income:10.2f}          Total: ${total:10.2f}")


main()