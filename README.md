# 💰 Expense Tracker

A command-line based Expense Tracker built with Python.

This project was created to practice Python fundamentals, modular programming, file handling, CRUD operations, input validation, searching, filtering, sorting, and basic version control with Git and GitHub.

---

## 🚀 Features

- ➕ Add expenses
- ✏️ Edit existing expenses
- 🗑️ Delete expenses
- 📋 List all expenses
- 🔎 Search expenses
- 🏷️ Filter expenses by category
- 📊 Sort expenses
  - Amount: Low to High
  - Amount: High to Low
  - Date: Oldest to Newest
  - Date: Newest to Oldest
  - Category: A to Z
- 📅 Monthly expense summary
- 💾 Save expenses to JSON
- 📂 Load expenses from JSON
- 📄 Export expenses to CSV
- ✅ Input validation
- 📆 Date validation
- 🆔 Automatic expense ID generation

---

## 🛠️ Technologies Used

- **Python 3**
- JSON
- CSV
- Git
- GitHub

The project uses Python's built-in modules such as:

- `json`
- `csv`
- `datetime`

No external Python packages are required.

---

## 📁 Project Structure

```text
expense-tracker/
│
├── main.py                 # Program entry point and CLI menu
├── data.py                 # Shared expense data
├── validators.py           # Input validation functions
├── expense_manager.py     # Expense management operations
├── storage.py              # JSON and CSV file operations
├── expenses.json           # JSON expense data
├── expenses.csv            # CSV export
├── .gitignore              # Git ignored files
└── README.md               # Project documentation