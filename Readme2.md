# 🎓 Student Registration System

## 📌 Description

This project consists of a command-line application developed in Python to manage student records for a school.  
It allows users to register, search, update, delete, and store student information using CSV files.

---

## 🚀 Features

- Register new students  
- Display all registered students  
- Search students by ID  
- Update student information  
- Delete student records  
- Save data to a CSV file  
- Load data from a CSV file  

---

## 🧱 Project Structure

The project is organized into the following modules:

### 📄 `app.py`
Entry point of the application.  
It initializes the system, loads existing data from the CSV file, and controls the main program loop.

---

### ⚙️ `processes.py`
Contains the core business logic of the system, including:

- Student registration  
- Displaying the student list  
- Searching for a student by ID  
- Updating student data  
- Deleting student records  

---

### ✅ `validations.py`
Provides reusable input validation functions to ensure data integrity, such as:

- Positive number validation  
- Non-empty text validation  
- Input format validation  

---

### 💾 `csv_manager.py`
Handles data persistence by managing CSV file operations, including:

- Saving student data to a CSV file  
- Loading student data from a CSV file  
- Validating file structure and handling invalid rows  

---

## 💾 Data Storage

The system stores data in:


Each record contains:

- `Id`
- `Name`
- `Age`
- `Program`
- `State` (True/False)

---

## 🛠 Technologies Used

- Python 🐍  
- CSV file handling (`csv` module)  
- Lists and dictionaries  
- Modular programming  
- Input validation  
- Exception handling  

---

## ▶️ How to Run

```bash
python app.py
```
📋 Menu Options
Register new student
Display student list
Search student
Update student
Delete student
Save CSV
Exit
🧠 Input Validation

The system ensures valid user input through reusable validation functions:

Prevents empty values
Ensures numeric inputs are positive
Avoids invalid data formats

This guarantees:

Data consistency
Better user experience
Reduced runtime errors
🧠 Design Principles
Separation of concerns (modular design)
Reusable validation functions
Clean and readable code
User-friendly interaction
📈 Future Improvements
Add email validation
Filter students by active/inactive status
Add search by name
Implement GUI interface
Migrate to a database (SQLite/MySQL)

Systems Engineer | Aspiring Software Developer