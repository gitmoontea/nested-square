import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("İç içe kare")

turtle_instance = turtle.Turtle()
turtle_instance.color("white")

init_value = 200
subtraction_value = 20
init = init_value
def shrinkingSquare():
    global subtraction_value
    global init_value
    for i in range(4):
        state = (i + 1 == 2) and init == init_value
        if(int(i + 1) % 2 != 0):
            turtle_instance.forward(init_value)
            turtle_instance.left(90)
        else:
            if(init_value > 0 and not state):
                init_value -= subtraction_value
            turtle_instance.forward(init_value)
            turtle_instance.left(90)


loop_count = int((init_value / subtraction_value))

for i in range(loop_count):
    if init_value != 0:
        shrinkingSquare()


turtle.done()
