import validators
from datetime import datetime
import data

def display_expenses(expenses_to_display):
    if not expenses_to_display:
        print("No expenses to display.")
        return

    print("\n========== EXPENSES ==========")

    print(
        f"{'ID':<5}"
        f"{'Amount':<12}"
        f"{'Category':<15}"
        f"{'Description':<20}"
        f"{'Date'}"
    )

    print("-" * 65)

    for expense in expenses_to_display:
        print(
            f"{expense['Id']:<5}"
            f"₹{expense['Amount']:<11}"
            f"{expense['Category']:<15}"
            f"{expense['Description']:<20}"
            f"{expense['Date']}"
        )

def add_expense() :
    expense = {}
    amount = validators.get_valid_amount()
    category = validators.get_valid_category()
    description = validators.get_valid_description()
    date = validators.get_valid_date()

    expense['Id'] = data.get_next_id()
    expense['Amount'] = amount
    expense['Category'] = category
    expense['Description'] = description
    expense['Date'] = date

    data.expenses.append(expense)

def edit_expense():
    expense_id = int(input("Enter the id to edit: "))
    found = False
    updated = False

    for expense in data.expenses:

        if expense['Id'] == expense_id:
            found = True

            print("Current expense:")
            print("Amount:", expense['Amount'])
            print("Category:", expense['Category'])
            print("Description:", expense['Description'])
            print("Date:", expense['Date'])

            print("""
========== EDIT EXPENSE ==========

1. Amount
2. Category
3. Description
4. Date
5. Cancel
""")

            while True:
                choice = int(input("Choose what to edit: "))

                if choice == 1:
                    expense['Amount'] = validators.get_valid_amount()
                    updated = True

                elif choice == 2:
                    expense['Category'] = validators.get_valid_category()
                    updated = True

                elif choice == 3:
                    expense['Description'] = validators.get_valid_description()
                    updated = True

                elif choice == 4:
                    expense['Date'] = validators.get_valid_date()
                    updated = True

                elif choice == 5:
                    print("Edit cancelled.")
                    break

                else:
                    print("Invalid choice. Please choose 1-5.")

            break

    if not found:
        print("No such id found.")
    elif updated:
        print("Expense updated successfully!")

def delete_expense() :
    expense_id = int(input("Enter the Id no you wanna delete: "))

    found = False
    for expense in data.expenses :
        if expense['Id'] == expense_id :
            found = True
            data.expenses.remove(expense)
            print("Successfully removed the expense!")
            break
    if not found :
        print("No such expense with this id!")

def search_expenses():
    keyword = input("Enter search keyword: ").strip().lower()

    matching_expenses = []

    for expense in data.expenses:
        if (
            keyword in expense['Category'].lower()
            or keyword in expense['Description'].lower()
            or keyword in expense['Date'].lower()
        ):
            matching_expenses.append(expense)

    if matching_expenses:
        display_expenses(matching_expenses)
    else:
        print("No matching expenses found.")

def filter_by_category():
    category = input("Enter the category name: ").strip().lower()

    filtered_expenses = []

    for expense in data.expenses:
        if expense['Category'].lower() == category:
            filtered_expenses.append(expense)

    if filtered_expenses:
        display_expenses(filtered_expenses)
    else:
        print("No expenses found for this category!")

def sort_expenses():

    print("""
========== SORT EXPENSES ==========

1. Amount — Low to High
2. Amount — High to Low
3. Date — Oldest to Newest
4. Date — Newest to Oldest
5. Category — A to Z
6. Cancel
""")

    choice = int(input("Choose sorting option: "))

    if choice == 1:
        sorted_expenses = sorted(
            data.expenses,
            key=lambda expense: expense['Amount']
        )

    elif choice == 2:
        sorted_expenses = sorted(
            data.expenses,
            key=lambda expense: expense['Amount'],
            reverse=True
        )

    elif choice == 3:
        sorted_expenses = sorted(
            data.expenses,
            key=lambda expense: datetime.strptime(
                expense['Date'],
                "%d/%m/%Y"
            )
        )

    elif choice == 4:
        sorted_expenses = sorted(
            data.expenses,
            key=lambda expense: datetime.strptime(
                expense['Date'],
                "%d/%m/%Y"
            ),
            reverse=True
        )

    elif choice == 5:
        sorted_expenses = sorted(
            data.expenses,
            key=lambda expense: expense['Category'].lower()
        )

    elif choice == 6:
        return

    else:
        print("Invalid choice.")
        return

    display_expenses(sorted_expenses)

def get_monthly_summary() :
    month = input("Enter month (MM/YYYY): ")

    print("\n========== Monthly Summary ==========")
    summary = {}
    totalAmount = 0
    found = False
    for expense in data.expenses :
        if month in expense['Date'] :
            found = True
            category = expense['Category']

            summary[category] = summary.get(category, 0) + expense['Amount']

    if found == True :
        for key,value in sorted(summary.items()) :
            totalAmount+= value
            print(
                f"{key:<10}"
                f"₹{value:<10}"
            )
        print("-" * 15)
        print(
                f"{'Total':<10}"
                f"₹{totalAmount:<10}"
            )

    else :
        print("No expenses found this month!")

