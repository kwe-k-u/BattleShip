#battle ship
# This game is a mod on mineSweeper. The player has 5 clicks to click on a 3 mines i
# in order to win



# imports
from graphics import *

def drawInterface():

    #drawing the window
    window = GraphWin("something", 300,300)
    window.setCoords(0,0,100,100)

    #adding the grid for the markets
    for column in range(10):
        for row in range(10):
            Rectangle(Point(0+(row*10),0+(column*10)),Point(20+(row*10),20+(column*10))).draw(window)
