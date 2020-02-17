#this is the logical engine for the game
from visuals import *

userClick = [] # array to hold the user click positions
minePositions = [] # array to hold the positions of the mines


#This function runs the game loop
def main():
    drawInterface()

    while True:
        click = window.getMouse()
        onClick(click)

#This function generates random positions for the cake mines
# =============================================================================
# def placeMines():
#
#
# =============================================================================
# this function determines which box was clicked
def onClick(cordinates):
    x = cordinates.getX()
    y = cordinates.getY()
    x = getcenterX(x)
    y = getcenterY(y)

    #Determines which grid was clicked
    colourRec(whichGrid(x,y))

#Determines which grid was clicked
def whichGrid(x,y):
    for i in grids:
        if i.getCenter().getX() == x and i.getCenter().getY() == y:
            return i

# This function determines the x value of the center of the rectangle clicked
def getcenterX(clickX):
    for center in centerX:
        if clickX-center <5:
            return center


#This function determines the y value of the center of the rectangle clicked
def getcenterY(clickY):
    for center in centerY:
        if clickY-center <5:
            return center

# This function checks if the clicked on square already contains a mine
def findMine(rectangle):
    if rectangle==2:
        something =3

#



#running the game
main()


'''
if click poisition isn't in user clicks
    check mines and change colour




'''