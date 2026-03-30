# 🗂️ Python CRUD Template

A clean, reusable starting point for console-based CRUD projects with **JSON** and **CSV** persistence.

Built from real project experience — everything is commented and ready to adapt.

---

## 📁 Project Structure

```
project/
│
├── main.py        ← Menu, user interaction, calls to crud functions
├── crud.py        ← All read/write logic (JSON and CSV)
├── validate.py    ← Input validation helpers (reusable)
├── data/
│   ├── data.json  ← Created automatically on first run (JSON mode)
│   └── data.csv   ← Created automatically on first run (CSV mode)
└── README.md
```

---

## ⚡ Quick Start

**1. Clone or copy the project folder.**

**2. Run the program:**
```bash
python3 main.py
```

The `data/` folder and files are created automatically — no setup needed.

---

## 🔀 Choosing JSON or CSV

Each CRUD operation has both versions available. In `main.py`, simply use the version you need:

```python
# JSON version (default)
if create_record_json(data):
    print("Saved.")

# CSV version — comment out JSON and uncomment this:
# if create_record_csv(data):
#     print("Saved.")
```

Same pattern for read, update, delete, and search.

> **Tip:** Stick to one format per project. Mixing both in the same run can cause confusion.

---

## 📦 Available Functions

### JSON
| Function | Description |
|---|---|
| `read_records_json()` | Returns all records as a list |
| `create_record_json(record)` | Adds a record, validates unique ID |
| `update_record_json(id, field, data)` | Updates matching record |
| `delete_record_json(id, field)` | Deletes matching record |
| `find_by_id_json(id)` | Returns first match by ID |
| `find_by_field_json(field, value)` | Partial search across any field |

### CSV
| Function | Description |
|---|---|
| `read_records_csv()` | Returns all records as a list of strings |
| `create_record_csv(record)` | Adds a record, validates unique ID |
| `update_record_csv(id, field, data)` | Updates matching record |
| `delete_record_csv(id, field)` | Deletes matching record |
| `find_by_id_csv(id)` | Returns first match by ID |
| `find_by_field_csv(field, value)` | Partial search across any field |

> ⚠️ **CSV note:** All values are stored and read as **strings**. Cast them when needed:
> ```python
> age = int(record["age"])
> price = float(record["price"])
> ```

---

## ✅ Validation Helpers (`validate.py`)

| Function | Returns | Use for |
|---|---|---|
| `read_positive_int(message)` | `int` | IDs, quantities, room numbers |
| `read_float(message)` | `float` | Prices, scores |
| `read_text(message)` | `str` | Names, statuses, categories |
| `read_date(message)` | `str` | Dates in YYYY-MM-DD format |
| `validate_date_range(start, end)` | `bool` | Check end > start |

Two more are available **commented out** in `validate.py`:
- `read_email()` — validates email format with regex
- `read_option()` — restricts input to a list of valid choices

---

## 🛠️ How to Adapt This Template

### Step 1 — Define your fields in `get_record_data()` (`main.py`)
```python
def get_record_data():
    return {
        "id":       read_positive_int("Client ID: "),
        "name":     read_text("Name: "),
        "plan":     read_text("Plan (monthly/annual): "),
        "status":   read_text("Status (active/inactive): "),
    }
```

### Step 2 — Add menu options in `show_menu()` (`main.py`)
```python
def show_menu():
    print("\n--- GYM MANAGEMENT ---")
    print("1. Add client")
    print("2. List clients")
    ...
```

### Step 3 — Add extra CRUD functions in `crud.py` if needed
```python
def list_active_records_json():
    records = read_records_json()
    active = [r for r in records if r["status"].lower() == "active"]
    for r in active:
        print(r)
```

---

## 🐛 Common Mistakes

| Mistake | Fix |
|---|---|
| `input(...).strip` without `()` | Always call `.strip()` with parentheses |
| Saving name with trailing space | Use `.strip()` on every text input |
| CSV ID comparison fails | CSV stores everything as strings — compare with `str(id_value)` |
| Searching by exact name only | Use `value in field.lower()` for partial matches |
| No `try/except` on int inputs | Wrap `int(input(...))` in try/except ValueError |

---

## 📋 Checklist Before Submitting

- [ ] Unique ID validation on create
- [ ] `try/except` on all numeric inputs
- [ ] `.strip()` on all text inputs
- [ ] Empty list message when no records exist
- [ ] Partial search (not exact match only)
- [ ] Docstrings on all functions
- [ ] `data/` folder created automatically
