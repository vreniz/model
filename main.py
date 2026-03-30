"""
main.py — Entry point and user interface.

This file handles:
- Displaying the menu
- Reading user input
- Calling CRUD functions from crud.py
- Printing results

Adapt the menu options, fields, and function calls to your project.
"""

# ── Choose your storage format ───────────────
# JSON version  → use functions ending in _json
# CSV version   → use functions ending in _csv
# ─────────────────────────────────────────────
from crud import *
from validate import read_positive_int, read_text  # add more as needed


# ══════════════════════════════════════════════
#  MENU
# ══════════════════════════════════════════════

def show_menu():
    """Displays the main menu."""
    print("\n--- PROJECT NAME ---")        # ← change this
    print("1. Create record")
    print("2. List all records")
    print("3. Search record")
    print("4. Update record")
    print("5. Delete record")
    print("6. Exit")
    # Uncomment or add options as needed:
    # print("7. List active records")


# ══════════════════════════════════════════════
#  DATA COLLECTION
# ══════════════════════════════════════════════

def get_record_data():
    """
    Collects all fields for a new record from user input.

    Returns:
        dict: Record ready to be saved.

    Tip: use read_positive_int(), read_text(), read_float(),
         read_date() from validate.py for each field.
    """
    return {
        "id":     read_positive_int("ID: "),
        "name":   read_text("Name: "),
        # "price":  read_float("Price: "),          # uncomment if needed
        # "date":   read_date("Date (YYYY-MM-DD): "), # uncomment if needed
        "status": read_text("Status: "),
    }


# ══════════════════════════════════════════════
#  MAIN LOOP
# ══════════════════════════════════════════════

if __name__ == "__main__":
    while True:
        show_menu()
        option = input("Choose an option: ").strip()

        # ── 1. CREATE ────────────────────────────────
        if option == "1":
            data = get_record_data()

            # JSON version:
            if create_record_json(data):
                print("Record saved successfully.")

            # CSV version (comment out JSON and uncomment this):
            # if create_record_csv(data):
            #     print("Record saved successfully.")

        # ── 2. LIST ALL ──────────────────────────────
        elif option == "2":
            # JSON version:
            records = read_records_json()

            # CSV version:
            # records = read_records_csv()

            if records:
                print("\nAll records:")
                for r in records:
                    print(r)
            else:
                print("No records found.")

        # ── 3. SEARCH ────────────────────────────────
        elif option == "3":
            mode = input("Search by (1) ID or (2) Name: ").strip()

            if mode == "1":
                try:
                    record_id = int(input("ID: "))

                    # JSON version:
                    result = find_by_id_json(record_id)

                    # CSV version:
                    # result = find_by_id_csv(record_id)

                    print(result if result else "Not found.")
                except ValueError:
                    print("Invalid ID.")

            elif mode == "2":
                name = input("Name: ").strip()

                # JSON version:
                results = find_by_field_json("name", name)

                # CSV version:
                # results = find_by_field_csv("name", name)

                if results:
                    for r in results:
                        print(r)
                else:
                    print("No results found.")

        # ── 4. UPDATE ────────────────────────────────
        elif option == "4":
            try:
                record_id = int(input("ID of record to update: "))
                new_data = get_record_data()

                # JSON version:
                ok = update_record_json(record_id, "id", new_data)

                # CSV version:
                # ok = update_record_csv(record_id, "id", new_data)

                print("Updated." if ok else "Not found.")
            except ValueError:
                print("Invalid ID.")

        # ── 5. DELETE ────────────────────────────────
        elif option == "5":
            try:
                record_id = int(input("ID of record to delete: "))

                # JSON version:
                ok = delete_record_json(record_id)

                # CSV version:
                # ok = delete_record_csv(record_id)

                print("Deleted." if ok else "Not found.")
            except ValueError:
                print("Invalid ID.")

        # ── 6. EXIT ──────────────────────────────────
        elif option == "6":
            print("Goodbye!")
            break

        # ── EXTRA OPTION EXAMPLE (uncomment to use) ──
        # elif option == "7":
        #     list_active_records()   # define this in crud.py

        # ── INVALID OPTION ───────────────────────────
        else:
            print("Invalid option. Please choose a number from the menu.")
