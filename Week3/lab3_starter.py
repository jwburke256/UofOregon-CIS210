# Pizza calculator example code

import math
import doctest


def pizza_calculator(diameter, cost):
    '''
    (int, num) -> float

    Calculates and returns the cost per square inch
    of pizza for a pizza of given diameter and cost.

    Examples:
    >>> pizza_calculator(14, 18)
    0.117
    >>> pizza_calculator(14, 20.25) 
    0.132
    '''
    r = diameter / 2
    area = circle_area(r)
#    area = math.pi * r**2
    cost_per_inch = cost / area
    cost_per_inch = round(cost_per_inch, 3)
    return cost_per_inch

def main():
    '''
    Compare multiple pizza values.
    '''
    print("Pizza 1: ", pizza_calculator(14, 18))
    print("Pizza 2: ", pizza_calculator(14, 20.25))
    print("Pizza 3: ", pizza_calculator(20, 27))

    return None

def circle_area(radius):
    '''
    (num) -> num
    Returns the area of a circle when given its diameter.

    >>> circle_area(14)
    615.7521601035994
    '''
    area = math.pi * radius ** 2
    return area



main() # <-- to actually run the program!

print(doctest.testmod())



