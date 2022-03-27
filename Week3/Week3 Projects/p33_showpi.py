''' 
CIS 210 Project 3-3 Show Monte Pi

Author: Jacob Burke

Credits: CIS210 p33_showpi_starter file

Create functions that visualize the montePi function using turtle graphics.
'''

from turtle import *
import math
import random

def isInCircle(x, y, r):
    '''
    (Number, Number, Number) -> Boolean

    Returns a boolean based on if the given point falls inside a quarter circle
    with a radius of r.
    
    >>> isInCircle(0, 0, 1)
    True
    >>> isInCircle(.5, .5, 1)
    True
    >>> isInCircle(1, 2, 1)
    False
    '''
    distance = math.sqrt(x**2 + y**2)

    if distance <= r:
        return True
    else:
        return False

def reportPi(numDarts, approxPi):
    '''
    (Integer, Float) -> None

    Compares the montePi functions result to the math libraries pi function,
    and prints the results. Returns None when complete.

    >>> reportPi(1000, mypi)
    With 1000 iterations:
    my approximate value for pi is: 3.148
    math lib pi value is: 3.141592653589793
    >>> reportPi(1000, mypi)
    With 1000 iterations:
    my approximate value for pi is: 3.08
    math lib pi value is: 3.141592653589793
    This is a 1.96 percent error.
    '''
    compare = round(abs((((math.pi - approxPi) / math.pi) *100)), 2)
    print("With " + str(numDarts) + " iterations:")
    print("my approximate value for pi is: " + str(approxPi))
    print("math lib pi value is: " + str(math.pi))
    print("This is a " + str(compare) + " percent error.")
    
def drawBoard():
    '''
    () -> None

    Draws the dartboard using turtle module in support of the showMontePi
    function.
    '''

    wn = Screen()
    wn.setworldcoordinates(-2, -2, 2, 2)

    speed(0); hideturtle()
    penup()

    goto(-1, 0)
    pendown()
    goto(1, 0)
    penup()
    goto(0, 1)
    pendown()
    goto(0, -1)
    penup()
    goto(0, -1)

    return None
    
def showMontePi(numDarts):
    '''
    (Integer) -> Float

    Uses the drawBoard function to draw a dartboard, then draws colored dots to
    visualize the monte carlo python alogithm. Returns the approximation for
    pi.
    '''
    # set up canvas and turtle
    # to animate the algorithm;
    # draw x, y axes
    # DRAWBOARD FUNCTION
    drawBoard()

    # pen should stay up for drawing darts
 
    inCircle = 0

    # throw the darts and check whether
    # they landed on the dart board and
    # keep count of those that do
    for i in range(numDarts):
        x = random.random()
        y = random.random()

    # CALLS ISINCIRCLE FUNCTION.
        goto(x,y)
        if isInCircle(x, y, 1) == True:
            inCircle += 1
            color("blue")
        else:
            color("red")

        dot()

    # calculate approximate pi
    approxPi = inCircle/numDarts * 4

    #wn.exitonclick()

    return approxPi

def main():
    '''
    () -> None

    Runs an example of the showMontePi and reportPi functions.
    '''
    k = 1000
    mypi = showMontePi(k)
    reportPi(k, mypi)
    return None
    
main()
