#battle ship
# This game is a mod on mineSweeper. The player has 5 clicks to click on a 3 mines i
# in order to win



#                           imports
from graphics import *

#                   global variables
window = GraphWin("Battleship royal", 300,300)
window.setCoords(0,0,100,120)
centerX = []
centerY = []




#                    Function definitions
def drawInterface():

    #drawing the window

    #adding the grid for the markets
    for column in range(10):
        for row in range(10):
            rectangle = Rectangle(Point(0+(row*10),0+(column*10)),Point(10+(row*10),10+(column*10)))
            rectangle.draw(window)
            point = rectangle.getCenter()
            centerX.append(point.getX())
            centerY.append(point.getY())
# =============================================================================
            x = point.getX()
            y = point.getY()
            Point(x,y).draw(window)
# =============================================================================

