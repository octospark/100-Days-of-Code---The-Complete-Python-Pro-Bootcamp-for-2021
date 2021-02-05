# import colorgram
#
# colors = colorgram.extract("hirst_dot_picture.jpg", 30)
# colors_tuples = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors_tuples.append((r, g, b))
import turtle, random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed(0)

color_list = [(231, 205, 85), (228, 148, 89),(120, 167, 186), (162, 11, 19), (31, 111, 160), (234, 81, 45),
              (175, 19, 14), (124, 177, 145), (5, 99, 36), (189, 186, 23), (207, 65, 23), (26, 131, 43),
              (10, 40, 76), (243, 202, 5), (14, 63, 40), (86, 14, 22), (135, 84, 99), (48, 167, 74),
              (4, 65, 140), (173, 134, 149), (39, 22, 19), (49, 150, 195), (228, 171, 161), (219, 63, 69),
              (73, 134, 188), (173, 204, 175)]

tim.hideturtle()
tim.penup()
tim.setpos(-200, -250)
tim.pendown()

for i in range(1, 11):
    for j in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.setpos(tim.xcor() - 500, tim.ycor() + 50)


screen = turtle.Screen()
screen.exitonclick()
