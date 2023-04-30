from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.write("Level: 1", False, "center", FONT)
        self.level = 1

    def next_level(self):
        self.write(f"Level: {self.level}", False, "center", FONT)
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", False, "center", FONT)
