import random
from turtle import Turtle, Screen
from tkinter import messagebox

FONT = ("Times New Roman", 20, 'bold')
X_POSITION = -480
Y_POSITION = [240, 160, 80, 0, -80, -160, -240]


# screen settings
my_screen = Screen()
my_screen.screensize(canvwidth=600, canvheight=400)
my_screen.title("The Turtle Racing Game")
my_screen.bgcolor("forestgreen")
answer = my_screen.textinput(title="The Turtle Racing Game",
                             prompt="Which turtle will you bet on?(red,yellow,purple,pink,blue,orange,brown)").lower()

# Draw Start Line
start_line = Turtle()
start_line.penup()
start_line.goto(x=-400, y=300)
start_line.right(90)
while start_line.ycor() != -300:
    start_line.pensize(11)
    start_line.pendown()
    start_line.forward(10)
    start_line.hideturtle()

# Write Start word
start = Turtle()
start.penup()
start.goto(x=-455, y=320)
start.write(arg="Start Line", font=FONT)
start.hideturtle()

# Write Finish word
finish = Turtle()
finish.penup()
finish.goto(x=320, y=320)
finish.write(arg="Finish Line", font=FONT)
finish.hideturtle()

# Draw Finish Line
finish_line = Turtle()
finish_line.penup()
finish_line.goto(x=400, y=300)
finish_line.right(90)
while finish_line.ycor() != -300:
    finish_line.pensize(width=11)
    finish_line.pendown()
    finish_line.forward(10)
    finish_line.hideturtle()


colour_list = ["red", "yellow", "purple", "pink", "blue", "orange", "brown", ]
tim_list = []

# create turtles for race
for item in range(0, 7):
    tim = Turtle()
    tim.penup()
    tim.shape("turtle")
    chose_color = colour_list[item]
    tim.color(chose_color)
    y_cor = Y_POSITION[item]
    tim.goto(X_POSITION, y_cor)
    tim.pendown()
    tim_list.append(tim)

# move turtles
game_is_on = True
while game_is_on:
    for tim in tim_list:
        if tim.xcor() > 550:
            game_is_on = False
            winning_color = tim.pencolor()
            # check if user's bet is same as that of winner or not
            if winning_color == answer:
                messagebox.showinfo(title="Result", message=f"Congratulations!!!\nThe winner is {winning_color} turtle.")
            else:
                messagebox.showinfo(title="Result", message=f"You loose!!!\nThe winner is {winning_color} turtle.")
    # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        tim.penup()
        tim.forward(rand_distance)

my_screen.exitonclick()
