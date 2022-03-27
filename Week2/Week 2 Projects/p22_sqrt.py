''' 
CIS 210 Project 2-2 Approximate Square Root

Author: Jacob Burke

Credits: N/A

Create a function to square a number based off the babylonian method, then
compare the results to the math module square root function.
'''
import math
from math import *

def mysqrt(n, k):
    '''
    (Integer, Integer) -> Float

    Returns the approximate square root of n using the babylonian method, with
    k being the amount the method loops.

    >>> mysqrt(5, 5)
    2.236067977499978
    >>> mysqrt(10, 10)
    3.162277660168379
    >>> mysqrt(3, 20)
    1.7320508075688772
    '''
    x = 1
    #Babylonian Method
    for i in range(k):
        x = 0.5*(x + n/x)
    return x

def sqrt_compare(num, iterations):
    '''
    (Integer, Integer) -> None

    Prints the difference between the mysqrt and math lib sqrt functions as a
    percentage error.

    >>> sqrt_compare(10000, 8)
    For 10000 using 8 iterations:
    mysqrt value is: 101.20218365353946
    math lib sqrt value is: 100.0
    This is a 1.2 percent error
    >>> sqrt_compare(1111, 6)
    For 1111 using 6 iterations:
    mysqrt value is: 34.7939639349116
    math lib sqrt value is: 33.331666624997915
    This is a 4.39 percent error
    >>> sqrt_compare(799, 10)
    For 799 using 10 iterations:
    mysqrt value is: 28.26658805020514
    math lib sqrt value is: 28.26658805020514
    This is a 0.0 percent error
    '''
    mysqrt_result = mysqrt(num, iterations)
    sqrt_result = sqrt(num)
    compare = round(abs((((sqrt_result - mysqrt_result) / sqrt_result) *100)), 2)
    print('For ' + str(num) + ' using ' + str(iterations) + ' iterations:')
    print('mysqrt value is: ' + str(mysqrt_result))
    print('math lib sqrt value is: ' + str(sqrt_result))
    print('This is a ' + str(compare) + ' percent error')
    return None

def main():
    '''Square root comparison program driver.'''
    sqrt_compare(25, 5)
    sqrt_compare(25, 10)
    sqrt_compare(625, 5)
    sqrt_compare(625, 10)
    sqrt_compare(10000, 8)
    sqrt_compare(10000, 10)
    sqrt_compare(10000, 11)
    return None

main()
