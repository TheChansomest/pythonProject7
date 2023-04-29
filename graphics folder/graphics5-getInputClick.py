from graphics import *


def clickUp():
    col_arr=["violet","indigo","blue","green","yellow","orange","red"]
    win = GraphWin("Omar's Beard Simulation", 300, 300) # give title and dimensions
        
    message = Text(Point(win.getWidth()/2, 250), 'Click to Exit')
    message.draw(win)


    clickPoint = win.getMouse()
    y = clickPoint.getY()
    x = clickPoint.getX()

    print(x, y)

    win.getMouse()# get mouse to click on screen to exit
    win.close() # close the drawing window
    
def main():
    clickUp()


main()
                      
