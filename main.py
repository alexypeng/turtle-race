from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour.").lower()
colours = ["red", "orange", "yellow", "green", "blue", "violet"]
positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.up()
    new_turtle.goto(x=-225, y=positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 230:
            winner = turtle
            is_race_on = False


if winner.pencolor() == user_bet:
    print(f"You've won! The winner is the {winner.pencolor()} turtle.")
else:
    print(f"You've lost! The winner is the {winner.pencolor()} turtle.")

screen.exitonclick()