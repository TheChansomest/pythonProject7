from graphics import *


def main():
    print("Graphics 1 by Omar")
    win = GraphWin('Face', 400, 400) # give title and dimensions

    # The HEAD
    head = Circle(Point(40,100), 25) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    # the L EYE
    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    # the R EYE
    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    # the MOUTH
    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    # the DAH
    label = Text(Point(200, 200), 'One of a kind Py Face')
    label.setTextColor("green")
    label.setFace("courier")
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 300), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

def main2():
    print("in main 2 ")
    win = GraphWin("My Circle", 100, 100)
    c = Circle(Point(50,50), 10)
    c.draw(win)


    win.getMouse() # pause for click in window
    win.close()


main()
main2()
