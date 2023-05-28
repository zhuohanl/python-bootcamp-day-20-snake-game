from turtle import Turtle

HEADER = (0, 270)
CENTRE = (0, 0)
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(HEADER)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(CENTRE)
        self.write(arg="Game Over.", align=ALIGNMENT, font=FONT)
