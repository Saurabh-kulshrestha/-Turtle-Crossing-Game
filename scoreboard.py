from turtle import Turtle

# Font style for scoreboard text
FONT = ("Courier", 24, "normal")

# Scoreboard class to display level and game over message
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()              # Inherit Turtle properties
        self.level = 0                  # Start from level 0
        self.penup()                    # Remove drawing line when turtle moves
        self.hideturtle()              # Hide the turtle icon
        self.update_score()            # Show the initial score

    # Function to update and display the current level
    def update_score(self):
        self.clear()                   # Clear previous text to avoid overlapping
        self.goto(-280, 260)           # Set position for score text
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Display level

    # Function to increment level and update scoreboard
    def level_up(self):
        self.level += 1                # Increase level by 1
        self.update_score()            # Refresh the scoreboard

    # Function to display game over message
    def game_over(self):
        self.goto(-80, 0)              # Set position for game over message
        self.write("Game Over!", font=FONT)  # Display message
