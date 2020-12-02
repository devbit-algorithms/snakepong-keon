# python library to make screens
import turtle

gamewindow = turtle.Screen()
gamewindow.title("Snake Pong")
gamewindow.bgcolor("black")
gamewindow.setup(width=600, height=600)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("red")
paddle.shapesize(stretch_wid=8, stretch_len=2)
paddle.penup()
paddle.goto(-400, 0)
paddle.dx = 5
paddle.dy = -5
Pspeed = 2

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=8, stretch_len=2)
paddle2.penup()
paddle2.goto(400, -200)
paddle2.dx = 5
paddle2.dy = -5

# Snake
snake = turtle.Turtle()

# Ball
ball = turtle.Turtle()
ball.speed(30)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = -5

cpu = 0
right_player = 0

sketch = turtle.Turtle() 
sketch.speed(0) 
sketch.color("blue") 
sketch.penup() 
sketch.hideturtle() 
sketch.goto(0, 260) 
sketch.write("CPU : 0    Right_player: 0", 
             align="center", font=("Courier", 24, "normal")) 

while True:
    gamewindow.update()
   
    ball.setx(ball.xcor()+ball.dx) 
    ball.sety(ball.ycor()+ball.dy)
    
    if paddle.ycor() > ball.ycor():
        paddle.sety(paddle.ycor() - Pspeed)

    elif paddle.ycor() < ball.ycor():
        paddle.sety(paddle.ycor() + Pspeed)    

    if ball.ycor() > 280: 
        ball.sety(280) 
        ball.dy *= -1
  
    if ball.ycor() < -280: 
        ball.sety(-280) 
        ball.dy *= -1
  
    if ball.xcor() > 500: 
        ball.goto(0, 0) 
        ball.dy *= -1
        cpu += 1
        sketch.clear() 
        sketch.write("CPU : {}    Right_player: {}".format( 
                      cpu, right_player), align="center", 
                      font=("Courier", 24, "normal")) 
  
    if ball.xcor() < -500: 
        ball.goto(0, 0) 
        ball.dy *= -1
        right_player += 1
        sketch.clear() 
        sketch.write("CPU : {}    Right_player: {}".format( 
                                 cpu, right_player), align="center", 
                                 font=("Courier", 24, "normal")) 
  

    # Paddle ball collision         
    if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor()<paddle.ycor()+40 and ball.ycor()>paddle.ycor()-40): 
        ball.setx(-360) 
        ball.dx*=-1

    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < paddle2.ycor()+40 and ball.ycor() > paddle2.ycor()-40): 
        ball.setx(360) 
        ball.dx*=-1