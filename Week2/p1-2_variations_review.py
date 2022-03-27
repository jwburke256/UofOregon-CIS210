'''
p12_variations-W21

Author: Jacob Burke

Credits: N/A

Write some functions that manipulate integers, return a value, and practice
writing docstrings.
'''

def convert(i, j, k):
    '''
    (int, int, int) -> int

    Return an integer where i is the least significant digits (ones
    place), j is the tens place, and k is the hundreds place.

    >>>convert(1, 2, 3)
    321

    >>>convert(1, 0, 0)
    1

    >>>convert(0, 0, 1)
    100
    '''

    # this is a comment
    result = k*100 + j*10 + i
    return result
