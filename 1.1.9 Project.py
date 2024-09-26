#Setting up the program
import os
import time
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

#1=Right 2=Left

#Intro
os.system("cls")
time.sleep(1)
print("Welcome to Build-a-Minion")
time.sleep(2)
os.system("cls")
while True:    
    start = input("Do you want to make a minion? ")
    if start == "yes" or start == "Yes" or start == "YES":
        print("Here we go!")
        os.system("cls")
        break
    elif start == "maybe" or start == "Maybe":
        continue
    else:
        continue

#Moving trtl to start body
painter.penup()
painter.right(90)
painter.forward(100)
painter.left(90)
painter.forward(100)
painter.pendown()

r = 300
#Makes Minion Body
def body(r):
    body_color = input("What color do you want the body to be?")
    painter.pencolor(body_color)
    painter.fillcolor(body_color)
    painter.begin_fill()
    painter.left(45)
    for loop in range(2):
        painter.circle(r,90)
        painter.circle(r/2,90)
    painter.end_fill()


def hair():
    painter.pencolor("black")
    painter.fillcolor("black")
    painter.begin_fill()
    painter.penup()
    painter.goto(-30,368)
    painter.setheading(100)
    painter.pendown()
    painter.forward(25)

    painter.penup()
    painter.goto(-15,368)
    painter.setheading(90)
    painter.forward(25)
    
    painter.penup()
    painter.goto(0,368)
    painter.setheading(80)
    painter.pendown()
    painter.forward(25)
    painter.end_fill()
    painter.penup()

def eyes():
    # Right Eye
    painter.fillcolor("#D3D3D3")
    painter.begin_fill()
    painter.penup()
    painter.goto(75,175)
    painter.pendown()
    painter.circle(50)
    painter.end_fill()




    painter.fillcolor("white")
    painter.begin_fill()
    painter.penup()
    painter.goto(75, 185)
    painter.pendown()
    painter.circle(40)
    painter.end_fill()




    # Outter Eye Color
    eye_color = input("What Color Eyes?")
    painter.fillcolor(eye_color)
    painter.begin_fill()
    painter.penup()
    painter.goto(75, 205)
    painter.pendown()
    painter.circle(20)
    painter.end_fill()




    # Inner Eye
    painter.fillcolor("black")
    painter.begin_fill()
    painter.penup()
    painter.goto(75, 215)
    painter.pendown()
    painter.circle(10)
    painter.end_fill()










    # Left Eye
    # Goggle
    painter.fillcolor("#D3D3D3")
    painter.begin_fill()
    painter.penup()
    painter.goto(-75, 175)
    painter.pendown()
    painter.circle(50)
    painter.end_fill()




    # White Part Of Eye
    painter.fillcolor("white")
    painter.begin_fill()
    painter.penup()
    painter.goto(-75, 185)
    painter.pendown()
    painter.circle(40)
    painter.end_fill()




    # Outter Eye Color
    painter.fillcolor(eye_color)
    painter.begin_fill()
    painter.penup()
    painter.goto(-75, 205)
    painter.pendown()
    painter.circle(20)
    painter.end_fill()
    # Inner Eye Color
    painter.fillcolor("black")
    painter.begin_fill()
    painter.penup()
    painter.goto(-75, 215)
    painter.pendown()
    painter.circle(10)
    painter.end_fill()
    painter.penup()

   

def clothes():
    clothes_color = input("What color do you want the clothes to be?")
    painter.pencolor(clothes_color)
    painter.fillcolor(clothes_color)
    painter.begin_fill()
    painter.penup()
    #painter.goto()
    painter.pendown()
    painter.setheading(90)
    painter.forward(150)
    x = 100
    y = 50
    
    #Straps 1 Start
    painter.right(45)
    painter.forward(120)
    painter.left(50)
    painter.forward(25)
    painter.left(125)
    painter.forward(173)
    #Straps 1 End

    painter.penup()
    painter.goto(x,y)
    painter.setheading(180)
    painter.pendown()
    painter.forward(210)
    x = painter.xcor()
    y = painter.ycor()
    
    #Straps 2 Start

    painter.setheading(135)
    painter.forward(125)
    painter.right(50)
    painter.forward(25)
    painter.right(125)
    painter.forward(178)
    #Straps 2 End
    
    painter.penup()
    painter.goto(x,y)
    painter.pendown()
    painter.setheading(270)
    painter.forward(150)
    painter.left(90)
    painter.forward(210)
    painter.end_fill()



def legs_boots():     
    # Start Leg 1
    painter.goto(100,-100)
    painter.setheading(-90)
    painter.pendown()
    painter.forward(100)

    # Start Boot 1
    boot_color = input("What color to you want the boots to be?")
    painter.pencolor(boot_color)
    painter.fillcolor(boot_color)
    painter.begin_fill()
    r = 37
    painter.penup()
    painter.forward(25)
    painter.pendown()
    painter.setheading(-45)
    for loop in range(2):
        painter.circle(r, 90)
        painter.circle(r / 2, 90)
    painter.end_fill()
    # End Boot 1

    # Start Leg 2
    painter.penup()
    painter.goto(-110, -100)
    painter.setheading(-90)
    painter.pendown()
    painter.forward(100)
    # End Leg 2

    # Start Boot 2
    painter.pencolor(boot_color)
    painter.fillcolor(boot_color)
    painter.begin_fill()
    painter.setheading(135)
    r = 37
    for loop in range(2):
        painter.circle(r, 90)
        painter.circle(r / 2, 90)
    painter.end_fill()
    painter.penup()
    # End Boot 2

def arms():
    arm_color = input("What color do you want the gloves to be?")
    #Go to Arm 1
    painter.penup()
    painter.goto(187,90)
    painter.pendown()
    #End 

    #Start Arm 1
    painter.setheading(-45)
    painter.forward(150)
    painter.setheading(45)
    #Start Gloves 1
    painter.fillcolor(arm_color)
    painter.begin_fill()
    
    #Setting variables for hands
    x_cord = 293
    y_cord = -21
    heading = 45
    for i in range (3):    
        r = 10
        painter.pendown()
        painter.setheading(heading)
        for loop in range(2):
            painter.circle(r, 90)
            painter.circle(r / 2, 90)
        painter.penup()
        painter.goto(x_cord,y_cord)
        heading = heading - 130
    painter.end_fill()
    #End
    #Go to Arm 2
    painter.penup()
    painter.goto(-187,90)
    painter.pendown()

    #Start Arm 2
    painter.setheading(-135)
    painter.forward(150)
    painter.setheading(135)

    #Start Gloves 2
    painter.fillcolor(arm_color)
    painter.begin_fill()
    #Setting variable for hands
    x_cord = -293
    y_cord = -16
    heading = 45
    for i in range (3):    
        r = 10
        painter.pendown()
        painter.setheading(heading)
        for loop in range(2):
            painter.circle(r, 90)
            painter.circle(r / 2, 90)
        painter.penup()
        painter.goto(x_cord,y_cord)
        heading = heading - 130
    painter.end_fill()




# Draw all parts of the minion
body(r)
clothes()
eyes()
legs_boots()
#hair()
arms()

# Hide the turtle and keep the window open
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()