import pandas
import turtle

# screen setting
my_screen = turtle.Screen()
my_screen.bgpic("India_map.gif")
user_name = my_screen.textinput(title="Guess the State", prompt="Enter the state name: ")
score = 0

# read data from CSV
data = pandas.read_csv("Indian_states.csv")
state_names = data.state.to_list()

# List of guessed names
guessed_list = []

# check if user's answer is in the state list
while score < 38:
    if user_name in state_names:
        guessed_list.append(user_name)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == user_name]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(arg=user_name)
        score = score+1
        user_name = my_screen.textinput(title=f"{score}/39", prompt="Enter the state name: ")

    elif user_name == "Exit":
        break
    else:
        user_name = my_screen.textinput(title=f"{score}/39", prompt="Enter the state name: ")
my_screen.mainloop()

# creating a remaining names list
remaining_list = []
for name in state_names:
    if name not in guessed_list:
        remaining_list.append(name)

# Creating a Dataframe of remaining list
df = pandas.DataFrame(remaining_list)

# Converting Dataframe to CSV file
df.to_csv("Remaining_state_names.csv")
