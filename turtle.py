import turtle 

my_turtle = turtle.Turtle()

my_turtle.forward(80)

my_turtle.shapesize(3)

my_turtle.shape('turtle')

my_turtle.color('red')

for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(50)

for i in range(60):
    if i%2 == 0:
        my_turtle.forward(100)
        my_turtle.right(60)
    else:
        my_turtle.forward(150)
        my_turtle.right(80)
