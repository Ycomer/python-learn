import turtle
 
def draw_square ():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(1)
    for x in range(0,4):
        brad.forward(100)
        brad.right(90)
	
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("blue")
    angie.circle(100)

    head = turtle.Turtle()
    head.shape("turtle")
    head.color("white")
    head.left(210)

    for x in range(0,3):
        head.forward(200)
        head.right(120)
    
    window.exitonclick()
draw_square()
