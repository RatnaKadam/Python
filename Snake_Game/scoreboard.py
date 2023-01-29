from turtle import Turtle

FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.color("white")
        self.write(arg=f"Score:{self.score} ", align="center", font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score:{self.score} ", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
