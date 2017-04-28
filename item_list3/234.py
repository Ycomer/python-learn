import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Creat the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)
    #Creat the turtle Angie - Draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    #Creat the turtle Head - Draws  a triangle
    head = turtle.Turtle()
    head.shape("turtle")
    head.color("white")
    head.left(210)
    for x in range(0,3):
        head.forward(200)
        head.right(120)

    window.exitonclick()
draw_art()
