import turtle
def spiral(sides, trun, color, width):
    
    t = turtle.Turtle()
    t.color(color)
    t.width(width)
    t.speed(0)
    for n in range(sides):
        t.forward(n)
        t.right(trun)
        
    
spiral(150, 45, "cyan", 5)
