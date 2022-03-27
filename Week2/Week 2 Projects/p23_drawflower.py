''' 
CIS 210 Project 2-3 Draw Flower

Author: Jacob Burke

Credits: N/A

Using turtle graphics, create a function to draw a polygon, then use that
function to draw a flower by calling the polygon function multiple times.
'''
from turtle import *

def drawPolygon(sideLength, numSides):
    '''
    (Integer, Integer) -> None

    Draws a polygon with turtle graphics with user arguments of side length and
    number of sides.
    '''
    turnAngle = 360 / numSides
    for i in range(numSides):
        forward(sideLength)
        right(turnAngle)
    return None
    
def drawFlower(numSquares):
    '''
    (Integer) -> None

    Draws a flower with turtle graphics, with the higher the argument, the more
    intricate the flower design.
    '''
    penup()
    sety(-200)
    seth(90)
    pendown()
    fd(200)
    seth(0)
    turnAngle = 360 / numSquares
    for i in range(numSquares):
        drawPolygon(25, 4)
        right(turnAngle)

    return None

def main():
    pencolor('purple')
    speed(10)
    drawFlower(25)
    return None

main()
