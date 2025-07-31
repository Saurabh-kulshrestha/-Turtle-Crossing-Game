from random import randint
from turtle import Turtle
import random

# List of possible colors for the cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Starting speed of cars
STARTING_MOVE_DISTANCE = 5

# How much faster cars get each level
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        # List to hold all car objects
        self.all_cars = []
        # Initial speed of the cars
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        # Only create a car occasionally (1 in 6 chance) to avoid too many at once
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")  # Create a new car as a square turtle
            new_car.shapesize(stretch_len=2, stretch_wid=1)  # Make it longer to look like a car
            new_car.penup()  # Prevent drawing lines
            new_car.color(random.choice(COLORS))  # Set a random color
            random_y = random.randint(-250, 250)  # Choose a random vertical position
            new_car.goto(300, random_y)  # Start from the right edge of the screen
            self.all_cars.append(new_car)  # Add car to the list

    def move_cars(self):
        # Move each car to the left by the current car speed
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        # Increase the speed of the cars for the next level
        self.car_speed += MOVE_INCREMENT
