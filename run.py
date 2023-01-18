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

scorelog = SHEET.worksheet('scorelog')

data = scorelog.get_all_values()

print(data)

# import random module
import random

# import curses module
import curses

import time


# set up screen
setup = curses.initscr()
h, w = setup.getmaxyx()
win = curses.newwin(h, w, 0, 0)

win.keypad(1)
curses.curs_set(0)


# Set Snake and Food Start positions
snake_head = [10,15]
body_position = [[15,10],[14,10],[13,10]]
food_position = [20,20]
score = 0 

# Show the Food on screen
win.addch(food_position[0], food_position[1], curses.ACS_BULLET)
print(food_position)

prev_button_direction = 1
button_direction = 1
key = curses.KEY_RIGHT

# Set up conditions to end game 
def hit_wall(snake_head):
    """
    If statement if snake head collides with a boundary wall
    """
    if snake_head[0]>=h-1 or snake_head[0]<=0 or snake_head[1]>=w-1 or snake_head[1]<=0 :
        return 1
    else:
        return 0

def hit_self(body_position):
    snake_head = body_position[0]
    if snake_head in body_position[1:]:
        return 1
    else:
        return 0