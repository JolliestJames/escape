def escaped(position):
    x = int(position[0])
    y = int(position[1])
    return x < -35 or x > 35 or y < -35 or y > 35

def draw_line():
    angle = 0
    step = 5
    t = turtle.Turtle()
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
    L = []
    for i in range(1, number + 1):
        t.penup()
        t.goto(-i, -i)
        t.pendown()
        L.extend(draw_square(t, i * 2))
        return L

def draw_squares_until_escaped(n):
    t = turtle.Turtle()
    L = draw_squares(n)
    with open("data_square", "wb") as f:
        pickle.dump(L, f)
