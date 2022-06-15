#importing libraries
import turtle as turt
import random
import time


#creating turtle screen
screen = turt.Screen()
# Name
screen.title('PySnek')
# Height and width of the screen
screen.setup(width = 700, height = 700)
# Will turn off screen updater
screen.tracer(0)
turt.bgcolor('black')



##creating a border for our game
# right() is used to turn clockwise while left() is for counterclockwise

turt.speed(5)
turt.pensize(4)
turt.penup()
turt.goto(-310, 250)
turt.pendown()
turt.color('white')
turt.forward(600)
turt.right(90)
turt.forward(500)
turt.right(90)
turt.forward(600)
turt.right(90)
turt.forward(500)
# Will not draw while the snake is moving
turt.penup()
turt.hideturtle()

#score
score = 0
delay = 0.1


#snake
# Turtle() creates a new turtle obj.
snek = turt.Turtle()
snek.speed(0)
snek.shape('square')
snek.color("white")
snek.penup()
# Moves the turtle at x and y coords
snek.goto(0,0)
snek.direction = 'stop'


#food
fruit = turt.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30, 30)

old_fruit=[]

#scoring
scoring = turt.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score :", align="center", font=("Courier", 24, "bold"))


#######define how to move
def snek_go_up():
    if snek.direction != "down":
        snek.direction = "up"

def snek_go_down():
    if snek.direction != "up":
        snek.direction = "down"

def snek_go_left():
    if snek.direction != "right":
        snek.direction = "left"

def snek_go_right():
    if snek.direction != "left":
        snek.direction = "right"

def snek_move():
    if snek.direction == "up":
        y = snek.ycor()
        snek.sety(y + 20)

    if snek.direction == "down":
        y = snek.ycor()
        snek.sety(y - 20)

    if snek.direction == "left":
        x = snek.xcor()
        snek.setx(x - 20)

    if snek.direction == "right":
        x = snek.xcor()
        snek.setx(x + 20)

# Keyboard bindings
# Listens when a key is press via listen()
screen.listen()
# Directional keys indicate movements with onkeypresses
screen.onkeypress(snek_go_up, "Up")
screen.onkeypress(snek_go_down, "Down")
screen.onkeypress(snek_go_left, "Left")
screen.onkeypress(snek_go_right, "Right")

#main loop

while True:
        screen.update()
            #snake and fruit coliisions
        if snek.distance(fruit)< 20:
                x = random.randint(-290, 270)
                y = random.randint(-240, 240)
                fruit.goto(x,y)
                scoring.clear()
                score+=1
                scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))
                delay-=0.001
                
                ## creating new_ball
                new_fruit = turt.Turtle()
                new_fruit.speed(0)
                new_fruit.shape('square')
                new_fruit.color('red')
                new_fruit.penup()
                old_fruit.append(new_fruit)
                

        #adding ball to snake
        
        for index in range(len(old_fruit) -1, 0, -1):
                a = old_fruit[index-1].xcor()
                b = old_fruit[index-1].ycor()

                old_fruit[index].goto(a, b)
                                     
        if len(old_fruit)>0:
                a= snek.xcor()
                b = snek.ycor()
                old_fruit[0].goto(a, b)
        snek_move()

        ##snake and border collision    
        if snek.xcor()>280 or snek.xcor()< -300 or snek.ycor()> 240 or snek.ycor()< -240:
                time.sleep(1)
                # clear() will delete all the drawings of the turtle on the screen
                screen.clear()
                screen.bgcolor('black')
                scoring.goto(0,0)
                scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


        ## snake collision
        for food in old_fruit:
                if food.distance(snek) < 20:
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor('black')
                        scoring.goto(0, 0)
                        scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


                
        time.sleep(delay)

turtle.Terminator()
