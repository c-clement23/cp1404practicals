"""
Project Management Program
Estimated Time: 1.5 hours
"""
from html.parser import incomplete

from project import Project
import datetime

FILENAME = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    MENU = """- (L)oad projects
    - (S)ave projects
    - (D)isplay projects
    - (F)ilter projects by date
    - (A)dd new project
    - (U)pdate project
    -(Q)uit"""
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects(projects, date_str)
        elif choice == "a":
            project = add_project()
            projects.append(project)
        elif choice == "u":
            update_project(projects)



def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)
        return projects

def save_projects(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects: ")
    for project in incomplete:
        print(f" {project}")
    print("Completed projects: ")
    for project in complete:
        print(f" {project}")


def get_start_date(project):
    return project.start_date

def filter_projects(projects, date_string):
    import datetime
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [p for p in projects if p.start_date > filter_date]
        filtered = sorted(filtered_projects, key=get_start_date)
        for project in filtered:
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")

def add_project():
    name = input("Name: ")
    date_str = input("Satart date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    return Project(name, date_str, priority, cost, completion)

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project choice: "))
    project = projects[index]
    print(project)
    try:
        new_percent_str = input("New Percentage: ")
        new_priority_str = input("New Priority: ")

        new_percent = int(new_percent_str) if new_percent_str else None
        new_priority = int(new_priority_str) if new_priority_str else None

        project.update(new_percent, new_priority)
    except ValueError:
        print("Invalid input. Skipped update.")