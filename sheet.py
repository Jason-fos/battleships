"""
Sheet.py contains validation

"""
# Imports
import gspread
from google.oauth2.service_account import Credentials
# Constants
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('battleships')
USERS = SHEET.worksheet('users')


def login_info():
    """
    Function to get data from the worksheet
    to validate log in information provided
    by the user

    """
    user_login = USERS.get_all_records()
    return user_login


def update_login_info(data):
    """
    Function to update the users worksheet
    with new username and password information
    provided by the user

    """
    USERS.append_row(data)


def validate_info(user, password):
    """
    Function that checks if the username already
    exists and that the password and username info
    provided by the user are valid. It will provide
    the user with an error if invalid data is entered

    """
    try:
        if len(user) < 6 or len(password) < 6:
            raise ValueError(
                'Username and password need to be min of 5 characters\n'
                )
    except ValueError:
        print('Input not valid')
        return False
    try:
        existing = login_info()
        for ex in existing:
            if ex['USERNAME'] == user:
                raise ValueError(
                    'Username exists already\n'
                )
    except ValueError as v_e:
        print(f'Username not valid: {v_e}')
        return False
    try:
        if not (isinstance(user, str) or isinstance(password, str)):
            raise TypeError(
                'Please enter information in string form\n'
            )
    except TypeError as t_e:
        print(f'Input not valid: {t_e}')
        return False
    else:
        print('You"re all signed up\n')
        return True
