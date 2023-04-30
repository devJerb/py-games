from turtle import Turtle

FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()

        self.goto(x=0, y=280)

        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_score()
