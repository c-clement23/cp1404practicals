def main():
    menu = ("(G)et a valid score\n"
            "(P)rint result\n"
            "(S)how stars\n"
            "(Q)uit")
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter Score: "))
            score = validate_score(score)
        elif choice == "P":
            print(determine_score(score))
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice!")
        print(menu)
        choice = input(">>> ").upper()
    print("Program ended!")

def validate_score(score):
    while score < 0 or score > 100:
        print("Invalid Score (must be in 0 - 100 range)")
        score = int(input("Enter Score: "))
    return score

def determine_score(score):
    if score < 0 or score > 100:
        grade = "Invalid score"
    elif score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade
main()
