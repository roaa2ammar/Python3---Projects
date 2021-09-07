# creating pictures using recursion and Python turtle library

import turtle


turtle.shape("circle")
turtle.color("white","yellow")
turtle.speed(10000)
def circles(n):
    if n == 250:
        return
    else:
        turtle.bgcolor("light blue")
        turtle.circle(2*n)
        turtle.circle(-2*n)
        turtle.left(n)
        circles(n+8)
    return

circles(200)
    

