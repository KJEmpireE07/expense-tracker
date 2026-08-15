import json
import csv
from datetime import datetime
import validators , storage , expense_manager
import data



def list_expenses():

    if data.expenses :
        expense_manager.display_expenses(data.expenses)
    else :
        print("No expenses added!! ADD or Load the expense in it.")



def cli_menu() :
    print("========== EXPENSE TRACKER ==========")
    print(
    """
    1. Add Expense
    2. Delete Expense
    3. List Expenses
    4. Filter by Category
    5. Monthly Summary
    6. Save expenses
    7. Load expenses
    8. CLI Menu
    9. Export CSV
    10. Edit Ids
    11. Search Expenses
    12. Sort Expenses
    13. Exit
    
    """

    )
   
def valid_option() :
    while True :
        try :
            option = int(input("Enter the option to continue: "))
            if option >= 1 and option <= 13 :
                return option
            print("Please enter the option within the range.")

        except ValueError :
            print("Please enter correct option.")



print("========== EXPENSE TRACKER ==========")
print(
    """
    1. Add Expense
    2. Delete Expense
    3. List Expenses
    4. Filter by Category
    5. Monthly Summary
    6. Save expenses
    7. Load expenses
    8. CLI Menu
    9. Export CSV
    10. Edit Ids
    11. Search Expenses
    12. Sort Expenses
    13. Exit
    
    """

)

while(True) :
    option = valid_option()

    if option == 1 :
        expense_manager.add_expense()
    elif option == 2 :
        expense_manager.delete_expense()
    elif option == 3 :
        list_expenses() 
    elif option == 4 :
        expense_manager.filter_by_category()
    elif option == 5 :
        expense_manager.get_monthly_summary()
    elif option == 6 :
        storage.save_expenses()
    elif option == 7 :
        storage.load_expenses()
    elif option == 8 :
        cli_menu()
    elif option == 9 :
        storage.export_csv()
    elif option == 10 :
        expense_manager.edit_expense()
    elif option == 11 :
        expense_manager.search_expenses()
    elif option == 12 :
        expense_manager.sort_expenses()
    elif option == 13 :
        break







