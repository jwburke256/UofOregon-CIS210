''' 
CIS 210 Project 2-1 Determining Net Pay

Author: Jacob Burke

Credits: N/A

Create functions to calculate tax and net income when given hours worked.
'''

def tax(gross):
    '''
    (Integer) -> Float

    Returns the amount of the tax given the gross pay.

    >>> tax(3000)
    450.0
    >>> tax(500)
    75.0
    >>> tax(2250)
    337.5
    >>> 
    '''
    tax = gross * 0.15
    return tax

def netpay(hours):
    '''
    (Float) -> Float(rounded to two decimal places)

    Returns the net pay of an employee given the number of hours worked.

    >>> netpay(40)
    382.5
    >>> netpay(1)
    9.5625
    >>> netpay(15.5)
    148.22
    '''
    gross = 11.25 * hours
    t = tax(gross)
    netpay = gross - t
    return round(netpay, 2)

def main():
    '''Net pay program driver.'''
    print('For 1 hours work, netpay is: ', netpay(1))
    print('For 40 hours work, netpay is: ', netpay(40))
    return None

main()
