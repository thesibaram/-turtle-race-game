# turtle_race/screen_setup.py

from turtle import Screen
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS

def create_screen():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Turtle Race")
    return screen

def get_user_bet(screen):
    user_bet = screen.textinput(
        title="Make your bet",
        prompt=f"Which turtle will win? Enter a color ({', '.join(COLORS)}): "
    )
    while user_bet is None or user_bet.lower() not in COLORS:
        user_bet = screen.textinput(
            title="Invalid bet!",
            prompt=f"Please enter a valid color ({', '.join(COLORS)}): "
        )
    return user_bet.lower()
