from graphics import *
import time
import math

num_dots = 50


def follow(prev_dot, curr_dot):
    dx = prev_dot.getCenter().getX() - curr_dot.getCenter().getX()
    dy = prev_dot.getCenter().getY() - curr_dot.getCenter().getY()
    dist = ((dx ** 2) + (dy ** 2)) ** 0.5
    if dist > 30:
        angle = math.atan2(dy, dx)
        dx_new = 10 * math.cos(angle)
        dy_new = 10 * math.sin(angle)
        curr_dot.move(dx_new, dy_new)


def move_dots(dots):
    for i in range(1, len(dots)):
        prev_dot = dots[i - 1]
        curr_dot = dots[i]
        follow(prev_dot, curr_dot)


def path_of_dots(win):
    dots = []
    dot = Circle(Point(50, 50), 5)
    dot.setFill("black")
    dot.draw(win)
    dots.append(dot)
    for i in range(num_dots - 1):
        dot = Circle(Point(50 + (i + 1) * 30, 50), 5)
        dot.setFill("black")
        dot.draw(win)
        dots.append(dot)

    x = 0
    while x < 400:
        dots[0].move(0, 1)
        move_dots(dots)
        time.sleep(0.01)
        x += 1

    while x < 800:
        dots[0].move(1, 0)
        move_dots(dots)
        time.sleep(0.01)
        x += 1
    while x < 1200:
        dots[0].move(0, -1)
        move_dots(dots)
        time.sleep(0.01)
        x += 1
    while x < 1600:
        dots[0].move(-1, 0)
        move_dots(dots)
        time.sleep(0.01)
        x += 1

def main():
    win = GraphWin("Dot Trail", 500, 500)
    win.setBackground("gray")


    path_of_dots(win)

    win.getMouse()
    win.close()


main()