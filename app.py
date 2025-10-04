import turtle as t
import time
import random

delay = 0.1
score = 0
high_score = 0

# Set up the screen
screen = t.Screen()
screen.title("Snake Game")
screen.bgcolor("blue")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = t.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = t.Turtle()
food.speed(0)
food.shape(random.choice(['square', 'triangle', 'circle']))
food.color(random.choice(['red', 'green', 'black']))
food.penup()
food.goto(0, 100)

segments = []

# Score display
pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center", font=("candara", 24, "bold"))

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main game loop
while True:
    screen.update()
    
    # Check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("candara", 24, "bold"))

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add a segment
        new_segment = t.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("candara", 24, "bold"))

    # Move the end segments first
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    # Move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("candara", 24, "bold"))

    time.sleep(delay)

screen.mainloop()
