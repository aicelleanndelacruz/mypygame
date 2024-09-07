import turtle
import random

screen = turtle.Screen()
screen.title("Turtle Game with Obstacles and Collectibles")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(1)
player.shapesize(stretch_wid=2, stretch_len=2) 

def create_collectible():
    collectible = turtle.Turtle()
    collectible.shape("circle")
    collectible.color("yellow")
    collectible.penup()
    collectible.goto(random.randint(-290, 290), random.randint(-290, 290))
    return collectible


def create_obstacle(x, y):
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.penup()
    obstacle.goto(x, y)
    return obstacle

def display_game_over():
    game_over = turtle.Turtle()
    game_over.hideturtle()
    game_over.penup()
    game_over.color("black")
    game_over.goto(0, 50)
    game_over.write("Game Over", align="center", font=("Arial", 36, "bold"))
    

    restart_instructions = turtle.Turtle()
    restart_instructions.hideturtle()
    restart_instructions.penup()
    restart_instructions.color("black")
    restart_instructions.goto(0, -50)
    restart_instructions.write("Press OK to restart", align="center", font=("Arial", 18, "bold"))

def update_score_display():
    score_display.clear()
    score_display.write(f"Score: {score}", align="left", font=("Arial", 18, "normal"))


def reset_game():
    global obstacles, collectible, score
    player.goto(0, 0)
    player.setheading(0)
    player.color("green")
    player.shapesize(stretch_wid=2, stretch_len=2)  

    
    for obs in obstacles:
        obs.hideturtle()
    
    
    obstacles = []
    for _ in range(20):  
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        obstacles.append(create_obstacle(x, y))
    
    if collectible:
        collectible.hideturtle()
    
    collectible = create_collectible()
    
    score = 0
    update_score_display()

obstacles = []
collectible = None
score = 0

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-290, 260)  
score_display.color("black")
update_score_display()

reset_game()

def move_up():
    player.setheading(90)
    player.forward(20)

def move_down():
    player.setheading(270)
    player.forward(20)

def move_left():
    player.setheading(180)
    player.forward(20)

def move_right():
    player.setheading(0)
    player.forward(20)
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")


def check_collisions():
    for obstacle in obstacles:
        if player.distance(obstacle) < 30:  
            return "obstacle"
    if player.distance(collectible) < 20:
        return "collectible"
    return None


while True:
    player.forward(0) 
    collision = check_collisions()
    if collision == "obstacle":
        player.hideturtle()
        display_game_over()  
        turtle.textinput("Game Over", "You hit an obstacle! Press OK to restart.")
        reset_game()  
        player.showturtle()
    elif collision == "collectible":
        collectible.hideturtle()
        collectible = create_collectible() 

     
        current_wid = player.shapesize()[0]
        current_len = player.shapesize()[1]
        player.shapesize(stretch_wid=current_wid + 0.5, stretch_len=current_len + 0.5)
        player.color("blue") 
        
        score += 10
        update_score_display()
    screen.update()
