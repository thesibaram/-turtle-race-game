# turtle_race/countdown.py
from turtle import Turtle
import time

def start_countdown():
    announcer = Turtle()
    announcer.hideturtle()
    for count in ["Ready 🏁", "Set 🔥", "Go! 🚀"]:
        announcer.clear()
        announcer.write(count, align="center", font=("Arial", 30, "bold"))
        time.sleep(1)
    announcer.clear()
