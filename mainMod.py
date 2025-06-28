# steps of snake game 
# 1.create a snake
# 2.move the snake
# 3.control the snake
# 4.Detect collision with food
# 5.create a scoreboard
# 6.detect collision with wall
# 7.detect collision with tail


# Now we will attach a file to keep track the High score

from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
from wall import Wall
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.bgpic('jungle.gif')
screen.title("The Snake game")
screen.tracer(0)




difficulty=screen.textinput(title="Choose Difficulty",prompt="easy/medium/hard").lower()




if difficulty=="easy":
    speed=0.15
    wall_count=3
elif difficulty=="medium":
    speed=0.1
    wall_count=5
elif difficulty=="hard":
    speed=0.08
    wall_count=7
else:
    speed=0.1
    wall_count=3



# data.txt file will keep track the Hihg score

snake=Snake()
food=Food()
scoreboard=Scoreboard()
wall=Wall(wall_count=wall_count)





# Set focus on TurtleScreen (in order to collect key-events).
# Dummy arguments are provided in order to be able to pass
# listen() to the onclick method.
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# when the 3 snake block moves together then the screen will be update
# delay of 0.1 sec after 3 block together moving forward
# screen.tracer(0) turns off automatic updates, so you can manually control when the screen refreshes (with screen.update()).
# The tail segment moves to where the second-last one was, and so on until the head, which moves forward.


# adding the pause and resume function
is_pause=False

def toggle_pause():
    global is_pause
    is_pause=not is_pause  #is_pause=True

screen.onkey(toggle_pause, "space")




game_is_on=True


# gaming loop
while game_is_on:
    screen.update()
    time.sleep(speed)


    if not is_pause:
        # Move the segments from tail to head
        snake.move()

        # screen

        # Detect Collision between Food and Snake

        #distance method is used here..This method return the distance from the 
        #turtle to(x,y), the given vector or the given othrt turtle 

        if snake.head.distance(food)<15:
            # refresh
            food.refresh()
            # extend
            snake.extend()
            scoreboard.increase_score()

        # Detect Collision between snake and Wall boundary


        # Since you're using screen.tracer(0) (manual screen updates),
        # you must call screen.update() after hiding the food.

        if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
            game_is_on=False  # game stop

            # food disappear and screen update
            food.hideturtle()
            screen.update()
            scoreboard.reset()


        # Detect collision with tail
        # for segment in snake.segments:
            # bypass the snake head because one of the segment
            # is the head itself so game will over in first iteration

            
            # if segment==snake.head:
            #     pass
            # use slicing
        for segment in snake.segments[1:]:
            if snake.head.distance(segment)<18:
                game_is_on=False
                food.hideturtle()
                screen.update()
                scoreboard.reset()

        # if the head collides with any segment in the tail
        # trigger game over

        # detect collision with middle wall
        for segment in wall.segments:
            if snake.head.distance(segment) < 17:
                game_is_on = False
                food.hideturtle()
                screen.update()
                scoreboard.reset()





    
    
        
screen.exitonclick()