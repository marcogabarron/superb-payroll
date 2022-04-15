# Superb Payroll

Superb Payroll is a system developed to help payroll specialists to control their employee's list, their start dates, ages, salary and department.
Superb Payroll saves data in a format that can be interpreted by every payslip generator software and can be processed in a secure and fast way. Superb Payroll generate a master file ready for processing.

Avoid errors in your master file and payroll processing confusions.

![Screens Screenshot](assets/images/screens-screenshot.png)

## Purpose 
------

Purpose of this project is to showcase my abilities in Python to accomplish project 3 of Code Institute course. 
Project was chosen to develop something meaningful to Payroll market. My wife as a payroll specialist had an important roll guiding me what could be useful to the market.
Project challenged my abilities and understanding of Python concepts taught on the course.

## User Experience
------

User experience designed to be a step by step on how to implement a master file in payroll.

- New employee entry user experience:
    - Information Requested in order that a master file accepts.
    - Relevant information is validated to make sure format of master file is kept.
    - Wrong format is rejected and explained the reason to the user.

## Features
------

### Existing Features

- Add new employee entry:
    - Generate employee ID number following the last employee ID number to avoid duplicated ID.
    - All information required to add a new employee entry is requested in a clear way to the user.
    - Relevant information is validated to make sure format of master file is kept.
    - After validation, information in the wrong format is rejected untill user enter information using the requested format.

![NewEmployeeEntry Screenshot](assets/images/header-screenshot.png)

- Search for employee ID:
    - User will be asked for a employee number.
    - Employee ID entry is validated.
    - System search for employee ID after validation if user exists.
    - All employee information with matching ID is presented to user in a friendly and clear way.

![SearchEmployeeID Screenshot](assets/images/gameoptions-screenshot.png)

- Input validation and error-checking:
    - You cannot enter wrong menu option. You must enter one of the options requested.
    - You must enter date of format dd/mm/yy.
    - You cannot enter inexistent employee ID.

![SearchEmployeeID Screenshot](assets/images/gameoptions-screenshot.png)

### Future Developmets

- Implement other methods of searching. 
- Implement update employee entry mehod.
- Add extra information collumns that can be entered.


## Data Model
------

I decided to use an Employee class as my model. The system creates one instance for new employee entry Employee class and one for search employee ID Employee class.

The employee class has two methods create_new_employee and show_employee.
The create_new_employee add a new row to google spreadsheet using all the data from the instance that is calling the method.
The show_employee method presents all the information of the instance Employee class to the user in a clear way.

## Testing
------

I have manually tested this project by doing this:

- Passed the code through a PEP8 linter and confirmed there are no problems.

- Given invalid inputs: strings when numbers are expected, wrong date format and wrong option number.

- Tested in my local terminal and the Code Institute Heroku terminal.

### Bugs

##### Solved Bugs

- Heroku deployment was giving me an error due to an extra line on requirements.txt. Once identified, line was removed and deployment complete successfully.

### Validator Testing

- PEP8: 
    - No errors were returned from PEP8online.com.

### Unfixed Bugs
No unfixed bugs

## Deployment
------

This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:
    - Fork or clone this repository.
    - Create a new Heroku App.
    - Add config var using credentials for google spreadsheet.
    - Add config var for PORT 8000.
    - Set the buildbacks to Python and NodeJS in that order.
    - Link the Heroku app to the repository.
    - Click on Deply.

The live link can be found here: <a href="https://superb-payroll.herokuapp.com/" target="_blank">Superb Payroll</a>

## Credits
------
- Code Institute for the deployment terminal.
- Love Sandwich project from CI for google spreadsheet and googleOAuth libraries.