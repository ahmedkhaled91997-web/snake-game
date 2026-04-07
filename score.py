from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score=self.get_high_score()
        self.score=0
        self.penup()
        self.hideturtle()
        self.color("cyan")
        self.goto(0,260)
        self.update_score()

    def get_high_score(self):
        with open("high_score.txt","r") as file:
            return int(file.read())

    def save_high_score(self):
        with open("high_score.txt","w") as file:
            if self.score>self.high_score:
                self.high_score=self.score
                self.save_high_score()
                file.write(str(self.high_score))
            else:
                file.write(str(self.high_score))
            

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score:{self.high_score-1} ",align="center",font=("Arial",16,"normal"))  
        self.score+=1
    def game_over(self):
        self.save_high_score()
        self.goto(0,50)
        self.write("________GAME OVER________",align="center",font=("Arial",24,"normal"))
        self.goto(-20,-30)
        self.write(f"Final Score:{self.score-1}\n\nHigh Score:{self.high_score-1} ",align="center",font=("Arial",16,"normal"))

        
