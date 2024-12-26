import turtle
import random  # Import random for generating random values

# Function to draw a filled circle
def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()

# Function to draw the snowman
def draw_snowman():
    # Bottom circle
    draw_circle(0, -200, 60, "white")
    # Middle circle
    draw_circle(0, -100, 40, "white")
    # Top circle (head)
    draw_circle(0, -40, 30, "white")
    # Eyes
    draw_circle(-10, -10, 5, "black")
    draw_circle(10, -10, 5, "black")
    # Nose (carrot)
    turtle.penup()
    turtle.goto(0, -20)
    turtle.color("orange")
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(0, -30)
    turtle.goto(15, -25)
    turtle.goto(0, -20)
    turtle.end_fill()
    # Mouth
    turtle.penup()
    turtle.goto(-15, -35)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.circle(20, 120)
    # Arms
    turtle.penup()
    turtle.goto(-40, -100)
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()
    turtle.goto(40, -100)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(50)

# Function to draw the Christmas tree
def draw_tree():
    # Tree trunk
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.color("brown")
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
    turtle.end_fill()
    # Tree layers
    turtle.color("green")
    layer_width = 100
    for y in range(-160, -40, 40):
        turtle.penup()
        turtle.goto(-210, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(-200 + layer_width, y - 40)
        turtle.goto(-190, y)
        turtle.goto(-210, y)
        turtle.end_fill()
        layer_width -= 20
    # Add ornaments
    for _ in range(8):
        turtle.penup()
        turtle.goto(-200 + random.randint(-30, 30), random.randint(-150, -50))
        turtle.dot(10, random.choice(["red", "yellow", "blue"]))

# Function to draw falling snow
def draw_snowflakes():
    for _ in range(50):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot(5, "white")

# Function to draw the entire scene
def draw_scene():
    turtle.speed(10)
    turtle.bgcolor("skyblue")  # Set background color
    draw_snowflakes()         # Draw snowflakes
    draw_tree()               # Draw Christmas tree
    draw_snowman()            # Draw snowman
    draw_circle(0, -250, 300, "white")  # Snowy ground

# Run the drawing
draw_scene()
turtle.done()
