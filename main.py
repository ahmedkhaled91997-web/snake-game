from turtle import Screen, Turtle
from food import Food
from snake  import Snake
from score import Score
import time


window=Screen()
window.setup(width=600,height=600)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)


food=Food()
snake=Snake()
score=Score()


game_is_on=True
while game_is_on:
    snake.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(snake.up,"Up")
    window.onkey(snake.down,"Down")
    window.onkey(snake.left,"Left")
    window.onkey(snake.right,"Right")
    if snake.head.distance(food)<15:
        food.refresh_position()
        snake.add_slice()
        score.update_score()
    if snake.head.xcor()>270 or snake.head.xcor()<-270 or snake.head.ycor()>270 or snake.head.ycor()<-270 :
        game_is_on=False
        window.bgcolor("red")    
        score.game_over()
    for _ in snake.turtles[:-1]:
        if snake.head.distance(_)<10:
            game_is_on=False
            window.bgcolor("red")
            score.game_over()
    
        



    



window.exitonclick()