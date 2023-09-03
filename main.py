from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
beginning_x = -230
beginning_y = -60

if user_bet:
    is_race_on = True

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=beginning_x, y=beginning_y)
    beginning_y += 25

while is_race_on:
    for turtle in screen.turtles():
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


if winner == user_bet:
    print(f"You've won! The {winner} turtle is the winner! ")
else:
    print(f"You've lost! The {winner} turtle is the winner! ")

screen.exitonclick()