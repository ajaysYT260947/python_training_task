import csv
import json
import os

# ----------------------------------
# Task 1: Write names to names.txt
# ----------------------------------

names = ["Arun", "Priya", "Rahul", "Divya", "Karthik"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
        
print("Names from names.txt:")

with open("names.txt", "r") as file:
    print(file.read())


# ----------------------------------
# Task 2: Create and read students.csv
# ----------------------------------

# Read CSV and print students scoring above 60
print("\nStudents scoring above 60:")

with open("students.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for student in reader:
        if int(student["marks"]) > 60:
            print(f"{student['name']} {student['marks']}")


# ----------------------------------
# Task 3: Save students to students.json
# ----------------------------------
students = [
    {"name": "Arun", "marks": 55},
    {"name": "Priya", "marks": 67},
    {"name": "Rahul", "marks": 72},
    {"name": "Divya", "marks": 88},
    {"name": "Karthik", "marks": 45}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=2)

print("Students from students.json:")

with open("students.json", "r") as file:
    loaded_students = json.load(file)

for student in loaded_students:
    print(f"{student['name']}: {student['marks']}")


# ----------------------------------
# Task 4: Handle a missing file
# ----------------------------------

print("Checking for a missing file:")

try:
    with open("missing.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("missing.txt -> File not found")