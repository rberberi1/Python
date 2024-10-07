import turtle
import pandas  

screen=turtle.Screen()
screen.title("U.S States Game")
image="CSV/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data= pandas.read_csv("CSV/50_states.csv")
all_states= data.state.to_list()
guessed_states=[]

while len(guessed_states) < 50:
  answer= screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

  if answer == "Exit":
    missing_states=[]
    for state in all_states:
      if state not in guessed_states:
        missing_states.append(state)
    new_data=pandas.DataFrame(missing_states)    
    new_data.to_csv("CSV/states_to_learn.csv")
    break

  if answer in all_states:
    guessed_states.append(answer)
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data=data[data.state==answer]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(state_data.state.item())




screen.exitonclick()