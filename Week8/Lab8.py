'''
CIS 210 Week 8 Lab Winter 2021

Author: Jacob B.

Credits: N/A

Exercises for assert and try/except.
'''

import doctest

def foo():
    '''
    (int, int) -> int

    Returns the integer quptient of x and y.
    '''

    '''
    if(y==0):
        print(f'Sorry homie, cannot do that')
        return 0
    '''

    x = int(input('Enter an integer between 1 and 10, inclusive: '))
    y = int(input('Enter an integer between 1 and 10, inclusive: '))

    assert 1 <=x and x <= 10 and 1 <=1 and y <=10
    
    print(f'You entered {x} and {y}. Thanks for following instrucstion.')
    
    return

def catch_them_all():
    '''
    '''

    try:
        x = 1 / 0
        y = 1 / 'hello world'
    except TypeError:
        print('found a type error')
    except ZeroDivisionError:
        print('found a zero division error')
    return

def incr_li(li, n):
    '''
    (list of ints, int) -> None

    Increment the first n values
    in a list by 1 and print the new list.
    '''
    '''
    >>> incr_li([1, 2, 3, 4], 2)
    [2, 3, 3, 4]
    >>> incr_li([1, 2, 3, 4], 5)
    [2, 3, 4, 5]
    '''
    newli = li[:] # slicing the entire list creates a copy
    for i in range(n):
        newli[i] += 1
    print(newli)

    try:
        x = [1, 2, 3, 4]
        y = 5
        incr_li(x, y)
    except IndexError:
        print('IndexError')
    
    return None

def find_file(fname):
    '''
    (file) -> None
    '''
    try:
        open(fname, 'r')
        fname.close()
    except FileNotFoundError:
        print('Where is ' + fname + '?')
        return None
    open(fname, 'r')
    
def key_error(key):
    dict = {1:'a', 2:'b', 3:'c'}
    try:
        print(dict[key])
    except KeyError:
        print(str(key) + ' is not a key')
        return None
    #print(dict[key])
    
print(doctest.testmod())
