#this is the logical engine for the game
from visuals import *

userClick = [] # array to hold the user click positions
#This function runs the game loop
def main():
    while True:
        click = window.getMouse()
        onClick(click)
# this function determines which box was clicked
def onClick(cordinates):
    x = cordinates.getX()
    y = cordinates.getY()
    getcenterX(x)
    getcenterY(y)

# This function determines the x value of the center of the rectangle clicked
def getcenterX(clickX):
    for center in centerX:
        if clickX-center <5:
            return center

#This function determines the x value of the center of the rectangle clicked

def getcenterY(clickY):
    for center in centerY:
        if clickY-center <5:
            return center

#running the game
drawInterface()
main()
