# import turtle module
import turtle

wind = turtle.Screen()
wind.title("ping pong by yahya")
wind.bgcolor("black")
wind.tracer(0)
wind.setup(height=600, width=800)

#midrab1
midrab1 = turtle.Turtle()
midrab1.speed(0)
midrab1.shape("square")
midrab1.color("blue")
midrab1.penup()
midrab1.goto(-350,0)
midrab1.shapesize(stretch_wid=5,stretch_len=1)

#midrab2
midrab2 = turtle.Turtle()
midrab2.speed(0)
midrab2.shape("square")
midrab2.color("red")
midrab2.penup()
midrab2.goto(350,0)
midrab2.shapesize(stretch_wid=5,stretch_len=1)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.dx = 0.4
ball.dy = 0

#score
scoreR =0
scoreL =0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player 1: {}  Player 2: {}".format(scoreL, scoreR), align="center", font=("Courier", 20, "normal"))








#functions
def midrab1_up():
    if midrab1.ycor() <250:
        y = midrab1.ycor()
        y += 50
        y = midrab1.sety(y)

def midrab1_down():
    if midrab1.ycor() >-250:
        y = midrab1.ycor()
        y -= 50
        y = midrab1.sety(y)


def midrab2_up():
    if midrab2.ycor() <250:
        y = midrab2.ycor()
        y += 50
        y = midrab2.sety(y)

def midrab2_down():
    if midrab2.ycor() >-250:
        y = midrab2.ycor()
        y -= 50
        y = midrab2.sety(y)

#keyboard bindings
wind.listen()
wind.onkeypress(midrab1_up,"w")
wind.onkeypress(midrab1_down,"s")
wind.onkeypress(midrab2_up,"Up")
wind.onkeypress(midrab2_down,"Down")

c = 0
#main game loop
while True:
    wind.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        midrab1.goto(-350, 0)
        midrab2.goto(350, 0)
        scoreL += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(scoreL, scoreR), align="center", font=("Courier", 20, "normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        midrab1.goto(-350, 0)
        midrab2.goto(350, 0)
        scoreR += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(scoreL, scoreL), align="center", font=("Courier", 20, "normal"))



    #midrab and ball
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < midrab2.ycor() + 40 and ball.ycor() > midrab2.ycor() -40:
        ball.setx(340)
        if c == 0:
            ball.dy = 0.3
            c +=1
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < midrab1.ycor() + 40 and ball.ycor() > midrab1.ycor() - 40:
        ball.setx(-340)
        if c ==0:
            ball.dy = 0.3
            c+=1
        ball.dx *= -1
