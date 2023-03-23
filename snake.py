import turtle 
import random as rd
import time

score = 0 
hs = 0
delay=0.1

#Making the screen
ws=turtle.Screen()
ws.title("Snake")
ws.bgcolor("black")
ws.setup(width=600,height=600)
#Tracer method defines at which frame the final screen will be updated. tracer(1) will make it update at each frame 
ws.tracer(0)

#hd of the snake #The hd will be intialized as a turtle object 
hd=turtle.Turtle()
hd.shape('square')
hd.color('yellow')
hd.penup()
hd.goto(0,0)
#Removes the line being drawn aka lifts the pen up so no line is being drawn, its companion pendown() does the oppposite.  
hd.direction="Stop"

#Food
food = turtle.Turtle()
colors=rd.choice(["red","green","yellow"])
shapes = rd.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.color(colors)
food.shape(shapes)
food.penup()
food.goto(0,100)

#Display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",font=("candara", 24, "bold"))

#Controls for moving the snake hd
def goup():
    if hd.direction != "down":
        hd.direction = "up"

def godown():
    if hd.direction != "up":
        hd.direction = "down"

def goleft():
    if hd.direction != "right":
        hd.direction = "left"

def goright():
    if hd.direction != "left":
        hd.direction = "right"

def movement():
    if hd.direction == "up":
        y = hd.ycor()
        hd.sety(y+20)
    if hd.direction == "down":
        y = hd.ycor()
        hd.sety(y-20)
    if hd.direction == "left":
        x = hd.xcor()
        hd.setx(x-20)
    if hd.direction == "right":
        x = hd.xcor()
        hd.setx(x+20)

ws.listen()
ws.onkeypress(goup,"Up")
ws.onkeypress(godown,"Down")
ws.onkeypress(goleft,"Left")
ws.onkeypress(goright,"Right")

#Core Gameplay
segments = []

# Main Gameplay
while True:
	ws.update()
	if hd.xcor() > 290 or hd.xcor() < -290 or hd.ycor() > 290 or hd.ycor() < -290:
		time.sleep(1)
		hd.goto(0, 0)
		hd.direction = "Stop"
		for segment in segments:
			segment.goto(1000, 1000)
		segments.clear()
		score = 0
		delay = 0.1
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(score, hs), align="center", font=("candara", 24, "bold"))
	if hd.distance(food) < 20:
		x = rd.randint(-270, 270)
		y = rd.randint(-270, 270)
		food.goto(x, y)

		# Adding segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("orange") # tail colour
		new_segment.penup()
		segments.append(new_segment)
		delay -= 0.001
		score += 10
		if score > hs:
			hs = score
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(score, hs), align="center", font=("candara", 24, "bold"))
	# Checking for hd collisions with body segments
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)
	if len(segments) > 0:
		x = hd.xcor()
		y = hd.ycor()
		segments[0].goto(x, y)
	movement()
	for segment in segments:
		if segment.distance(hd) < 20:
			time.sleep(1)
			hd.goto(0, 0)
			hd.direction = "stop"
			colors = rd.choice(['red', 'blue', 'green'])
			shapes = rd.choice(['square', 'circle'])
			for segment in segments:
				segment.goto(1000, 1000)
			segment.clear()

			score = 0
			delay = 0.1
			pen.clear()
			pen.write("Score : {} High Score : {} ".format(score, hs), align="center", font=("candara", 24, "bold"))
	time.sleep(delay)

ws.mainloop()
