""" Import Section """
# import os to clear the terminal to play game again
import os

# import pyfiglet to display ascii title text
import pyfiglet

# import colorama to add colour
import colorama
from colorama import Fore
colorama.init(autoreset=True)

import gspread
from google.oauth2.service_account import Credentials


# Scope Code to call Google Drive
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('speed_snake_scores')

easy = SHEET.worksheet('easy')
medium = SHEET.worksheet('medium')
hard = SHEET.worksheet('hard')

# data = easy.get_all_values()

def clear():
    """
    Clear the screen for the player
    """
    os.system('clear')

def display_snake_title