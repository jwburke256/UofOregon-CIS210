''' 
CIS 210 Project 3-2 Monte Pi (Approximating pi)

Author: Jacob Burke

Credits: N/A

Create functions that calculate pi using the monte carlo method, and compare the
results of that function withe the built in math library pi function.
'''
import math
from math import *
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
    distance = sqrt(x**2 + y**2)

    if distance <= r:
        return True
    else:
        return False
    
def montePi(numDarts):
    '''
    (Integer) -> Float

    Returns an approximate number of pi using a monte carlo simluation when
    given numDarts. The higher the number, the closer the approximation.

    >>> montePi(100)
    3.4
    >>> montePi(10000)
    3.1328
    >>> montePi(100000)
    3.1462
    >>> 
    '''
    inCircle = 0
    
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        
        if isInCircle(x, y, 1) == True:
            inCircle += 1

    pi = inCircle / numDarts * 4
    return pi

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
    compare = round(abs((((pi - approxPi) / pi) *100)), 2)
    print("With " + str(numDarts) + " iterations:")
    print("my approximate value for pi is: " + str(approxPi))
    print("math lib pi value is: " + str(pi))
    print("This is a " + str(compare) + " percent error.")
    return None

def main():
    '''
    () -> None

    Runs examples of the montePi and reportPi functions.
    '''
    k = 100
    mypi = montePi(k)
    reportPi(k, mypi)

    m = 100000
    mypi = montePi(m)
    reportPi(m, mypi)

    n = 10000000
    mypi = montePi(n)
    reportPi(n, mypi)

main()
