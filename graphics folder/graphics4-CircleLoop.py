from graphics import *
import time

def drawCicrcles():
    col_arr=["violet","indigo","blue","green","yellow","orange","red"]
    workArea = GraphWin("Omar's Beard Simulation", 300, 300) # give title and dimensions

   # myImage = Image(Point(300,300), "images/omar-face-and-hat.gif")
    myImage.draw(workArea)
    
    x=workArea.getWidth()/2 # get x of middle of drawing area
    y=workArea.getHeight()/2 # get y of middle of drawing area

    i=0
    while i<len(col_arr):
        cir=Circle(Point(x, (y+i*10)), 10+10*i)    # draw circle with center at middle of drawing area
        cir.setOutline(col_arr[i])          # get a next outline color from color array
        cir.setWidth(4)                     # set outline width
        cir.draw(workArea)                  # draw the current circle
        time.sleep(0.05)
        i+=1                                # increment counter for iteration
        
    message = Text(Point(workArea.getWidth()/2, 250), 'Click to Exit')
    message.draw(workArea)


    workArea.getMouse()# get mouse to click on screen to exit
    workArea.close() # close the drawing window
    
def main():
    drawCicrcles()


main()
                      
