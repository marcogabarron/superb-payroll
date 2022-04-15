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


class Employee:
    """
    Class to serve as a blueprint for employees.
    Parameter: employee ID, name, start date, date of birth,
    salary and department.
    Class has methods: create_new_employee and show_employee.
    """
    def __init__(
        self, employee_id, name, start_date,
        date_of_birth, salary, department
    ):
        self.employee_id = employee_id
        self.name = name
        self.start_date = start_date
        self.date_of_birth = date_of_birth
        self.salary = salary
        self.department = department

    def create_new_employee(self):
        """
        The create_new_employee add a new row to google spreadsheet
        using all the data from the instance that is calling the method.
        Worksheet: employee.
        """
        employee_worksheet = SHEET.worksheet("employee")
        data = [
            self.employee_id, self.name, self.start_date,
            self.date_of_birth, self.salary, self.department
            ]
        employee_worksheet.append_row(data)

    def show_employee(self):
        """
        The show_employee method presents all the information
        of the instance Employee class to the user in a clear way.
        """
        print(
            f"\nEmployee ID: {self.employee_id} \nName: {self.name} \
                \nStart Date: {self.start_date}\
                \nDate of Birth: {self.date_of_birth}\
                \nSalary: {self.salary} \nDepartment: {self.department}"
            )


def start_menu():
    """
    Start Menu to give user two options:
    1- Add new employee
    2- Search for employee ID
    Run a while loop to collect a valid string of data from the user
    Run validate_option function to option entry is correct.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print(
            "\nPlease choose one option: \n\
             1- Add new employee \n\
             2- Search for employee ID \n\
             3- Leave"
            )
        user_option = input(
            "\nEnter number 1, number 2 or number 3 for options:\n"
            )

        if validate_option(user_option):
            break

    if user_option == '1':
        new_entry()
    elif user_option == '2':
        search_employeeID()

    elif user_option == '3':
        end_menu()


def validate_option(user_option):
    """
    Validate if user_option is equal to 1, 2 or 3.
    Implementing a try except to validate user_option
    """
    try:
        if user_option != '1' and user_option != '2' and user_option != '3':
            raise ValueError(
                f"\nPlease select options number 1, 2 or 3,\
                 you provided {user_option}"
            )

    except ValueError as e:
        print(f"\nInvalid data: {e}, please try again.\n")
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
                f"Date Format invalid"
            )
    except ValueError as e:
        print(f"\nInvalid data: {e}, please try again.\n")
        return False

    return True


def validate_id(id):
    """
    Validate employee ID.
    Implementing a try except to validate employee ID entry.
    """
    employee_worksheet = SHEET.worksheet("employee")
    try:
        cell = employee_worksheet.find(id)
        if cell is None:
            raise TypeError(
                f"Employee ID not in the system"
            )
    except TypeError as e:
        print(f"\nEmployee ID not found: {e}, please try again.\n")
        return False

    return True


def new_entry():
    """
    Generate employee ID from the last ID registered.
    Request all the information in order to have everything
    for a payroll master file.
    Validation made using the right methods.
    """
    while True:
        print(
            "\nPlease choose one option: \n\
             1- Start New Entry \n\
             2- Return to Main Menu \n\
             3- Leave"
            )
        user_option = input(
            "\nEnter number 1, number 2 or number 3 for options:\n"
            )

        if validate_option(user_option):
            break

    if user_option == '1':

        employee_worksheet = SHEET.worksheet("employee")

        list_of_dicts = employee_worksheet.get_all_records()
        last_id = employee_worksheet.cell(len(list_of_dicts)+1, 1).value
        employee_id = int(last_id)+1

        name = input("\nPlease enter employee's name:\n")
        while True:
            start_date = input(
                "\nPlease enter employee's Start Date(dd/mm/yy):\n"
                )
            start_date_valid = start_date.replace("/", "")
            if validate_date(start_date_valid):
                break

        while True:
            date_birth = input(
                "\nPlease enter employee's Date of Birth(dd/mm/yy):\n"
                )
            date_birth_valid = date_birth.replace("/", "")
            if validate_date(date_birth_valid):
                break

        salary = input("Please enter employee's Salary:\n")

        department = input("Please enter employee's department:\n")

        print("New employee entry being created...\n")
        print(f"New employee ID number is: {employee_id}")
        new_employee = Employee(
            employee_id, name, start_date, date_birth, salary, department
            )
        new_employee.create_new_employee()
        print("\nEmployee worksheet updated successfully\n")

        new_entry()

    elif user_option == '2':
        start_menu()

    elif user_option == '3':
        end_menu()


def search_employeeID():
    """
    Search for employee ID.
    Ask the user for employee ID and
    search through employee list to find a match.
    """
    employee_worksheet = SHEET.worksheet("employee")
    while True:
        print("\nPlease choose one option: \n\
         1- Start Search for employee ID \n\
         2- List all employees \n\
         3- Return to Main Menu")
        user_option = input(
            "\nEnter number 1, number 2 or number 3 for options:\n"
            )

        if validate_option(user_option):
            break

    if user_option == '1':
        while True:
            id = input(
                "\nPlease enter employee ID:\n"
                )
            if validate_id(id):
                break

        cell = employee_worksheet.find(id)
        values_list = employee_worksheet.row_values(cell.row)
        found_employee = Employee(
            values_list[0], values_list[1],
            values_list[2], values_list[3], values_list[4], values_list[5]
            )
        found_employee.show_employee()

        search_employeeID()

    elif user_option == '2':
        list_of_dicts = employee_worksheet.get_all_values()
        for employee in list_of_dicts:
            if employee[0] == 'Employee ID':
                continue
            individual_employee = Employee(
                employee[0], employee[1], employee[2],
                employee[3], employee[4], employee[5]
                )
            individual_employee.show_employee()

        search_employeeID()

    elif user_option == '3':
        start_menu()


def end_menu():
    """
    Show good bye message and quits system.
    """
    print("\nGood Bye! Hope to see you soon.\n")
    quit()

start_menu()
