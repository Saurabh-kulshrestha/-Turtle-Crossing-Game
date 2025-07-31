# Required modules import
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)  # Set the screen size
screen.tracer(0)  # Turn off automatic screen updates for manual control

# Create game objects
player = Player()  # Player turtle object
car_manager = CarManager()  # Manages car creation and movement
scoreboard = Scoreboard()  # Displays score (level) and game over message

# Set up keyboard controls
screen.listen()  # Start listening for key presses
screen.onkey(player.go_up, "w")  # Move the player up on pressing 'w'

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Control game speed
    screen.update()  # Refresh the screen

    car_manager.create_cars()  # Randomly generate cars
    car_manager.move_cars()  # Move all cars on screen

    # Detect collision between player and any car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # If too close to a car
            scoreboard.game_over()  # Show game over message
            game_is_on = False  # Stop the game

    # Detect if player has reached the finish line
    if player.is_at_finish_line():
        player.go_to_start()  # Reset player's position
        car_manager.level_up()  # Increase car speed
        scoreboard.level_up()  # Increase level and update score display

# Close the screen when clicked
screen.exitonclick()
