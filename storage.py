import json
import csv
import expense_manager
import data

def save_expenses() :
    if data.expenses != [] :
    
        with open("expenses.json", "w") as file :
            json.dump(data.expenses, file, indent=4)

        print("Successfully saved the expenses!")

    else :
        print("No expenses to save!")
    


def load_expenses() :

    if data.expenses == [] :

        try :


            with open("expenses.json","r") as file :
                data.expenses = json.load(file)

            print("Successfully loaded expenses!")
        except FileNotFoundError:
            print("No expenses saved")

    else :
        print("Expenses already exits!")


def export_csv() :
    if not data.expenses :
        print("No expenses to export")
    else :
        with open("expenses.csv", "w", newline="") as file :
            writer = csv.writer(file)

            writer.writerow(['Id','Amount','Category','Description','Date'])

            for expense in data.expenses :
                writer.writerow([expense['Id'],expense['Amount'],expense['Category'],expense['Description'],expense['Date']])
        print("Expenses exported successfully!")