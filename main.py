from turtle_race.screen_setup import create_screen, get_user_bet
from turtle_race.turtle_setup import create_turtles, draw_finish_line
from turtle_race.countdown import start_countdown
from turtle_race.race import start_race

def main():
    screen = create_screen()
    user_bet = get_user_bet(screen)
    turtles = create_turtles()
    draw_finish_line()
    start_countdown()
    start_race(turtles, user_bet)
    screen.exitonclick()

if __name__ == "__main__":
    main()
