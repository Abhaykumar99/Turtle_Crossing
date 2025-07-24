import turtle
import random
import time

screen = turtle.Screen()
screen.title("Day 23 – Turtle Crossing")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SPAWN_CHANCE = 6


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move_up(self):
        self.sety(self.ycor() + 10)

    def at_finish_line(self):
        return self.ycor() > 280

    def reset_position(self):
        self.goto(0, -280)


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, CAR_SPAWN_CHANCE) == 1:
            car = turtle.Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            y = random.randrange(-250, 250, 20)
            car.goto(300, y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT

    def hit(self, player):
        return any(car.distance(player) < 40 for car in self.cars)


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", font=("Arial", 16, "normal"))

    def next_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 30, "bold"))


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if car_manager.hit(player):
        scoreboard.game_over()
        game_on = False

    if player.at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.next_level()

screen.exitonclick()

