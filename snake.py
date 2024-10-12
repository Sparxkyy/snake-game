STARTING_POSITION=[(0,0), (-20,0), (-40,0)]

from turtle import Turtle

MOVE_DISTANCE=20
up=90
down=270
right=0
left=180

#is class me fo function bnaye first jo snake  create krta h with the help of two blocks
#and next function wo h jo snake ko move krta forward ye dono hi functions isliye bnaye taaki
#code small ho ske or isme class or init functin ka bhi revision ho gya. move function ek baar or ache se dekhna pdega
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]
#ye samaj nhi aya
    def move(self):
        for seg_num in range(len( self.segments) - 1, 0, -1):
            new_x =  self.segments[seg_num - 1].xcor()
            new_y =  self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)
    def add_segment(self,position):

        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)


    def extend(self):
        #add a new segment to snake
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)