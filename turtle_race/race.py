# turtle_race/race.py

from turtle import Turtle
import random
from .constants import FINISH_LINE_X

def start_race(turtles, user_bet):
    announcer = Turtle()
    announcer.hideturtle()

    is_race_on = True
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > FINISH_LINE_X:
                is_race_on = False
                winner = turtle.pencolor()
                result_message = f"The {winner} turtle won!"
                if winner == user_bet:
                    result_message = f"🎉 Congratulations! {result_message}"
                else:
                    result_message = f"😢 You lost. {result_message}"
                announcer.write(result_message, align="center", font=("Arial", 20, "bold"))
                break
            random_distance = random.randint(1, 10)
            turtle.forward(random_distance)
