from turtle import Turtle
import random
"""make inherit class of turtle so that the 
food class will have all the mmethods of the turtle"""

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")  #so new piece of food has circle shape
        self.penup()
        self.shapesize(stretch_len=0.8,stretch_wid=0.8)
        # stretch_len or wid=0.8 means 0.8*20px
        self.color("black")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        # fastest move from 1 location to another location
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.goto(random_x,random_y)


