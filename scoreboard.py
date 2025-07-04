from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",20,"bold")
FONT_GAMEOVER=("Courier",30,"bold")
FONT_POINT = ("Courier", 20, "bold")


# '''The issue is with how Python interprets backslashes (\) in strings. For example:

# \U starts a Unicode escape sequence like \U0001F600 (emoji).

# So Python tries to parse \Users\... as a Unicode, which causes the error.


# Fix Options
# 🔹 Option 1: Use raw string
# python
# Copy code
# with open(r"C:\Users\desha\OneDrive\Desktop\MYCODE\Python\projects python\snake_game\data.txt
# '''

# Adding a high Score Function to keep track the High Score
# 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open(r"C:\Users\desha\OneDrive\Desktop\MYCODE\Python\projects python\snake_game\Snake-Game-using-OOPS\data.txt") as data:
            self.high_score=int(data.read())
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()  #for hiding the turtle which write the score
        self.update_scoreboard() #show that at starting the score is Zero

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}",align=ALIGNMENT,font=FONT)


    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open(r"C:\Users\desha\OneDrive\Desktop\MYCODE\Python\projects python\snake_game\Snake-Game-using-OOPS\data.txt",mode='w') as data:
                data.write(f"{self.high_score}")
        # then update the socreboard
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
    def game_over(self):
        self.clear()  #clear the score board when game is over
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_GAMEOVER)
        self.goto(0,-20) #change in this line
        self.write(f"Your Score is {self.score}", align=ALIGNMENT, font=FONT_POINT)
        self.goto(0,-40) #change in this line
        self.write(f"High Score is {self.high_score}", align=ALIGNMENT, font=FONT_POINT)
        self.score = 0


         