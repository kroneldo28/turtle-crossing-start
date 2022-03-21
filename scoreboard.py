from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-290, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level {self.level}", move=False, align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(-60, 0)
        self.write("GAME OVER !", move=False, align="left", font=FONT)
