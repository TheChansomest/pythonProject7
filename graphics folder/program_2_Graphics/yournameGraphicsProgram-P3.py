
#Lines of circles with different color

from graphics import *


def Main():
    # Create a window 500x500 pixels
    win = GraphWin('Circles', 500, 500)

    # Make the window scaled
    # bottom leftmost corner is (0,0)
    # top rightmost corner is (10,10)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    for i in range(10):
        # Draw a circle centered at 5,5
        circ = Circle(Point(i, i), .5)
        circ.setFill(color_rgb(255, i * 10, i * 20))
        circ.draw(win)
    for i in range(10):
        # Draw a circle centered at 5,5
        circ2 = Circle(Point(10-i, i), .5)
        circ2.setFill(color_rgb(255, i * 10, i * 20))
        circ2.draw(win)
    for i in range(10):
        # Draw a circle centered at 5,5
        circ3 = Circle(Point(5, i), .5)
        circ3.setFill(color_rgb(0, 255, i * 20))
        circ3.draw(win)
    for i in range(10):
        # Draw a circle centered at 5,5
        circ3 = Circle(Point(i, 5), .5)
        circ3.setFill(color_rgb(0, 255, i * 20))
        circ3.draw(win)
    # Draw quit message
    message = Text(Point(5, 0.5), "Click anywhere to quit")
    message.draw(win)

    # Wait until we click mouse in the window
    win.getMouse()

    win.close()


Main()