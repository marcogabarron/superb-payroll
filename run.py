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
        user_option = input("Enter number 1 for option 1 or number 2 for option 2\n")

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


def new_entry():
    """
    Add a new employee to the system. Write a new employee row on google sheets
    """
    print("Add employee")

def search_employeeID():
    """
    Search for employee ID.
    Ask the user for employee ID and search through employee list to find a match.
    """
    print("Search employee ID")

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