from datetime import datetime
from data import expenses

def get_valid_amount() :
    while True :
        try :
            amount = float(input("Enter the amount: "))
            if amount > 0 :
                return amount
            else :
                print("Enter number greater than zero.")
        except ValueError :
            print("Invalid amount. Please enter a number.")
   
def get_valid_category():
    while True:
        category = input("Enter the category: ").strip()

        if category:
            return category

        print("Category cannot be empty.")

def get_valid_description():
    while True:
        description = input("Enter the description: ").strip()

        if description:
            return description

        print("Description cannot be empty.")

def get_valid_date() :
    while True :
        try :
            date_string = input("Enter the date: ").strip()
            date_object = datetime.strptime(date_string, "%d/%m/%Y" ) # %Y for  4 digit year and %y for 2 digit year

            return date_object.strftime("%d/%m/%Y")
        except ValueError:
            print("Incorrect date format. Enter again!")

def get_next_id() :
    if expenses == [] :
        return 1
    else :
        max_id = 0
        for expense in expenses :
            if expense['Id'] > max_id :
                max_id = expense['Id']

        return max_id + 1