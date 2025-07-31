from turtle import Turtle

# Constants for player settings
STARTING_POSITION = (0, -280)  # Starting point near the bottom of the screen
MOVE_DISTANCE = 10            # Distance the player moves each time
FINISH_LINE_Y = 280           # Y-coordinate where the finish line is located


# Player class inherits from Turtle
class Player(Turtle):

    def __init__(self):
        super().__init__()           # Initialize the Turtle superclass
        self.shape("turtle")         # Set the turtle shape
        self.setheading(90)          # Make the turtle face upward (90 degrees)
        self.penup()                 # Lift the pen so it doesn't draw lines
        self.go_to_start()           # Move the player to the starting position

    def go_up(self):
        # Move the turtle forward (upward by 10 units)
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        # Move the player back to the starting position
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        # Check if the player has crossed the finish line
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False  # You missed this return in your original code
