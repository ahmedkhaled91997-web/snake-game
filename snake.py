from turtle import Turtle 
class Snake:
    def __init__(self):
        self.turtles=[]
        self.positions=((-40,0),(-20,0),(0,0))
        self.create_snake()
        self.head=self.turtles[-1]
    def create_snake(self):
        for i in range(3):
            new_turtle=Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(self.positions[i])
            self.turtles.append(new_turtle)
    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.turtles[-1].forward(20)
    def add_slice(self):
        new_turtle=Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        self.turtles.insert(0,new_turtle)
    def up(self):
        self.turtles[-1].setheading(90)
    def down(self):
        self.turtles[-1].setheading(270)
    def left(self):
        self.turtles[-1].setheading(180)
    def right(self):
        self.turtles[-1].setheading(0)


                