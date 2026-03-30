from crudstudent import *
import re


def show_menu():
    """
    Displays menu options.
    """
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Register Student")
    print("2. List Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def read_positive_int(message):
    """
    Validates positive integer input.
    """
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("Must be a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Must be an integer.")


def read_text(message):
    """
    Validates text input.

    - Not empty
    - Not only numbers
    - Only letters, numbers and spaces
    """
    while True:
        text = input(message).strip()

        if not text:
            print("Field cannot be empty.")
            continue

        if text.isdigit():
            print("Cannot contain only numbers.")
            continue

        valid = True
        for c in text:
            if not (c.isalpha() or c.isdigit() or c.isspace()):
                valid = False
                break

        if not valid:
            print("Invalid format. Only letters, numbers and spaces.")
            continue

        return text


def get_student_data():
    """
    Collects student data.
    """
    return {
        "id": read_positive_int("Student ID: "),
        "name": read_text("Name: "),
        "age": read_positive_int("Age: "),
        "program": read_text("Program: "),
        "status": "active",
    }


def get_update_data():
    return {
        "name": read_text("Name: "),
        "age": read_positive_int("Age: "),
        "program": read_text("Program: "),
    }


if __name__ == "__main__":

    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            data = get_student_data()
            if create_student(data):
                print("Student registered successfully.")

        elif option == "2":
            students = read_students()
            if students:
                print("\nSTUDENTS:")
                for s in students:
                    print(s)
            else:
                print("No students found.")

        elif option == "3":
            try:
                student_id = int(input("Enter Student ID: "))
                result = find_student_by_id(student_id)
                print(result if result else "Not found.")
            except ValueError:
                print("Invalid ID.")

        elif option == "4":
            try:
                student_id = int(input("Enter ID to update: "))
                updated = update_student(student_id, get_update_data())
                print("Updated." if updated else "Not found.")
            except ValueError:
                print("Invalid ID.")

        elif option == "5":
            try:
                student_id = int(input("Enter ID to delete: "))
                print("Deleted." if delete_student(student_id) else "Not found.")
            except ValueError:
                print("Invalid ID.")

        elif option == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
