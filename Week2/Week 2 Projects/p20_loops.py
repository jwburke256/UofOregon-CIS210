''' 
CIS 210 Project 2-0 Learning Looping

Author: Jacob Burke

Credits: N/A

Adjust previous python code from for loops to while loops and vice versa.
'''

def q6():
    '''
    (None) -> Integer

    Returns an the Integer, based off of the local variables i and p's staring
    values.

    >>> q6()
    16
    '''
    i = 0
    p = 1
    while i < 4:
        # i = 1
        p = p * 2
        i += 1

    return p

def q6_better():
    '''
    (None) -> Integer

    Returns an the Integer, based off of the local variables i and p's staring
    values.

    >>> q6_better()
    16
    '''
    p = 1
    for i in range(4):
        p = p * 2
        
    return p

def q6_final(n, m):
    '''
    (Integer, Integer) -> Integer

    Returns the result of n raised to the power of m.
    
    >>> q6_final(2, 2)
    4
    >>> q6_final(3, 9)
    19683
    >>> q6_final(5, 5)
    3125
    '''
    p = 1
    for i in range(m):
        p = p * n

    return p
    
def add_digits2a(n):
    '''(int) --> int

    Return sum of digits of n, a positive 3-digit integer.
    Implement using a while loop.

    >>> add_digits2a(789)
    24
    >>> add_digits2a(101)
    2
    >>> add_digits2a(000)
    0
    '''
    digit_sum = 0
    ctr = 1
    while ctr < 4:
        digit = n % 10
        n = n // 10
        digit_sum += digit
        ctr += 1

    return digit_sum

def add_digits2a_better(n):
    '''
    (int) --> int

    Return sum of digits of n, a positive 3-digit integer.
    Implement using a while loop.

    >>> add_digits2a(789)
    24
    >>> add_digits2a(101)
    2
    >>> add_digits2a(000)
    0
    '''
    digit_sum = 0
    for i in range(3):
        digit = n % 10
        n = n // 10
        digit_sum += digit

    return digit_sum
    
def add_digits2b(n):
    '''(int) --> int

    Return sum of digits of n, where n is a
    positive integer of any length.

    >>> add_digits2b(789)
    24
    >>> add_digits2b(101)
    2
    >>> add_digits2b(000)
    0
    >>> add_digits2b(5)
    5
    >>> add_digits2b(10101)
    3
    '''
    digit_sum = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        digit_sum += digit

    return digit_sum

def add_digits2b_better(n):
#This is not a good approach, as with the start of the loop the initial value
#for n is the argument value. Within the loop itself n changes, but it does not
#change the value for n in the range function. So eventually within the loop n
#becomes 0, but the loop continues to run until when the range function is set
#to stop
    '''(int) --> int

    Return sum of digits of n, where n is a
    positive integer of any length.

    >>> add_digits2b_better(789)
    24
    >>> add_digits2b_better(101)
    2
    >>> add_digits2b_better(000)
    0
    >>> add_digits2b_better(5)
    5
    >>> add_digits2b_better(10101)
    3
    '''
    digit_sum = 0
    for i in range(n):
        digit = n % 10
        n = n // 10
        digit_sum += digit

    return digit_sum


