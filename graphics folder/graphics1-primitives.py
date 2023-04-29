from graphics import *

def main():
    win = GraphWin("CSCE160 - Spring 2023", 500, 500)
    win.setBackground(color_rgb(0,0,0))

    #Circle
    #pt = Point(250, 250) #don't really need
    cir = Circle(Point(250, 250), 50) # get used to using this method
    cir.setFill(color_rgb(100, 255, 50)) # default color is back if you get rid if "fill"
    cir.draw(win) # actually draws the circle

    cir2 = Circle(Point(100, 250), 60)
    cir2.setOutline(color_rgb(0, 255, 255))
    cir2.setFill(color_rgb(255, 100, 50))
    cir2.setWidth(5)
    cir2.draw(win)
    
    #Rectangle
    rect = Rectangle(Point(450, 250), Point(350, 350))
    rect.setOutline("red")
    rect.setFill(color_rgb(255, 100, 50))
    rect.draw(win)

    #Polygon
    poly = Polygon(Point(40, 40),
                   Point(100, 100),
                   Point(40, 100)
                   )
    poly.setFill(color_rgb(255, 0, 255))
    poly.setOutline(color_rgb(0, 255, 0))
    poly.setWidth(5)
    poly.draw(win)

    ln = Line(Point(250, 250), Point(250, 350))
    ln.setOutline(color_rgb(0, 255, 255))
    ln.draw(win)

    #Text
    txt = Text(Point(250, 50), "What's up?") # the location is the center of the text
    txt.setTextColor(color_rgb(0, 255, 200))
    txt.setSize(30)
    txt.setFace('courier')
    txt.draw(win)

    #InputText
    input_box = Entry(Point(250, 250), 10)
    input_box.draw(win)
    
    txt = Text(Point(250, 280), "")
    txt.draw(win)

    #img = Image(Point(250, 250), "images/omar-face-and-hat.gif") #added hashtag
    #img.draw(win)

    while True:
        txt.setText(input_box.getText())

        
    win.getMouse()
    win.close()

main()
                      
