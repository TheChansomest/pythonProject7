from graphics import *



def main():
    win = GraphWin("My Circle", 500, 500)
    win.setBackground("red")

    ball = Circle(Point(5, 105), 5)
    ball.setFill("Black")
    ball.draw(win)

    ball2 = Circle(Point(5, 305), 5)
    ball2.setFill("Black")
    ball2.draw(win)
    x = 0
    while x < 200:
        ball.move(1, 1)
        ball2.move(1,-1)
        time.sleep(0.01)  # in terms of millisecounds
        x = x + 1
    t=0.05
    while x < 300:
        ball.move(1, -1)
        ball2.move(1, 1)
        time.sleep(t-0.01)  # in terms of millisecounds
        x = x + 1

    win.getMouse()  # pause for click in window
    win.close()

main()
