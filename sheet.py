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

