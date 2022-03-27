# DOCTEST EXAMPLE

import doctest #<-- check it out!

#Recall project 2-1:

def tax(gross_pay):
    '''
    float -> float

    Return tax on gross_pay.

    >>> tax(100)
    15.0
    >>> tax(5)
    0.75
    '''
    TAX_RATE = .15
    return gross_pay * TAX_RATE

def netpay(hours):
    '''
    float -> float

    Return net pay (after taxes) based on hours worked.

    >>> netpay(1)
    9.56
    >>> netpay(40)
    382.5
    '''
    RATE = 11.25
    pay = hours * RATE      
    tax_amt = tax(pay)      
    net = pay - tax_amt     
    net = round(net, 2)
    return net

print(doctest.testmod())

'''
things to NOTICE!!!!

1) The syntax for an example in the docstring is:
>>> myfunction(specific arguments)
expected output

*Note that this includes a SPACE after the >>> *

2) testmod() RETURNS its value, which is a tuple of (failed=#, attempted=#)
    It also PRINTS a report of any failures
    (but it prints nothing if it was all successful).

3) introduce an error in either the code or an example of use (e.g., round to 3
rather than 2 digits).  re-run module to see doctest.testmod error report.

4) doctest.testmod is "brittle", meaning it's very sensitive to syntax and output format.
(the opposite of "robust")

5) doctest.testmod will not work for functions that draw pictures, include random number
generation, user input, for example (do you see why?)

'''

