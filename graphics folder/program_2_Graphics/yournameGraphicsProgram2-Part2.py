
# Draw multiple houses at selected position.
from graphics import *


# Draw a face at coordinates x,y in win
def face(win, x, y):

    # Draw base of house
    rect = Rectangle(Point(2 + x, 2 + y), Point(8 + x, 5 + y))
    rect.setFill("blue");
    rect.draw(win)

    # Draw door
    rect = Rectangle(Point(4 + x, 2 + y), Point(6 + x, 4 + y))
    rect.setFill("maroon");
    rect.draw(win)

    # Draw roof
    hat = Polygon(Point(2 + x, 5 + y), Point(5 + x, 9 + y), Point(8 + x, 5 + y))
    hat.setFill("navy")
    hat.draw(win)

    # Draw a window
    center = Point(5 + x, 7 + y)
    circ = Circle(center, 0.5)
    circ.setFill('yellow')
    circ.draw(win)


def main():
    win = GraphWin("Houses", 500, 500)
    win.setCoords(0.0, 0.0, 100.0, 100.0)

    while True:
        try:
            num = int(input("Please enter a positive integer greater than 1: "))
            if num <= 1:
                raise ValueError("Input must be positive and greater than 1")
            break
        except ValueError as e:
            print(e)
    message = Text(Point(20, 10), "Click " + str(num) + " times")
    message.draw(win)

    while num > 0:
        p1 = win.getMouse()
        num -= 1
        message.setText("Click " + str(num) + " more times")

        face(win, p1.x, p1.y)

    message.setText("You clicked " + str(num) + " times. Click to close.")

    for t in range(num):
        # Get mouse and draw a face in this position
        p1 = win.getMouse()
        face(win, p1.x, p1.y)

        # Wait for click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()


main()