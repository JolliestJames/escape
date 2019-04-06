import argparse
import inspect
import random
import pickle
import turtle

def draw_bag():
    turtle.shape('turtle')
    turtle.pen(pencolor='green', pensize=5)
    turtle.penup()
    turtle.goto(-35, 35)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)

def escaped(position):
    x = int(position[0])
    y = int(position[1])
    return x < -35 or x > 35 or y < -35 or y > 35

def draw_line():
    angle = 0
    step = 5
    t = turtle.Turtle()
    t.shape('turtle')
    t.pen(pencolor='green', pensize=5)
    while not escaped(t.position()):
        t.left(angle)
        t.forward(step)

def draw_square(t, size):
    L = []
    for i in range(4):
        t.forward(size)
        t.left(90)
        store_position_data(L, t)
    return L

def store_position_data(L, t):
    position = t.position()
    L.append([position[0], position[1], escaped(position)])

def draw_squares(number):
    t = turtle.Turtle()
    t.shape('turtle')
    L = []
    for i in range(1, number + 1):
        t.penup()
        t.goto(-i, -i)
        t.pendown()
        L.extend(draw_square(t, i * 2))
    return L

def draw_squares_until_escaped(number):
    t = turtle.Turtle()
    t.shape('turtle')
    L = draw_squares(number)
    with open("data_square", "wb") as f:
        pickle.dump(L, f)

def draw_triangles(number):
    t = turtle.Turtle()
    t.shape('turtle')
    for i in range(1, number):
        t.forward(i*10)
        t.right(120)

def draw_spirals_until_escaped():
    t = turtle.Turtle()
    t.shape('turtle')
    t.penup()
    t.left(random.randint(0, 360))
    t.pendown()

    i = 0
    turn = 360/random.randint(1, 10)
    L = []
    store_position_data(L, t)
    while not escaped(t.position()):
        i += 1
        t.forward(i*5)
        t.right(turn)
        store_position_data(L, t)

    return L

def draw_random_spirangles():
    L = []
    for i in range(10):
        L.extend(draw_spirals_until_escaped())

    with open("data_rand", "wb") as f:
        pickle.dump(L, f)

if __name__ == '__main__':
    functions = {
        "line": draw_line,
        "squares": draw_squares_until_escaped,
        "triangles": draw_triangles,
        "spirangles": draw_random_spirangles
    }

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--function", choices=functions, help="One of" + ','.join(functions.keys()))
    parser.add_argument("-n", "--number", default=50, type=int, help="How many?")
    args = parser.parse_args()

    try:
        f = functions[args.function]
        turtle.setworldcoordinates(-70., -70., 70., 70.)
        draw_bag()
        turtle.hideturtle()
        if len(inspect.getargspec(f).args) == 1:
            f(args.number)
        else:
            f()
        turtle.mainloop()
    except KeyError:
        parser.print_help()
