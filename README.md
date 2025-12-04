📘 README.md (Full Version)
# 📚 Library Inventory Manager  
### Mini Project – Programming for Problem Solving using Python  
#### Object-Oriented Design • JSON Persistence • CLI • Exception Handling • Logging

---

## 📌 Project Overview
The **Library Inventory Manager** is a Python-based mini project designed to help campus libraries manage their collection of books using a simple **command-line interface (CLI)**.

This project demonstrates:
- Object-Oriented Programming (OOP)
- File handling with JSON
- Exception handling and logging
- Modular package structure
- Simple, interactive text-based menus

The system allows library staff to:
- Add new books  
- Issue and return books  
- Search catalog entries  
- View all books  
- Maintain persistent data storage  

---

## 🎯 Learning Objectives (As per Assignment)
By completing this project, the learner demonstrates the ability to:

- ✔ Use classes, objects, attributes, and methods  
- ✔ Apply OOP principles: encapsulation, magic methods, modular design  
- ✔ Store data persistently using JSON  
- ✔ Use `pathlib` for file operations  
- ✔ Safely handle missing or corrupted files  
- ✔ Build a functional CLI menu  
- ✔ Implement `try–except–finally` blocks  
- ✔ Use Python logging with appropriate log levels  
- ✔ Organize the project into a structured Python package  

---

## 🏗️ Project Folder Structure


library-inventory-manager-<yourname>/
├── library_manager/
│ ├── init.py
│ ├── book.py
│ └── inventory.py
├── cli/
│ └── main.py
├── catalog.json
├── library.log
├── README.md
├── requirements.txt
└── .gitignore


---

## ⚙️ Installation & Setup

### **1️⃣ Clone the repository**


git clone https://github.com/
<yourusername>/library-inventory-manager-<yourname>.git
cd library-inventory-manager-<yourname>


### **2️⃣ Make sure Python is installed**
Recommended: Python **3.8+**

### **3️⃣ Run the program**


python cli/main.py


No external libraries are required — everything is built into Python.

---

## 🖥️ How the CLI Works

Once the program runs, you will see:



------ Library Inventory Manager ------

Add Book

Issue Book

Return Book

View All Books

Search Book

Exit


### ✔ Features Available

| Option | Function |
|-------|----------|
| 1 | Add a new book |
| 2 | Issue a book by ISBN |
| 3 | Return a book by ISBN |
| 4 | Display all books |
| 5 | Search books by title |
| 6 | Close the program |

---

## 📚 JSON File Handling

### `catalog.json`
- Stores all books persistently  
- Automatically created if missing  
- Handles corruption safely using try–except  

Example JSON entry:
```json
{
    "title": "Python Basics",
    "author": "Eric Matthes",
    "isbn": "12345",
    "status": "available"
}

🧱 Mapping Project Tasks to Files
✔ Task 1 — Book Class

Located in:

library_manager/book.py


Includes:

__init__()

__str__()

to_dict()

issue()

return_book()

is_available()

✔ Task 2 — Inventory Manager

Located in:

library_manager/inventory.py


Includes:

add_book()

search_by_title()

search_by_isbn()

display_all()

✔ Task 3 — JSON File Persistence

Handled in:

load()

save()

Uses:

json module

pathlib.Path

exception handling for corrupted files

✔ Task 4 — Menu-Driven CLI

Located in:

cli/main.py


Provides interactive menu with validation.

✔ Task 5 — Exception Handling & Logging

try–except–finally used throughout

Logging setup using:

logging.basicConfig(level=logging.INFO)

✔ Task 6 — Packaging

Project structured as a Python package

Includes:

__init__.py

README.md

requirements.txt

.gitignore

🧪 Bonus: Unit Tests (Optional)

You can add tests inside:

/tests


Example:

def test_add_book():
    ...

📜 Logging

All events (add, issue, return, save, load errors) are logged in:

library.log


Log levels used:

INFO

WARNING

ERROR

📦 Requirements

requirements.txt includes:

json
pathlib
logging


(Standard Python libraries — no installation needed)


📑 Academic Integrity

This project is created for educational purposes.
Do not submit work copied from others.
If you use code from external sources, cite them clearly.

✔️ Final Notes

This project fully satisfies:

OOP

JSON

CLI

Exceptions

Logging

Packaging

Documentation
