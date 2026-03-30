"""
crud.py — Data layer for the project.
Handles all read/write operations for both CSV and JSON formats.

To switch between formats, just change the DATA_FILE path and
use the corresponding set of functions (JSON or CSV section).
"""

import json
import csv
import os

# ─────────────────────────────────────────────
#  FILE PATHS — change these to match your project
# ─────────────────────────────────────────────
DATA_FOLDER = "data"
DATA_JSON   = os.path.join(DATA_FOLDER, "data.json")
DATA_CSV    = os.path.join(DATA_FOLDER, "data.csv")


def _ensure_folder():
    """Creates the data folder if it doesn't exist."""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)


# ══════════════════════════════════════════════
#  JSON SECTION
# ══════════════════════════════════════════════

def read_records_json():
    """
    Reads all records from the JSON file.

    Returns:
        list: List of record dictionaries. Empty list if file doesn't exist.
    """
    if not os.path.isfile(DATA_JSON):
        return []

    with open(DATA_JSON, "r", encoding="utf-8") as file:
        return json.load(file)


def _save_records_json(records):
    """
    Overwrites the JSON file with the given list of records.

    Args:
        records (list): List of dictionaries to save.
    """
    _ensure_folder()
    with open(DATA_JSON, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)


def create_record_json(record):
    """
    Adds a new record to the JSON file.

    Validates:
    - Unique ID (compares record["id"] against existing records)

    Args:
        record (dict): Record to add.

    Returns:
        bool: True if saved, False if ID already exists.
    """
    records = read_records_json()

    # ── Unique ID check ──────────────────────
    for r in records:
        if r["id"] == record["id"]:
            print("Error: A record with this ID already exists.")
            return False

    records.append(record)
    _save_records_json(records)
    return True


def update_record_json(id_value, id_field, new_data):
    """
    Finds a record by a given field and updates it.

    Args:
        id_value: Value to search for (e.g., 1001).
        id_field (str): Field name to match (e.g., "id").
        new_data (dict): Fields to update.

    Returns:
        bool: True if updated, False if not found.
    """
    records = read_records_json()
    updated = False

    for r in records:
        if r[id_field] == id_value:
            r.update(new_data)
            updated = True

    if updated:
        _save_records_json(records)

    return updated


def delete_record_json(id_value, id_field="id"):
    """
    Deletes a record from the JSON file by field match.

    Args:
        id_value: Value to search for.
        id_field (str): Field name to match (default: "id").

    Returns:
        bool: True if deleted, False if not found.
    """
    records = read_records_json()
    filtered = [r for r in records if r[id_field] != id_value]

    if len(filtered) != len(records):
        _save_records_json(filtered)
        return True

    return False


def find_by_id_json(id_value, id_field="id"):
    """
    Returns the first record matching the given ID.

    Args:
        id_value: Value to search for.
        id_field (str): Field to match (default: "id").

    Returns:
        dict | None
    """
    for r in read_records_json():
        if r[id_field] == id_value:
            return r
    return None


def find_by_field_json(field, value):
    """
    Returns all records where field contains value (partial, case-insensitive).

    Args:
        field (str): Field name to search in (e.g., "name").
        value (str): Value to look for.

    Returns:
        list: Matching records.
    """
    value = value.strip().lower()
    return [r for r in read_records_json() if value in str(r.get(field, "")).lower()]


# ══════════════════════════════════════════════
#  CSV SECTION
# ══════════════════════════════════════════════

def read_records_csv():
    """
    Reads all records from the CSV file.

    Returns:
        list: List of record dictionaries. Empty list if file doesn't exist.

    Note:
        All values from CSV are strings. Cast them as needed (e.g., int(r["id"])).
    """
    if not os.path.isfile(DATA_CSV):
        return []

    with open(DATA_CSV, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def _save_records_csv(records):
    """
    Overwrites the CSV file with the given list of records.

    Args:
        records (list): List of dictionaries to save. Must be non-empty.
    """
    _ensure_folder()
    with open(DATA_CSV, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)


def create_record_csv(record):
    """
    Adds a new record to the CSV file.

    Validates:
    - Unique ID (compares as string since CSV stores everything as text)

    Args:
        record (dict): Record to add.

    Returns:
        bool: True if saved, False if ID already exists.
    """
    records = read_records_csv()

    # ── Unique ID check (CSV stores values as strings) ──
    for r in records:
        if r["id"] == str(record["id"]):
            print("Error: A record with this ID already exists.")
            return False

    file_exists = os.path.isfile(DATA_CSV)
    _ensure_folder()

    with open(DATA_CSV, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=record.keys())
        if not file_exists:
            writer.writeheader()  # Write column headers on first record
        writer.writerow(record)

    return True


def update_record_csv(id_value, id_field, new_data):
    """
    Finds a record by a given field and updates it.

    Args:
        id_value: Value to search for (will be compared as string).
        id_field (str): Field name to match.
        new_data (dict): Fields to update.

    Returns:
        bool: True if updated, False if not found or file is empty.
    """
    records = read_records_csv()
    if not records:
        return False

    updated = False

    for r in records:
        if r[id_field] == str(id_value):
            r.update(new_data)
            updated = True

    if updated:
        _save_records_csv(records)

    return updated


def delete_record_csv(id_value, id_field="id"):
    """
    Deletes a record from the CSV file by field match.

    Args:
        id_value: Value to search for (compared as string).
        id_field (str): Field name to match (default: "id").

    Returns:
        bool: True if deleted, False if not found.
    """
    records = read_records_csv()
    if not records:
        return False

    filtered = [r for r in records if r[id_field] != str(id_value)]

    if len(filtered) != len(records):
        _save_records_csv(filtered)
        return True

    return False


def find_by_id_csv(id_value, id_field="id"):
    """
    Returns the first record matching the given ID.

    Args:
        id_value: Value to search for (compared as string).
        id_field (str): Field to match (default: "id").

    Returns:
        dict | None
    """
    for r in read_records_csv():
        if r[id_field] == str(id_value):
            return r
    return None


def find_by_field_csv(field, value):
    """
    Returns all records where field contains value (partial, case-insensitive).

    Args:
        field (str): Field name to search in.
        value (str): Value to look for.

    Returns:
        list: Matching records.
    """
    value = value.strip().lower()
    return [r for r in read_records_csv() if value in str(r.get(field, "")).lower()]
