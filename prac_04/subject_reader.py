"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)

    display_subjects(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    # input_file = open(FILENAME)
    # for line in input_file:
    #     print(line)  # See what a line looks like
    #     print(repr(line))  # See what a line really looks like
    #     line = line.strip()  # Remove the \n
    #     parts = line.split(',')  # Separate the data into its parts
    #     print(parts)  # See what the parts look like (notice the integer is a string)
    #     parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
    #     print(parts)  # See if that worked
    #     print("----------")
    # input_file.close()
    data = []
    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data

def display_subjects(data):
    """Display subject information in readable format"""
    for subject_code, lecturer, student_count in data:
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")

main()