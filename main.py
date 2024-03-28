import colorgram
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.hideturtle()
screen = Screen()
screen.colormode(255)
colors_extract = colorgram.extract('hirst.jpg', 70)
rgb_extract = []
for color in range(len(colors_extract)):
    rgb = colors_extract[color - 1].rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    rgb_temp = (red, green, blue)
    rgb_extract.append(rgb_temp)
y = -200
for i in range(10):
    tim.teleport(-50, y)
    for r in range(10):
        dot_color = random.choice(rgb_extract)
        tim.speed(0)
        tim.penup()
        tim.dot(20, dot_color)
        tim.forward(50)
    y += 50







screen.exitonclick()