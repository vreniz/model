import csv
import os

DATA_FILE = os.path.join("data", "students.csv")


def read_students():
    """
    Reads all students from CSV file.

    Returns:
        list: List of student dictionaries
    """
    if not os.path.isfile(DATA_FILE):
        return []

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def create_student(student_data):
    """
    Adds a new student.

    Validates unique ID.

    Returns:
        bool
    """
    students = read_students()

    for student in students:
        if student["id"] == str(student_data["id"]):
            print("Error: Student ID already exists.")
            return False

    file_exists = os.path.isfile(DATA_FILE)

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=student_data.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(student_data)

    return True


def update_students_file(students):
    """
    Rewrites the CSV file with updated students.
    """
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)


def find_student_by_id(student_id):
    """
    Finds a student by ID.
    """
    students = read_students()

    for student in students:
        if student["id"] == str(student_id):
            return student

    return None


def update_student(student_id, new_data):
    """
    Updates student information.
    """
    students = read_students()
    updated = False

    for student in students:
        if student["id"] == str(student_id):
            student.update(new_data)
            updated = True

    if updated:
        update_students_file(students)

    return updated


def delete_student(student_id):
    """
    Deletes a student by ID.
    """
    students = read_students()
    new_students = [s for s in students if s["id"] != str(student_id)]

    if len(new_students) != len(students):
        update_students_file(new_students)
        return True

    return False
