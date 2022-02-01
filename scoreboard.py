from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("white")
        self.write(f"score: {self.score}", False , align = 'center', font=('Arial', 24, 'normal'))

    #def increase_score(self):