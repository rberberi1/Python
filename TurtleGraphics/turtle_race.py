from turtle import Turtle, Screen
import random

is_race_on=False

screen=Screen()
screen.setup(width=500, height=400)
user_bet= screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors=["red", "orange", "yellow", "green", "blue", "purple"]
y_positions=[-70, -40, -10, 20, 50, 80]
all_turtles=[]

for turtle_index in range(0,6):
  t1=Turtle(shape="turtle")
  t1.color(colors[turtle_index])
  t1.penup()
  t1.goto(x=-230, y=y_positions[turtle_index])
  all_turtles.append(t1)

if user_bet:
  is_race_on=True  

while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor()>230:
      is_race_on=False
      winner=turtle.pencolor()
      if winner == user_bet:
        print(f"You won! The {winner} turtle is the winner!")
      else:
        print(f"You lost! The {winner} turtle is the winner!")  
    distance=random.randint(0,10)
    turtle.forward(distance)


screen.exitonclick()