import turtle

wn = turtle.Screen()
wn.setup(width=900, height=600)
wn.bgcolor("black")
wn.title("Circles")

# Create a turtle object
turt1 = turtle.Turtle()
turt1.color("purple")
turt1.shape("arrow")
turt1.penup()
turt1.goto(-50,-50)
turt1.pendown()

turt2 = turtle.Turtle()
turt2.color("red")
turt2.shape("arrow")
turt1.penup()
turt1.goto(25,-180)
turt1.pendown()


turt3 = turtle.Turtle()
turt3.color("blue")
turt3.shape("arrow")
turt3.penup()
turt3.goto(-25,-80)
turt3.pendown()



# Set the drawing speed (optional, 0 is fastest)
turt1.speed(0) 
turt2.speed(0)
turt3.speed(10)

while True:
    for _ in range(4): 
        turt1.forward(100)
        turt1.left(70)

        turt2.forward(150)
        turt2.right(70)

        turt3.forward(200)
        turt3.right(150)

# Keep the window open until closed manually
turtle.done()



