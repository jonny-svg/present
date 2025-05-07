import turtle

# Setup screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Presentation")

# Turtle setup
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)

page = 0

# Load custom images
screen.addshape("Mcdonalds.gif")
screen.addshape("chicken.gif")
screen.addshape("noodles.gif")
screen.addshape("game.gif")
screen.addshape("study.gif")
screen.addshape("movie.gif")
screen.addshape("track.gif")

# --- Pages ---

screen.bgcolor("lightblue")
t.clear()
t.goto(0, 200)
t.write("Welcome to My Presentation!", align="center", font=("Arial", 24, "bold"))
t.goto(0, 150)
t.write("This is all about my favorite things.", align="center", font=("Arial", 16, "normal"))
t.goto(0, -250)
t.write("Press Enter to go to the next page.", align="center", font=("Arial", 12, "italic"))

# Unique shape: Circle
t.goto(0, 0)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
round = input("Enter to continue: ")


screen.bgcolor("lightgreen")
t.clear()
t.goto(0, 200)
t.write("Favorite Foods", align="center", font=("Arial", 24, "bold"))
t.goto(0, 150)
t.write("I love noodles, chicken, and mcdonalds!", align="center", font=("Arial", 16, "normal"))
t.goto(0, -250)
t.write("Press Enter to go to the next page.", align="center", font=("Arial", 12, "italic"))

# Show food images
t.goto(-200, 0)
t.shape("noodles.gif")
t.stamp()

t.goto(0, 0)
t.shape("chicken.gif")
t.stamp()

t.goto(200, 0)
screen.addshape("mcdonalds.gif")
t.shape("mcdonalds.gif")
t.stamp()

# Unique shape: Square
t.shape("classic")
t.goto(0, -100)
t.setheading(0)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
for _ in range(4):
    t.forward(60)
    t.right(90)
t.end_fill()
t.penup()
round = input("Enter to continue: ")

screen.bgcolor("plum")
t.clear()
t.goto(0, 200)
t.write("My Hobbies", align="center", font=("Arial", 24, "bold"))
t.goto(0, 150)
t.write("I enjoy games, studying, going out, and playing!", align="center", font=("Arial", 16, "normal"))
t.goto(0, -250)
t.write("Press Enter to go to the next page.", align="center", font=("Arial", 12, "italic"))

# Show hobby images
t.goto(-150, 0)
t.shape("game.gif")
t.stamp()

t.goto(150, 0)
t.shape("study.gif")
t.stamp()

# Unique shape: Triangle
t.shape("classic")
t.goto(0, -100)
t.setheading(0)
t.pendown()
t.fillcolor("green")
t.begin_fill()
for _ in range(3):
    t.forward(80)
    t.left(120)
t.end_fill()
t.penup()
round = input("Enter to continue: ")

screen.bgcolor("lightyellow")
t.clear()
t.goto(0, 200)
t.write("Favorite Movie", align="center", font=("Arial", 24, "bold"))
t.goto(0, 150)
t.write("My favorite movie is 'The Pursuit of Happyness'.", align="center", font=("Arial", 16, "normal"))
t.goto(0, -250)
t.write("Press Enter to go to the next page.", align="center", font=("Arial", 12, "italic"))

t.pendown()
screen.addshape("movie.gif")
t.shape("movie.gif")
t.stamp()
t.shape("classic")

# Show movie image
t.goto(0, 0)
t.shape("movie.gif")
t.stamp()

# Unique shape: Pentagon
t.shape("classic")
t.goto(0, -100)
t.setheading(0)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
for _ in range(5):
    t.forward(50)
    t.left(72)
t.end_fill()
t.penup()
round = input("Enter to continue: ")

screen.bgcolor("skyblue")
t.clear()
t.goto(0, 200)
t.write("Favorite Sport", align="center", font=("Arial", 24, "bold"))
t.goto(0, 150)
t.write("I enjoy track and field!", align="center", font=("Arial", 16, "normal"))
t.goto(0, -250)
t.write("Thanks for watching!", align="center", font=("Arial", 12, "italic"))

# Show track image
t.goto(0, 0)
t.shape("track.gif")
t.stamp()

    # Unique shape: Star
def draw_star(x, y, size, color):
    t.goto(x, y)
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

t.shape("classic")
draw_star(0, -120, 100, "gold")

# --- Navigation ---




turtle.done()