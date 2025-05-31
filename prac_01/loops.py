"""
3. Loops
========

"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
a. count in 10s from 0 to 100
"""
for i in range(0, 101, 10):
    print(i, end=" ")
print()

"""
b. count down from 20 to 1
"""
for i in range(20, 0, -1):
    print(i, end=" ")
print()

"""
c. print n stars from user input
"""
star_numbers = int(input("Number of stars: "))
for i in range(1, star_numbers + 1):
    print("*", end="")

"""
d. print n lines of increasing stars
"""
star_numbers = int(input("Number of stars: "))
for i in range(1, star_numbers + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()