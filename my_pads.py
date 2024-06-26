from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid= 5, stretch_len= 0.8)

        self.goto(x, y)

    def up(self):
        if self.ycor() < 240:

            new_yPos = self.ycor() + 50
            self.goto(self.xcor(), new_yPos)
    def down(self):
        if self.ycor() > -240:
            new_yPos = self.ycor() - 50
            self.goto(self.xcor(), new_yPos)





