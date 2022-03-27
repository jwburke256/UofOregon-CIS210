from math import sqrt

def myDist(x, y):
    '''
    (Num, Num) -> Float

    Returns the distance of a point from the origin (0, 0) using the Euclidean
    distance formula

    >>> myDist(1, 1)
    1.4142135623730951
    >>> myDist(-1, -1)
    1.4142135623730951
    >>> myDist(0,0)
    0.0
    '''
    dist = sqrt((x - 0)**2 + (y - 0)**2) #Euclidean Formula
    return dist

def isIn(x, y, r):
    '''
    (Num, Num, Num) -> None

    Returns None but has the side effect of printing if the two given points
    x and y are found within a circle given the radius r.

    >>> isIn(3, 3, 5)
    Point in Circle
    >>> isIn(3, 3, 1)
    Point not in Cirlce
    >>> isIn(1, 1, 2)
    Point in Circle
    '''
    #Use operational operators to determine if point is in circle with radius r
    if myDist(x, y) > r:
        print("Point not in Cirlce")
    else:
        print("Point in Circle")
    return None
