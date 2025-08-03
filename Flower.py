import turtle

wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.title("Flower")



#------------------------------------------------------
turt1 = turtle.Turtle()
turt1.color("red")
turt1.shape("blank")
turt1.pensize(5)
turt1.setpos(0,0)
turt1.speed(0)
#-------------------------------------------------------


for _ in range(18):
    turt1.color("blue")
    turt1.circle(100,75)
    turt1.penup()
    turt1.setpos(0,0)
    turt1.pendown()
    turt1.circle(-100,75)
    turt1.penup()
    turt1.setpos(0,0)
    turt1.pendown()
    turt1.left(20)

for _ in range(18):
    turt1.color("purple")
    turt1.circle(120,80)
    turt1.penup()
    turt1.setpos(0,0)
    turt1.pendown()
    turt1.circle(-120,80)
    turt1.penup()
    turt1.setpos(0,0)
    turt1.pendown()
    turt1.left(20)

for _ in range(18):
    turt1.color("red")
    turt1.circle(140,85)
    turt1.penup()
    turt1.setpos(0,0)
    turt1.pendown()
    turt1.circle(-140,85)
    turt1.penup()
    turt1.setpos(0,0)
    turt1.pendown()
    turt1.left(20)

turt1.speed(.5)

turt1.color("blue")
turt1.penup()
turt1.setpos(-200,0)
turt1.pendown()
turt1.left(90)
turt1.circle(-200.360)

turt1.color("purple")
turt1.penup()
turt1.setpos(-210,0)
turt1.pendown()
turt1.circle(-210.360)

turt1.color("red")
turt1.penup()
turt1.setpos(-220,0)
turt1.pendown()
turt1.circle(-220.360)

turt1.color("purple")
turt1.penup()
turt1.setpos(-230,0)
turt1.pendown()
turt1.circle(-230.360)

turt1.color("blue")
turt1.penup()
turt1.setpos(-240,0)
turt1.pendown()
turt1.circle(-240.360)



turtle.done()
