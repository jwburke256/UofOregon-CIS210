''' 
Prior programming experience quiz.
CIS 210 Project 1-1 Hello-Quiz Solution

Author: Jacob Burke

Credits: N/A

Add docstrings to Python functions that implement quiz 1 pseudocode.
(See p11_cricket.py for examples of functions with docstrings.)
'''

def q1(onTime, absent):
    '''
    (Boolean) -> String

    Returns string based on Boolean arguments input for both onTime and absent.
    Strings differ based on Boolean values for each parameter, based off of
    if the person was on time or absent, or niether.
    
    >>> q1(True, False)
    'Hello!'
    >>> q1(False, True)
    'Is anyone there?'
    >>> q1(False, False)
    'Better late than never.'
    '''
    if onTime:
        return('Hello!')
    elif absent:
        return('Is anyone there?')
    else:
        return('Better late than never.')

def q2(age, salary):
    '''
    (Integer, Integer) -> Boolean

    Returns Boolean based off of integer arguments input. Both age has to be
    younger than 18 and salary less than 10000 for Boolean to be True. If not
    then False.

    >>> q2(18, 8000)
    False
    >>> q2(20, 12000)
    False
    >>> q2(17, 800)
    True
    '''
    return (age < 18) and (salary < 10000)

def q3():
    '''
    (None) -> Integer

    Returns an Integer of either 5 or 6, based off of the local variable values
    of p and q.
    
    >>> q3()
    6
    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

def q4(balance, deposit):
    '''
    (Integer, Integer) -> Integer

    Returns final deposit balance based on the original balance and the deposit
    argument being added to the balance 10 times, through the use of a while
    loop.

    >>> q4(10, 5)
    60
    >>> q4(100, 50)
    600
    >>> q4(600, 300)
    3600
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

def q5(nums):
    '''
    docstring -
    (list of numbers) -> Integer       #fill in the rest of the type contract
 
    Returns an Intger based on the function looping through each item in the
    list. If the item is greater than or equal to 0, it adds one to the counter
    variable that is result. If not the while loop moves on to the next object.
    Once all items in the list have been checked, the function returns the
    integer.
    

    >>> q5([0, 1, 2, 3, 4, 5])    #examples are given
    6
    >>> q5([0, -1, 2, -3, 4, -5])
    3
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

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








    
    
     
        
    
