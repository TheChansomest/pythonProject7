#
#Simple house
#
from graphics import *


def Main():
    # Create a window 400x400 pixels
    win = GraphWin('Shapes', 500, 500)

    # Make the window scaled
    # bottom leftmost corner is (0,0)
    # top rightmost corner is (10,10)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    # Draw base of house
    rect = Rectangle(Point(2, 2), Point(8, 5))
    rect.setFill("blue");
    rect.draw(win)

    # Draw door
    rect = Rectangle(Point(4, 2), Point(6, 4))
    rect.setFill("maroon");
    rect.draw(win)

    # Draw roof
    hat = Polygon(Point(2, 5), Point(5, 9), Point(8, 5))
    hat.setFill("navy")
    hat.draw(win)

    # Draw a window
    center = Point(5, 7)
    circ = Circle(center, 0.5)
    circ.setFill('yellow')
    circ.draw(win)

    # Wait until we click mouse in the window
    win.getMouse()

    win.close()


Main()