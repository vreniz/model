"""
validate.py — Input validation helpers.

All functions here read from the user (via input()) and loop
until a valid value is entered. Import and call them from main.py.

Uncomment the sections you need for your project.
"""

import re
from datetime import datetime


# ══════════════════════════════════════════════
#  NUMBERS
# ══════════════════════════════════════════════

def read_positive_int(message):
    """
    Reads a positive integer from user input.

    Args:
        message (str): Prompt shown to the user.

    Returns:
        int: A valid integer greater than 0.
    """
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("Must be a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(message):
    """
    Reads a positive decimal number from user input.
    Accepts both '.' and ',' as decimal separators.

    Args:
        message (str): Prompt shown to the user.

    Returns:
        float: A valid positive float.
    """
    pattern = r"^\d+([.,]\d+)?$"

    while True:
        value = input(message).strip()

        if not value:
            print("Value cannot be empty.")
            continue

        if not re.match(pattern, value):
            print("Invalid format. Examples: 10  /  10.5  /  10,5")
            continue

        value = float(value.replace(",", "."))

        if value <= 0:
            print("Must be greater than 0.")
        else:
            return value


# ══════════════════════════════════════════════
#  TEXT
# ══════════════════════════════════════════════

def read_text(message):
    """
    Reads a non-empty text string from user input.

    Rules:
    - Cannot be empty
    - Cannot be only numbers
    - Only letters, digits, and spaces allowed

    Args:
        message (str): Prompt shown to the user.

    Returns:
        str: Valid text input.
    """
    while True:
        text = input(message).strip()

        if not text:
            print("Field cannot be empty.")
            continue

        if text.isdigit():
            print("Cannot be only numbers.")
            continue

        valid = all(c.isalpha() or c.isdigit() or c.isspace() for c in text)

        if not valid:
            print("Invalid format. Only letters, numbers, and spaces allowed.")
            continue

        return text


# ══════════════════════════════════════════════
#  DATES
# ══════════════════════════════════════════════

def read_date(message):
    """
    Reads a date in YYYY-MM-DD format from user input.

    Args:
        message (str): Prompt shown to the user.

    Returns:
        str: Valid date string in YYYY-MM-DD format.
    """
    while True:
        date_str = input(message).strip()

        if not date_str:
            print("Date cannot be empty.")
            continue

        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid format. Use YYYY-MM-DD (e.g., 2025-03-15).")


def validate_date_range(start, end):
    """
    Validates that end date is strictly after start date.

    Args:
        start (str): Start date in YYYY-MM-DD format.
        end (str): End date in YYYY-MM-DD format.

    Returns:
        bool: True if valid range, False otherwise.
    """
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date   = datetime.strptime(end,   "%Y-%m-%d")

    if end_date <= start_date:
        print("End date must be after start date.")
        return False

    return True


# ══════════════════════════════════════════════
#  EMAIL  (uncomment if needed)
# ══════════════════════════════════════════════

# def read_email(message):
#     """
#     Reads and validates an email address using regex.
#
#     Args:
#         message (str): Prompt shown to the user.
#
#     Returns:
#         str: Valid email address.
#     """
#     pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
#
#     while True:
#         email = input(message).strip()
#
#         if not email:
#             print("Email cannot be empty.")
#             continue
#
#         if " " in email:
#             print("Email cannot contain spaces.")
#             continue
#
#         if not re.match(pattern, email):
#             print("Invalid format. Example: user@gmail.com")
#             continue
#
#         return email


# ══════════════════════════════════════════════
#  OPTION SELECTOR  (uncomment if needed)
# ══════════════════════════════════════════════

# def read_option(message, valid_options):
#     """
#     Reads a menu option and validates it against a list.
#
#     Args:
#         message (str): Prompt shown to the user.
#         valid_options (list): Accepted values (e.g., ["1", "2", "3"]).
#
#     Returns:
#         str: A valid option from the list.
#
#     Example:
#         mode = read_option("Choose (1) CSV or (2) JSON: ", ["1", "2"])
#     """
#     while True:
#         option = input(message).strip()
#         if option in valid_options:
#             return option
#         print(f"Invalid option. Choose from: {', '.join(valid_options)}")
