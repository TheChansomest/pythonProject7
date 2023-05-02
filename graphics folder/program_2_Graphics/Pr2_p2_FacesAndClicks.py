#
# nfaces.py: Draw mutliple faces at selected position.
# by: Susan Computewell
#
from graphics import *


# Draw a face at coordinates x,y in win
def face(win, x, y):
    # Draw a circle centered at 5,5
    center = Point(5 + x, 5 + y)
    circ = Circle(center, 4)
    circ.setFill('yellow')
    circ.draw(win)

    # Draw left eye
    eye1 = Circle(Point(3 + x, 6 + y), 1)
    eye1.setFill("red")
    eye1.draw(win)

    # Draw right eye
    eye2 = Circle(Point(7 + x, 6 + y), 1)
    eye2.setFill("red")
    eye2.draw(win)

    # Draw mouth
    rect = Rectangle(Point(4 + x, 2 + y), Point(6 + x, 3 + y))
    rect.setFill("blue");
    rect.draw(win)

    # Draw hat
    hat = Polygon(Point(1 + x, 8 + y), Point(5 + x, 10 + y), Point(9 + x, 8 + y))
    hat.setFill("orange")
    hat.draw(win)


def main():
    win = GraphWin("Faces", 500, 500)
    win.setCoords(0.0, 0.0, 100.0, 100.0)
    message = Text(Point(20, 10), "Click n times")
    message.draw(win)

    for t in range(10):
        # Get mouse and draw a face in this position
        p1 = win.getMouse()
        face(win, p1.x, p1.y)

        # Wait for click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()


main()
