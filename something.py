import turtle

# Setting up screening 
screen = turtle.Screen()
screen.title("Simple Paper.io Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)  

#  Defining Player attributes
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0, 0)

# Setting up the trail attributes
trail_color = "lightblue"
player.pensize(3)
trail_pen_down = True  # Start drawing the trail immediately

# setting up speed 
player_speed = 0.1
captured_area = 0

# Directions
direction = "stop"

# Functions to change direction based on arrow key input
def go_up():
    global direction
    # Prevent reversing directly into the opposite direction
    if direction != "down":
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

# Move the turtle based on the current direction
def move():
    global trail_pen_down, captured_area

    if trail_pen_down:
        player.pendown()  # Enable drawing trail
        player.pencolor(trail_color)  # Set trail color
    else:
        player.penup()  # Stop drawing trail

    if direction == "up":
        y = player.ycor()
        player.sety(y + player_speed)
    elif direction == "down":
        y = player.ycor()
        player.sety(y - player_speed)
    elif direction == "left":
        x = player.xcor()
        player.setx(x - player_speed)
    elif direction == "right":
        x = player.xcor()
        player.setx(x + player_speed)

    # Check for collision with edges
    if abs(player.xcor()) > 290 or abs(player.ycor()) > 290:
        end_game("Hit the wall!")

# End the game
def end_game(reason):
    player.hideturtle()
    screen.update()
    print(f"Game Over! {reason}")
    turtle.done()

# Key bindings to control direction with arrow keys
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Main game loop
while True:
    screen.update()
    move()
    turtle.delay(100)  # Control the speed

# Exit on close
turtle.mainloop()
