from turtle import Turtle, Screen
import random
import time

# --- Constants for better readability and maintenance ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
FINISH_LINE_X = SCREEN_WIDTH / 2 - 50  # A little margin from the edge
START_LINE_X = -SCREEN_WIDTH / 2 + 20
COLORS = ["red", "green", "blue", "yellow", "purple"]

# --- Screen Setup ---
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle Race")

# --- User Input ---
user_bet = screen.textinput(title="Make your bet",
                            prompt=f"Which turtle will win? Enter a color ({', '.join(COLORS)}): ").lower()
while user_bet not in COLORS:
    user_bet = screen.textinput(title="Invalid bet!",
                                prompt=f"Please enter a valid color ({', '.join(COLORS)}): ").lower()

# --- Turtle Setup ---
turtles = []
y_positions = [-70, -40, -10, 20, 50]  # Adjusted y-coordinates for better spacing
for i, color in enumerate(COLORS):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=START_LINE_X, y=y_positions[i])
    turtles.append(new_turtle)

# --- Finish Line ---
finish_line = Turtle(visible=False) #hide the turtle and also prevent writing error
finish_line.penup()
finish_line.goto(FINISH_LINE_X, -SCREEN_HEIGHT / 2)  # Bottom of the screen
finish_line.setheading(90)  # Pointing up
finish_line.pendown()
finish_line.forward(SCREEN_HEIGHT) # Draw the line

finish_line.penup()
finish_line.goto(FINISH_LINE_X, SCREEN_HEIGHT/2 - 20) # Move to top of the finish line
finish_line.write("🏁", align="center", font=("Arial", 24, "bold")) # Write the flag

# --- Countdown ---
announcer = Turtle()
announcer.hideturtle()
for count in ["Ready 🏁", "Set 🔥", "Go! 🚀"]:
    announcer.clear()
    announcer.write(count, align="center", font=("Arial", 30, "bold"))
    screen.update()
    time.sleep(1)
announcer.clear()

# --- Race ---
is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > FINISH_LINE_X:
            is_race_on = False
            winner = turtle.pencolor()
            result_message = f"The {winner} turtle won!"
            if winner == user_bet:
                result_message = f"Congratulations! {result_message}"
            else:
                result_message = f"You lost. {result_message}"

            announcer.write(result_message, align="center", font=("Arial", 20, "bold"))
            break
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()
