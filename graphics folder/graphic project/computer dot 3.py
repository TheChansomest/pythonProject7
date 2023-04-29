from graphics import *
import time
import math

num_dots = 80
distance_between_dots = 25
size = 5
speed_of_follow = 1.5
speed = 0.001

def follow(prev_dot, curr_dot):
    dx = prev_dot.getCenter().getX() - curr_dot.getCenter().getX()
    dy = prev_dot.getCenter().getY() - curr_dot.getCenter().getY()
    dist = ((dx ** 2) + (dy ** 2)) ** 0.5
    if dist > distance_between_dots:
        angle = math.atan2(dy, dx)
        dx_new = speed_of_follow * math.cos(angle)
        dy_new = speed_of_follow * math.sin(angle)
        curr_dot.move(dx_new, dy_new)


def move_dots(dots):
    for i in range(1, len(dots)):
        prev_dot = dots[i - 1]
        curr_dot = dots[i]
        follow(prev_dot, curr_dot)


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

    moves = [
        (0, 2),  # move down
        (2, 0),  # move right
        (0, -2), # move up
        (-2, 0)  # move left
    ]
    times = [200, 200, 200, 200] # time values for each move

    for repeat in range(5): # repeat the pattern 5 times
        for i, move in enumerate(moves):
            x = 0
            while x < times[i]:
                dots[0].move(move[0], move[1])
                move_dots(dots)
                time.sleep(speed)
                x += 1

def main():
    win = GraphWin("Dot Trail", 500, 500)
    win.setBackground("gray")

    path_of_dots(win)

    win.getMouse()
    win.close()


main()