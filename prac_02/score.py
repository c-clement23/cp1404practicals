"""
2. Debugging
============
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

# TODO: Fix this!

def get_score():
    score = float(input("Enter score: "))
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

def main():
    score = get_score()
    grade = determine_score(score)
    print(grade)
    random_score = random.randint(0,100)
    random_grade = determine_score(random_score)
    print(random_grade)

main()




