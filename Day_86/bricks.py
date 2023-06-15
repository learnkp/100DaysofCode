import random
from turtle import Turtle

COLORS = ["#22A699", "#F29727", "#F24C3D", "#F2BE22", "#17594A",
          "#E966A0", "#9AC5F4", "#090580", "#606C5D"]


class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.all_bricks = []
        self.hideturtle()

    def create_bricks(self):
        y = 100
        for i in range(5):
            x = -265
            y += 25
            while x < 300:
                brick = Turtle("square")
                brick.penup()
                brick.shapesize(stretch_len=3, stretch_wid=1)
                brick.color(random.choice(COLORS))
                brick.goto(x, y)
                self.all_bricks.append(brick)
                x += 65

    def win(self):
        if len(self.all_bricks) == 0:
            self.goto(0, 0)
            self.write("YOU WON", align="center", font=("Courier", 30, "bold"))