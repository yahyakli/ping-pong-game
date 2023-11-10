# import turtle module
import turtle

p1 = str(input("player 1: "))
p2 = str(input("player 2: "))

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
ball.dx = 0.5
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
# pen.write("Player 1: {}  Player 2: {}".format(scoreL, scoreR), align="center", font=("Courier", 20, "normal"))
strscor = (f"{p1} : {scoreL}     {p2} : {scoreR}")
pen.write(strscor, align="center", font=("courier", 20, "normal"))








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

def midrab1_L():
    x =midrab1.xcor()
    x -=20
    x = midrab1.setx(x)


def midrab1_R():
    x =midrab1.xcor()
    x +=20
    x = midrab1.setx(x)


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


def midrab2_L():
    x =midrab2.xcor()
    x -=20
    x = midrab2.setx(x)


def midrab2_R():
    x =midrab2.xcor()
    x +=20
    x = midrab2.setx(x)



#keyboard bindings
wind.listen()
wind.onkeypress(midrab1_up,"w")
wind.onkeypress(midrab1_down,"s")
# wind.onkeypress(midrab1_L,"a")
# wind.onkeypress(midrab1_R,"d")
wind.onkeypress(midrab2_up,"Up")
wind.onkeypress(midrab2_down,"Down")
# wind.onkeypress(midrab2_L,"Left")
# wind.onkeypress(midrab2_R,"Right")

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
        c =0
        ball.dx = 0.3
        ball.dy = 0
        ball.goto(0,0)
        ball.dx *= -1
        midrab1.goto(-350, 0)
        midrab2.goto(350, 0)
        scoreL += 1
        pen.clear()
        # pen.write("Player 1: {}  Player 2: {}".format(scoreL, scoreR), align="center", font=("Courier", 20, "normal"))
        strscor = (f"{p1} : {scoreL}     {p2} : {scoreR}")
        pen.write(strscor, align="center", font=("courier", 20, "normal"))


    if ball.xcor() < -390:
        c =0
        ball.dx = 0.3
        ball.dy = 0
        ball.goto(0,0)
        ball.dx *= -1
        midrab1.goto(-350, 0)
        midrab2.goto(350, 0)
        scoreR += 1
        pen.clear()
        # pen.write("Player 1: {}  Player 2: {}".format(scoreL, scoreL), align="center", font=("Courier", 20, "normal"))
        strscor = (f"{p1} : {scoreL}     {p2} : {scoreR}")
        pen.write(strscor, align="center", font=("courier", 20, "normal"))



    #midrab and ball
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < midrab2.ycor() + 40 and ball.ycor() > midrab2.ycor() -40:
    # if ball.xcor() > midrab2.xcor() and ball.xcor() < midrab2.xcor() +10 and ball.ycor() < midrab2.ycor() +40 and ball.ycor() > midrab2.ycor() -40:
        ball.setx(340)
        if c ==0:
            ball.dy = 0.3
            c +=1
        ball.dx *= -1
        ball.color("red")

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < midrab1.ycor() + 40 and ball.ycor() > midrab1.ycor() - 40:
    # if ball.xcor() < midrab1.xcor() and ball.xcor() > midrab1.xcor() -10 and ball.ycor() < midrab1.ycor() +40 and ball.ycor() > midrab1.ycor() -40:
        ball.setx(-340)
        if c ==0:
            ball.dy = 0.3
            c+=1
        ball.dx *= -1
        ball.color("blue")
