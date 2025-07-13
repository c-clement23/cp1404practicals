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
        elif choice == 'd':
            display_projects(projects)



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

