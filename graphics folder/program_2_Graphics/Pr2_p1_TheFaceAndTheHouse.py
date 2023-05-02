#
# face.py - Simple face
#
from graphics import *


def Main():
    # Create a window 400x400 pixels
    win = GraphWin('Shapes', 500, 500)

    # Make the window scaled
    # bottom leftmost corner is (0,0)
    # top rightmost corner is (10,10)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    # Draw a circle centered at 5,5
    center = Point(5, 5)
    circ = Circle(center, 4)
    circ.setFill('yellow')
    circ.draw(win)

    # Draw left eye
    eye1 = Circle(Point(3, 6), 1)
    eye1.setFill("red")
    eye1.draw(win)

    # Draw right eye
    eye2 = Circle(Point(7, 6), 1)
    eye2.setFill("red")
    eye2.draw(win)

    # Draw mouth
    rect = Rectangle(Point(4, 2), Point(6, 3))
    rect.setFill("blue");
    rect.draw(win)

    # Draw hat
    hat = Polygon(Point(1, 8), Point(5, 10), Point(9, 8))
    hat.setFill("orange")
    hat.draw(win)

    # Draw message
    message = Text(Point(5, 0.5), "Click anywhere to quit")
    message.draw(win)

    # Wait until we click mouse in the window
    win.getMouse()

    win.close()


Main()
