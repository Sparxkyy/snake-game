from turtle import Turtle

ALIGNMENT="center"
FONT=("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data_file.txt") as data:
            self.high_score=int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()
        self.hideturtle()
        #to hide arrow we use hideturtle and use write function to display the score title on top

    def update_score(self):
        self.clear()
        self.write(f"Score={self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score> self.high_score:
            self.high_score=self.score
            with open("data_file.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()
    def increase_score(self):
        self.score+=1

        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"game over, your score:{self.score}", align="center", font=18)



