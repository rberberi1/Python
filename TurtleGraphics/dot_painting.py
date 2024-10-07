# import colorgram

# rgb_colors=[]
# colors=colorgram.extract('TurtleGraphics/image.jpg', 30)
# for color in colors:
#   r=color.rgb.r
#   g=color.rgb.g
#   b=color.rgb.b
#   new_color=(r, g, b)
#   rgb_colors.append(new_color)

# print(rgb_colors)  
import turtle as t
import random

t.colormode(255)
turtle=t.Turtle()
turtle.speed('fastest')
turtle.penup()
turtle.hideturtle()

color_list= [(203, 165, 108), (152, 74, 48), (52, 93, 124), (170, 153, 41), (223, 202, 136), (137, 32, 21), (132, 163, 185), (47, 121, 88), (198, 91, 72), (15, 99, 73), (70, 47, 39), (147, 179, 148), (98, 73, 75), (162, 142, 157), (234, 175, 164), (55, 46, 49), (184, 205, 172), (24, 81, 87), (38, 61, 74), (142, 22, 25), (85, 146, 126), (45, 65, 85), (175, 91, 94), (214, 177, 183), (18, 70, 64), (109, 125, 151)]

turtle.setheading(210)
turtle.forward(400)
turtle.setheading(0)
num_dots=100

for dot_count in range(1, num_dots + 1):
  turtle.dot(20, random.choice(color_list))
  turtle.forward(50)

  if dot_count % 10 ==0:
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)




screen=t.Screen()
screen.exitonclick()