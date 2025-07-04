from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0



class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            

    def add_segment(self,position):
        # adding segment
        new_segment=Turtle('circle')
        new_segment.color("red")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        # add a new segment to the snake
        # segment will add at the tail ..so -1
        self.add_segment(self.segments[-1].position())
        # position is a method of turtle class

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            # Start from the last segment (len(segments) - 1)
            # Go down to 1 (not including 0)
            # Step backwards (-1)
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

    # Move the head forward
        self.head.forward(MOVE_DISTANCE)
    



    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)