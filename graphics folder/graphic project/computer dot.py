from graphics import *
import time
import math

num_dots = 15


def move_dots(dots):
    for i in range(len(dots)):
        if i == 0:
            dots[i].move(1, 1)
        else:
            prev_dot = dots[i - 1]
            curr_dot = dots[i]
            dx = prev_dot.getCenter().getX() - curr_dot.getCenter().getX()
            dy = prev_dot.getCenter().getY() - curr_dot.getCenter().getY()
            dist = ((dx ** 2) + (dy ** 2)) ** 0.5
            if dist > 30:
                angle = math.atan2(dy, dx)
                dx_new = 10 * math.cos(angle)
                dy_new = 10 * math.sin(angle)
                curr_dot.move(dx_new, dy_new)

def main():
    win = GraphWin("Dot Trail", 500, 500)
    win.setBackground("gray")

    dots = []
    for i in range(num_dots):
        dot = Circle(Point(50 + i * 30, 50), 5)
        dot.setFill("black")
        dot.draw(win)
        dots.append(dot)

    x = 0
    while x < 200:
        move_dots(dots)
        time.sleep(0.01)
        x += 1

    win.getMouse()
    win.close()

main()