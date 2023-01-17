""" Import Section """
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

data = easy.get_all_values()

print(data)


def clear():
    """
    # Clear the screen for the player
    """
    os.system('clear')


def display_snake_title():
    """
    Title Page Display
    """
    title = pyfiglet.figlet_format(
        "SpeedSnake", font="slant", justify="center")
    print(title)

    subtitle = pyfiglet.figlet_format(
        "Play Snake", font="standard", justify="center")
    print(subtitle)

    print(Fore.RED + "Developed by Barry Ferguson".center(60) + "\n")