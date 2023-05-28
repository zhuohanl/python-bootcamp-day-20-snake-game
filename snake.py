from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self, head_images):
        self.segments = []

        self.head_images = head_images

        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        self.add_head(STARTING_POSITIONS[0])
        for position in STARTING_POSITIONS[1:]:
            self.add_segment(position)

    def add_head(self, position):
        new_segment = Turtle(self.head_images['right'])

        new_segment.penup()
        new_segment.goto(position)

        self.segments.append(new_segment)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("#21ff4f")

        new_segment.penup()
        new_segment.goto(position)

        self.segments.append(new_segment)

    def extend(self):
        # Add this segment to the same position as the last segment
        self.add_segment(self.segments[-1].position())

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            # find the x,y of the in-front segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # place the current segment to there
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if int(self.head.heading()) != DOWN:
            self.head.shape(self.head_images['up'])
            self.head.setheading(UP)

    def down(self):
        if int(self.head.heading()) != UP:
            self.head.shape(self.head_images['down'])
            self.head.setheading(DOWN)

    def left(self):
        if int(self.head.heading()) != RIGHT:
            self.head.shape(self.head_images['left'])
            self.head.setheading(LEFT)

    def right(self):
        if int(self.head.heading()) != LEFT:
            self.head.shape(self.head_images['right'])
            self.head.setheading(RIGHT)
