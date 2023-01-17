# import random module
import random

#import curses module
import curses

import time

# import pyfiglet to display ascii title text
import pyfiglet

# import colorama to add colour
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# set up screen
setup = curses.initscr()
h, w = setup.getmaxyx()
win = curses.newwin(h, w, 0, 0)

win.keypad(1)
curses.curs_set(0)

#Set Snake and Food Start positions
snake_head = [10,10]
food_position = [15,15]
score = 0

print(snake_head)
print(food_position)
print(score)