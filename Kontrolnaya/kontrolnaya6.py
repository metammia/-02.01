import turtle
turtle.hideturtle()
turtle.ht()
def draw_circles(radius):
    colors = ['blue', 'orange', 'green', 'red']
    proportions = [1, 1.5, 2, 2.5] 

    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()

    for color, proportion in zip(colors, proportions):
        turtle.color(color)
        turtle.circle(radius * proportion)

    turtle.done()

radius = int(input("Введите радиус первого круга: "))
draw_circles(radius)
