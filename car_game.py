import turtle
import time
import random

win = turtle.Screen()
win.title("Car Racing Game")
win.bgcolor("gray")
win.setup(width=600, height=800)
win.tracer(0)

line = turtle.Turtle()
line.speed(0)
line.color("white")
line.penup()
line.goto(-200, 400)
line.pendown()
line.goto(-200, -400)
line.penup()
line.goto(200, 400)
line.pendown()
line.goto(200, -400)
line.hideturtle()

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("blue")
player.shapesize(stretch_wid=2, stretch_len=1)
player.penup()
player.goto(0, -300)

obstacle = turtle.Turtle()
obstacle.speed(0)
obstacle.shape("square")
obstacle.color("red")
obstacle.shapesize(stretch_wid=2, stretch_len=1)
obstacle.penup()
obstacle.goto(random.randint(-150, 150), 300)

score = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 350)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

def move_left():
    x = player.xcor()
    if x > -180:  
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 180: 
        player.setx(x + 20)

win.listen()
win.onkey(move_left, "Left")
win.onkey(move_right, "Right")

game_over = False
obstacle_speed = 10

while not game_over:
    win.update()

    obstacle.sety(obstacle.ycor() - obstacle_speed)

    if obstacle.ycor() < -400:
        obstacle.goto(random.randint(-150, 150), 300)
        score += 1
        obstacle_speed += 0.5 
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    if player.distance(obstacle) < 30:
        score_display.clear()
        score_display.goto(0, 0)
        score_display.write("GAME OVER!", align="center", font=("Courier", 36, "bold"))
        game_over = True

    time.sleep(0.02)

win.mainloop()
