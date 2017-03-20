import turtle
def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1, 20)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1000, 800, 0, 0)
    pythonsize = 15
    turtle.pensize(pythonsize)
    turtle.pencolor("red")
    turtle.seth(10)
    drawSnake(40,80,5,pythonsize/2)

main() 
