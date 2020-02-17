#battle ship
# This game is a mod on mineSweeper. The player has 5 clicks to click on a 3 mines i
# in order to win



#                           imports
from graphics import *
centerX = []
centerY = []

#                   global variables
window = GraphWin("Battleship royal", 300,300)
window.setCoords(0,0,100,120)
grids = [] # array to hold the various grid squares



#                    Function definitions
def drawInterface():

    #drawing the window

    #adding the grid for the markets
    for column in range(10):
        for row in range(10):
            rectangle = Rectangle(Point(0+(row*10),0+(column*10)),Point(10+(row*10),10+(column*10)))
            rectangle.draw(window)
            point = rectangle.getCenter()

            grids.append(rectangle) #registers each instance of grid in an array

            # remembers the cordinates of the grid centers for click and placement cordination
            centerY.append(point.getY())
            centerX.append(point.getX())


# This function changes the colours of the grid
def colourRec(rectangle, colour):
    rectangle.setFill(colour)

