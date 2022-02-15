from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.setposition(0, 260)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", False, align= ALIGN, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
