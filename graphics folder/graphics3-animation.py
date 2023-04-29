from graphics import *

# draw a circle of radius
# 10 centered in a 100x100 window:
def main():
    win = GraphWin("My Circle", 500, 500)
    c = Circle(Point(50,50), 50)
    win.setBackground("red")
    c.draw(win)
 
    rec1 = Rectangle(Point(50,250), Point(60,100))
    rec1.setFill("Orange")
    rec1.draw(win)

    ball = Circle(Point(5,105), 5)
    ball.setFill("Black")
    ball.draw(win)
    x = 0
    while x < 300:
        ball.move(1,0)
        time.sleep(0.01) #in terms of millisecounds
        x = x + 1
    
    win.getMouse() # pause for click in window
    win.close()
main()
