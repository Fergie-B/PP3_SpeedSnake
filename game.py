# import random module
import random

#import curses module
import curses

# import pyfiglet to display ascii title text
import pyfiglet

# import colorama to add colour
import colorama
from colorama import Fore
colorama.init(autoreset=True)

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