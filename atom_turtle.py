import turtle

def draw_atom():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    atom = turtle.Turtle()
    atom.speed(0)  # Set the drawing speed to the fastest
    
    # Draw nucleus
    atom.color("black")
    atom.begin_fill()
    atom.circle(50)
    atom.end_fill()
    
    # Draw electron orbits
    for orbit in range(3):
        atom.penup()
        atom.goto(0, -20 * (orbit + 1))
        atom.pendown()
        atom.circle(20 * (orbit + 1))
    
    # Draw electrons
    electrons = ["blue", "green", "red"]
    for i, electron in enumerate(electrons):
        atom.penup()
        atom.goto(60, -20 * (i + 1))
        atom.pendown()
        atom.color(electron)
        atom.begin_fill()
        atom.circle(10)
        atom.end_fill()
    
    atom.hideturtle()

draw_atom()
turtle.done()
