from turtle import Turtle
import random

class Wall:
    def __init__(self, wall_count=2):
        self.segments = []
        self.create_random_walls(wall_count)

    def create_random_walls(self, count):
        for _ in range(count):
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            length = random.randint(2, 6)  
            # wall length between 2 to 6 segments
            orientation = random.choice(['vertical', 'horizontal'])
            self.create_wall_block(x, y, length, orientation)

    def create_wall_block(self, x, y, length, orientation='vertical'):
        for i in range(length):
            wall_segment = Turtle("square")
            wall_segment.color("orange")
            wall_segment.penup()
            if orientation == 'vertical':
                wall_segment.goto(x, y + i * 20)
            else:
                wall_segment.goto(x + i * 20, y)
            self.segments.append(wall_segment)
