#this is the logical engine for the game
from visuals import *
from random import randint

userClick = [] # array to hold the user click positions
minePositions = [] # array to hold the positions of the mines


# this function determines which box was clicked
def onClick(cordinates):
    x = cordinates.getX()
    y = cordinates.getY()
    x = getcenterX(x)
    y = getcenterY(y)

    #Determines which grid was clicked
    rectangle = whichGrid(x,y)
    if rectangle not in userClick:
        colourRec(rectangle,findMine(rectangle))
        userClick.append(rectangle)

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
    if rectangle in minePositions:
        return "green"
    else:
        return "red"


# This function places the mines in the grids
def placeMine():
    for i in range(10):
        print(len(grids))
        place = randint(0,len(grids))

        #record the mine position
        minePositions.append(whichGrid(centerX[place],centerY[place]))
    print(minePositions)

# This function runs the game loop
def main():
    drawInterface()
    placeMine()


    #WARNING this should be last in the function
    while True:
        click = window.getMouse()
        onClick(click)
    #place the mines in the game

#running the game
main()


'''
if click poisition isn't in user clicks
    check mines and change colour




'''