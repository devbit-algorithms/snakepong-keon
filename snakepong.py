import turtle 
import time 
import random 
  
delay = 0.1
  
  
# Gamewindow 
gamewindow = turtle.Screen()
gamewindow.title("Snake Pong")
gamewindow.bgcolor("black")
gamewindow.setup(width=600, height=600)
gamewindow.tracer(0) 

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

# Ball
ball = turtle.Turtle()
ball.speed(30)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = -5

# snake
snake = turtle.Turtle() 
snake.shape("square") 
snake.color("yellow") 
snake.penup() 
snake.goto(0, 0) 
snake.direction = "Stop"
  
cpu = 0
player = 0

# scoreboard
score = turtle.Turtle() 
score.speed(0) 
score.color("lightgreen") 
score.penup() 
score.hideturtle() 
score.goto(0, 260) 
score.write("CPU : 0    Player: 0", 
             align="center", font=("Courier", 24, "normal")) 
  
  
def up(): 
    if snake.direction != "down": 
        snake.direction = "up"  
  
def down(): 
    if snake.direction != "up": 
        snake.direction = "down"  
  
def left(): 
    if snake.direction != "right": 
        snake.direction = "left"  
  
def right(): 
    if snake.direction != "left": 
        snake.direction = "right"  
  
def move(): 
    if snake.direction == "up": 
        y = snake.ycor() 
        snake.sety(y+20) 
    if snake.direction == "down": 
        y = snake.ycor() 
        snake.sety(y-20) 
    if snake.direction == "left": 
        x = snake.xcor() 
        snake.setx(x-20) 
    if snake.direction == "right": 
        x = snake.xcor() 
        snake.setx(x+20) 
              
gamewindow.listen() 
gamewindow.onkeypress(up, "Up") 
gamewindow.onkeypress(down, "Down") 
gamewindow.onkeypress(left, "Left") 
gamewindow.onkeypress(right, "Right") 
  
snakeparts = [] 
    
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
        score.clear() 
        score.write("CPU : {}    Player: {}".format( 
                      cpu, player), align="center", 
                      font=("Courier", 24, "normal")) 
  
    if ball.xcor() < -500: 
        ball.goto(0, 0) 
        ball.dy *= -1
        player += 1
         # add new snake segment 
        new_segment = turtle.Turtle() 
        new_segment.speed(0) 
        new_segment.shape("square") 
        new_segment.color("yellow") 
        new_segment.penup() 
        snakeparts.append(new_segment) 
        delay -= 0.001
        score.clear() 
        score.write("CPU : {}    Player: {}".format( 
                                 cpu, player), align="center", 
                                 font=("Courier", 24, "normal"))

    if snake.xcor() > 600 or snake.xcor() < -600 or snake.ycor() > 400 or snake.ycor() < -400: 
        time.sleep(1) 
        snake.goto(0, 0) 
        snake.direction = "Stop" 
        delay = 0.1
    
    if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor() < paddle.ycor()+50 and ball.ycor() > paddle.ycor()-50): 
        ball.setx(-360) 
        ball.dx*=-1
   
    if (ball.xcor() > snake.xcor() - 10 and ball.xcor() < snake.xcor() + 10) and (ball.ycor() < snake.ycor()+40 and ball.ycor() > snake.ycor()-40): 
        ball.dx*=-1
       
    
    # Checking for snake collisions with body segments 
    for index in range(len(snakeparts)-1, 0, -1): 
        x = snakeparts[index-1].xcor() 
        y = snakeparts[index-1].ycor() 
        snakeparts[index].goto(x, y)
        if (ball.xcor() > x - 10 and ball.xcor() < x + 10) and (ball.ycor() < y + 40 and ball.ycor() > y -40):  
            ball.dx*=-1 
    if len(snakeparts) > 0: 
        x = snake.xcor() 
        y = snake.ycor() 
        snakeparts[0].goto(x, y) 
    move() 
    for segment in snakeparts: 
        if segment.distance(snake) < 20: 
            time.sleep(1) 
            snake.goto(0, 0) 
            snake.direction = "stop"
            for segment in snakeparts: 
                segment.goto(1000, 1000) 
            segment.clear() 
            delay = 0.1
    time.sleep(delay) 
  
gamewindow.mainloop() 