
import turtle
import random

score = 0
lives = 3

wn = turtle.Screen()
wn.title("MaskUp")
wn.bgcolor("green")
wn.bgpic("retro_city.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("human.gif")
wn.register_shape("Evil-Virus.gif")
wn.register_shape("surgical-mask.gif")

# Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("human.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Create a list of good guys
good_guys = []

# Add the good_guys
for _ in range(3):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("surgical-mask.gif")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(-100, 250)
    good_guy.speed = random.uniform(0.3, 2.0)
    good_guys.append(good_guy)

# Create a list of bad guys
bad_guys = []

# Add the bad_guys
for _ in range(5):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("Evil-Virus.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(100, 250)
    bad_guy.speed = random.uniform(0.3, 1.0)
    bad_guys.append(bad_guy)

# Make the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
font = ("Courier", 24, "normal")
pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

# Make the message
def show_message(score):
    message = turtle.Turtle()
    message.hideturtle()
    message.speed(0)
    message.color("white")
    message.penup()
    message.goto(0, 0)
    font = ("Courier", 24, "normal")
    message.write("GAME OVER: TOO MUCH EXPOSURE TO VIRUS\n Score: {}\n!MASK UP and STAY SAFE!".format(score), align="center", font=font) 

# Functions
def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"

def stop_player():
    player.direction = "stop"

# Keyboard Binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeyrelease(stop_player, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeyrelease(stop_player, "Right")

# Main game loop
while True:
    # Update screen
    wn.update()

    # Move the player
    if player.direction == "left":
        x = player.xcor()
        if x > -365:
            x -= 0.8
            player.setx(x)
    
    if player.direction == "right":
        x = player.xcor()
        if x < 365:
            x += 0.8
            player.setx(x)

    # Move the good guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)

        # Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)

        # Check for a collision with player
        if good_guy.distance(player) < 40:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)
        
    # Move the bad guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)

        # Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)

        # Check for a collision with player
        if bad_guy.distance(player) < 40:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

    if lives < 0:
        pen.clear()
        bad_guy.clear()
        good_guy.clear()
        show_message(score)
   


wn.mainloop()