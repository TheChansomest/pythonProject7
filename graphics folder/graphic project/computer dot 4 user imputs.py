from graphics import *
import time
import math

num_dots = 29
distance_between_dots = 40
size = 5
speed_of_follow = 5
speed = 0.001

def follow(prev_dot, curr_dot, target_pos):
    dx = prev_dot.getCenter().getX() - curr_dot.getCenter().getX()
    dy = prev_dot.getCenter().getY() - curr_dot.getCenter().getY()
    dist = ((dx ** 2) + (dy ** 2)) ** 0.5
    if dist > distance_between_dots:
        angle = math.atan2(dy, dx)
        dx_new = speed_of_follow * math.cos(angle)
        dy_new = speed_of_follow * math.sin(angle)
        curr_dot.move(dx_new, dy_new)

    # Move towards target position
    target_x, target_y = target_pos.getX(), target_pos.getY()
    curr_x, curr_y = curr_dot.getCenter().getX(), curr_dot.getCenter().getY()
    dx, dy = target_x - curr_x, target_y - curr_y
    dist = ((dx ** 2) + (dy ** 2)) ** 0.5
    if dist > distance_between_dots:
        angle = math.atan2(dy, dx)
        dx_new = speed_of_follow * math.cos(angle)
        dy_new = speed_of_follow * math.sin(angle)
        curr_dot.move(dx_new, dy_new)

def move_dots(dots, target_pos):
    for i in range(1, len(dots)):
        prev_dot = dots[i - 1]
        curr_dot = dots[i]
        follow(prev_dot, curr_dot, target_pos)


def path_of_dots(win):
    dots = []
    dot = Circle(Point(50, 50), size+5)
    dot.setFill("black")
    dot.draw(win)
    dots.append(dot)
    for i in range(num_dots - 1):
        dot = Circle(Point(50 + (i + 1) * 30, 50), size)
        dot.setFill("black")
        dot.draw(win)
        dots.append(dot)

    while True:
        target_pos = win.getMouse()
        for repeat in range(3):
            for i in range(len(dots)):
                move_dots(dots[i:], target_pos)
                time.sleep(speed)


def main():
    win = GraphWin("Dot Trail", 900, 600)
    win.setBackground("gray")

    path_of_dots(win)

    win.getMouse()
    win.close()


main()