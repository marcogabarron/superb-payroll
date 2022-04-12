import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('superb-payroll')

def start_menu():
    """
    Start Menu to give user two options: 1- Add new employee  2- Search for employee ID
    Run a while loop to collect a valid string of data from the user
    Run validate_option function to option entry is correct. 
    The loop will repeatedly request data, until it is valid.
    """
    while True: 
        print("Please choose one option: \n 1- Add new employee \n 2- Search for employee ID\n")
        user_option = input("Enter number 1 for option 1 or number 2 for option 2:\n")

        if validate_option(user_option):
            break

    if user_option == '1':
        new_entry()
    elif user_option == '2':
        search_employeeID()

def validate_option(user_option):
    """
    Validate if user_option is equal to 1 or 2.
    Implementing a try except to validate user_option
    """
    try:
        if user_option != '1' and user_option != '2':
            raise ValueError(
                f"Please select options number 1 or 2, you provided {user_option}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True

def validate_date(date):
    """
    Validate date.
    Implementing a try except to validate date entry.
    """
    try:
        [int(value) for value in date]
        if len(date) != 6:
            raise ValueError(
                f"Date Format invalid."
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True 

def new_entry():
    """
    Add a new employee to the system. Write a new employee row on google sheets
    """
    while True: 
        print("Please choose one option: \n 1- Start New Entry \n 2- Return to Main Menu\n")
        user_option = input("Enter number 1 for option 1 or number 2 for option 2:\n")

        if validate_option(user_option):
            break

    if user_option == '1':

        employee_worksheet = SHEET.worksheet("employee")

        list_of_dicts = employee_worksheet.get_all_records()
        last_id = employee_worksheet.cell(len(list_of_dicts)+1 , 1).value
        employee_id = int(last_id)+1

        name = input("Please enter employee's name:\n")
        while True:
            start_date = input("Please enter employee's Start Date(dd/mm/yy):\n")
            start_date_valid = start_date.replace("/", "")
            if validate_date(start_date_valid):
                break
        
        while True:
            date_birth = input("Please enter employee's Date of Birth(dd/mm/yy):\n")
            date_birth_valid = date_birth.replace("/", "")
            if validate_date(date_birth_valid):
                break

        salary = input("Please enter employee's Salary:\n")

        department = input("Please enter employee's department:\n")
        # print("Please enter number to choose department:\n 1- Administration\n 2- Sales\n 3- Service\n 4- Management\n")
        # department_entry = input("Enter number 1 for option 1, number 2 for option 2, number 3 for option 3 or number 4 for option 4:\n")

        print("New employee entry being created...\n")
        data = [employee_id, name, start_date, date_birth, salary, department]
        employee_worksheet.append_row(data)
        print("Employee worksheet updated successfully\n")


    elif user_option == '2':
        start_menu()


def search_employeeID():
    """
    Search for employee ID.
    Ask the user for employee ID and search through employee list to find a match.
    """
    employee_worksheet = SHEET.worksheet("employee")

    id = input("Please enter employee ID:\n")
    cell = employee_worksheet.find(id)
    values_list = employee_worksheet.row_values(cell.row)
    print(f"Employee ID: {values_list[0]} \nName: {values_list[1]} \nStart Date: {values_list[2]} \nDate of Birth: {values_list[3]} \nSalary: {values_list[4]} \nDepartment: {values_list[5]}\n")

# def get_data():
#     """
#     Get sales figures input from the user.
#     """
#     print("Please enter sales data from the last market.")
#     print("Data should be six numbers, separated by commas.")
#     print("Example: 10,20,30,40,50,60\n")

#     data = ["0030", "Maria", "09/10/2009", "09/10/1990", "80000", "Sales"]
#     employee_worksheet = SHEET.worksheet("employee")
#     # employee_worksheet.append_row(data)

    
#     cell = employee_worksheet.find("0030")
#     list_of_dicts = employee_worksheet.get_all_records()
#     print(list_of_dicts)
#     value = employee_worksheet.cell(len(list_of_dicts)+1 , 1).value
#     print(int(value)+1)

#     if cell == None:
#         print("Nothing equal, please go ahead")
#         # values_list = employee_worksheet.row_values(cell.row)
#         # print(values_list)




start_menu()
# get_data()