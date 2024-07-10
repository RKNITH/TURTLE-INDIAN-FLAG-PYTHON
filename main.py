#making Indian Flag using python turtle

from turtle import *

#canvas size
setup(700,500)
#shape for turtle
shape("triangle")
#speed for turtle
speed(15)
#background color
bgcolor("#DAF7A6")

def rect(leng,width,filled):
    setheading(0)
    penup()
    pendown()
    if filled==True:
        begin_fill()
    forward(leng)
    right(90)
    forward(width)
    right(90)
    forward(leng)
    right(90)
    forward(width)
    if filled==True: 
        end_fill()

def triangle(a,b,c,filled):
    
    if filled==True:
        begin_fill()
    right(45)
    forward(a)
    right(90)
    forward(b)
    right(135) 
    forward(c)
    if filled==True:
        end_fill()   
    
def rod():
    penup()
    goto(-185,182)
    pendown()
    color("black","black")
    rect(16,274,True)
    

def tip():
    penup()
    goto(-185,182)
    pendown()
    color("black","blue")
    triangle(11.3,11.3,16,True)

def obox():
         
    penup()
    goto(-169,182)
    pendown()
    color("black","orange")
    rect(200,40,True)

def midbox():
    penup()
    goto(-169,142) 
    right(90)
    pendown()   
    color("black","white")
    rect(200,40,True)

def gbox():
    penup()
    goto(-169,102) 
    right(90)
    pendown()   
    color("black","green")
    rect(200,40,True)

def chakra():
    penup()
    goto(-49,122)
    speed(30)
    pendown()
    color("black","white")
    circle(20,360)
    penup()
    goto(-69,122)
    #to draw spikes      
    for j in range(28):
        penup()
        goto(-69,122)
        pendown()
        color("blue")
        forward(20)
        goto(-69,122)
        right(13)
    speed(15)    
#to draw string for the flag
def string():
    penup()
    goto(-185,182)
    left(120)
    pendown()
    color("blue","blue")
    circle(63,140)
    left(180)
    circle(63,-180)   

def knot():    
    for i in range(38):

        color("blue")
        speed(300)
        forward(10)
        left(180)
        forward(10)
        right(13)
        width(1)
              

def flag(): 

    width(1)               
    rod()
    tip()
    obox()
    midbox()
    gbox()
    chakra()
    string()
    knot()
    speed(15)
# to write "i love india"
def i():
    
    penup()
    goto(70,10)
    width(10)   
    pendown()
    color("black","black") 
    goto(70,-30)
def letter():
    penup()
    goto(-10,-60)
    left(45)
    left(180)
    pendown()
    forward(40)
    left(90)
    forward(30)
    # drawing o
    penup()
    goto(40,-60)
    left(200)
    pendown()
    circle(20,360)
    penup()
    goto(80,-60)
    pendown()
    goto(100,-100)
    left(90)
    goto(120,-60)
    penup()
    goto(170,-65)
    right(110)
    pendown()
    forward(30)
    left(90)
    forward(40)
    left(90)
    forward(30)
    penup()
    goto(140,-80)
    pendown()
    forward(30)
    #india
    penup()
    right(78)
    goto(-30,-120)
    pendown()
    forward(40)
    penup()
    left(180)
    goto(-10,-160)
    pendown()
    forward(40)
    right(135)
    forward(50)
    left(135)
    forward(40)
    penup()
    goto(40,-120)
    left(180)
    pendown()
    forward(40)
    right(90)
    right(180)
    circle(20,180)
    left(90)
    penup()
    goto(75,-120)
    pendown()
    forward(40)
    penup()
    goto(95,-160)
    pendown()
    goto(115,-120)
    right(90)
    goto(135,-160)
    penup()
    goto(105,-140)
    left(180)
    pendown()
    forward(20)

#final execution
flag()
left(180)
penup()
i()
penup()
letter() 
#to hide turtle            
hideturtle()
#to close canvas window on click   
exitonclick()       
    


    