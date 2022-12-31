from turtle import Turtle

FONT = ('Courier', 8, 'normal')
ALIGNMENT = 'center'


class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, answer, x_column, y_column):
        self.goto(x_column, y_column)
        self.write(f"{answer}", False, align=ALIGNMENT, font=FONT)
