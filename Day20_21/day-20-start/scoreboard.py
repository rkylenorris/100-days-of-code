from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def get_high_score(self):
        with open('data.txt', 'r') as f:
            self.high_score = int(f.read())

    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('data.txt', 'w') as f:
            f.write(str(self.high_score))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

