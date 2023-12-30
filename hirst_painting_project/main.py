import colorgram

# I used this to have the program look at the painting, then pull the colors RGB values and add them to a list called rgb_colors
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
from turtle import Turtle, Screen
import turtle
import random
# Creates a turtle object
timmy = Turtle()
# This lets us set the colormode to accept RBG tuples AND strings to set colors
turtle.colormode(255)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
# Pulls the turtle's pen up so it doesn't ink while getting to the defined starting point
timmy.penup()
# Makes the turtle go super fast so I don't have to wait to see if I did it right
timmy.speed("fastest")

# Function that draws a dotted line, with dots instead of dashes. 
# Sends Timmy to the bottom left of the screen, draws a dot in a random color, goes pen up, then moves him in increments of 50 pixels
def draw_dot_line():
    y_coordinate = -200
    timmy.setpos(-200, y_coordinate)
    for h in range(10):
        timmy.setpos(-200, y_coordinate)
        y_coordinate += 50
        for i in range(10):
            timmy.color(random.choice(color_list))
            timmy.dot(20)
            timmy.penup()
            timmy.forward(50)

# Calls the function that draws a dotted line
draw_dot_line()
# Hides the turtle
timmy.hideturtle()
# Creates the screen object
screen = Screen()
# Keeps the screen open until we click, so I can see the beautiful artwork
screen.exitonclick()
