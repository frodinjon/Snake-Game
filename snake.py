from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

starting_positions = [(0,0), (-20, 0), (-40, 0)]

class Snake:
	def __init__(self):
		self.snake_body = []
		self.create_snake()
		self.head = self.snake_body[0]


	def create_snake(self):
		for i in starting_positions:
			self.add_segment(i)
			

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)	

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)
		

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)
		

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

	
	def move(self):
		for i in range(len(self.snake_body) - 1, 0, -1):
			self.snake_body[i].goto(self.snake_body[i-1].xcor(), self.snake_body[i-1].ycor())
		#self.snake_body[0].setheading(heading)
		self.head.fd(MOVE_DISTANCE)

	def extend(self):
		#add a segment to the snake
		self.add_segment(self.snake_body[-1].position())

	def add_segment(self, position):
		snake = Turtle('square')
		snake.color('white')
		snake.penup()
		snake.goto(position)
		self.snake_body.append(snake)


	def reset(self):
		for segment in self.snake_body:
			segment.hideturtle()
		self.snake_body.clear()
		self.create_snake()
		self.head = self.snake_body[0]