''' 
CIS 210 Project 1-2 Python Variations

Author: Jacob Burke

Credits: N/A

Description
'''

def convert(i, j, k):
    '''
    (Integer) -> Integer

    Combines 3 integers together to make one integer. With each integer argument
    needing to be >=0 and <10. If the argument is not, an error message is
    printed. The combination has i being the least significant digit and k being
    the most.
    
    >>> convert(1, 2, 3)
    321
    >>> convert(0, 0, 1)
    100
    >>> convert(10, 0, 0)
    Error, must be an integer greater than or equal to 0, or less than 10
    '''
    if i<0 or i>9 or j<0 or j>9 or k<0 or k>9:
        print("Error, must be an integer greater than or equal to 0, or less than 10")
        return
    else:
        j = j *10
        k = k*100
        result = i + j + k
        return result

def add_digits(n):
    '''
    (3-digit-Integer) -> Integer

    Sums the digits of a 3-digit integer number. 
    
    >>> add_digits(789)
    24
    >>> add_digits(101)
    2
    >>> add_digits(456)
    15
    '''
    a = n // 100
    #print(str(a))
    b = (n-(a*100)) // 10
    #print(str(b))
    c = (n-(a*100)-(b*10))
    #print(str(c))
    result = a + b + c
    return result

def add_digits2(n):
    '''
    (Integer) -> Integer

    Sums the digits of a 3-digit integer number. 
    
    >>> add_digits2(789)
    24
    >>> add_digits2(12345)
    15
    >>> add_digits2(7531)
    16
    '''
    i = 0
    result = 0
    n_len = len(str(n))
    #print(str(n_len))
    x = 10 ** (n_len - 1)
    #print(str(x))
    n_copy = n
    while i < n_len:
        result = result + (n_copy // x)
        n_copy = n_copy - ((n_copy // x) * x)
        x = x / 10
        i += 1

    return int(result)

def profit(n):
    '''
    (Integer) -> Float

    Returns the net profit, based on the argument being the number of customers
    as an integer. 
    
    >>> profit(5)
    2.5
    >>> profit(10)
    25.0
    >>> profit(0)
    -20.0
    '''
    cost = 20 + (0.5 * n)
    ticket_profit = n * 5
    net_profit = ticket_profit - cost
    return net_profit
    
