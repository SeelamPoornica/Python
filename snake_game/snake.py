import turtle as t
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_seg = t.Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position[0], position[1])
        self.segment.append(new_seg)

    def extend(self):
        position = self.segment[-1].position()
        self.add_segment(position)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
