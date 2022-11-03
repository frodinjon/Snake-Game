from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.title("My Snake game")
screen.screensize(600, 600)
screen.tracer(0)

snake1 = Snake()
food1 = Food()
scoreboard = Scoreboard()

game_on = True


screen.onkey(fun=snake1.up, key="Up")
screen.onkey(fun=snake1.down, key="Down")
screen.onkey(fun=snake1.left, key="Left")
screen.onkey(fun=snake1.right, key="Right")

screen.listen()


while game_on:
	screen.update()
	time.sleep(0.4)
	snake1.move()

	#detect collision with food
	if snake1.head.distance(food1) < 15:
		food1.refresh()
		snake1.extend()
		print("nom nom nom")
		scoreboard.increase_score()

	#detect collision with wall
	if snake1.head.xcor() > 280 or snake1.head.xcor() < -280 or snake1.head.ycor() > 280 or snake1.head.ycor() < -280:
		game_on = False
		scoreboard.game_over()

	#detect collision with tail
	#if head collides with any tail segment - trigger game over
	for segment in snake1.snake_body[1:]:
		if snake1.head.distance(segment) < 10:
			game_on = False
			scoreboard.game_over()
			
screen.exitonclick()