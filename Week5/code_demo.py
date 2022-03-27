'''
CIS 210 Winter 2021 Code Demo

Author: Jacob Burke

Credits: N/A

Testing and debugging code, while doumenting.
'''

'''
An old-style movie theatre has a simple profit function. Each customer pays $5
per ticket. Each performance costs the theatre $20, plus .50 per attendee.
Write a function, profit, which returns the net profit per show, given the
number of attendees at the show. (Python Variations, from How to Design
Programs, Felleisen, et al.)
'''
import doctest

def profit(attendees):
    '''
    (int) -> float

    Returns net profit of running a show based on the argument of number of
    attendees

    >>> profit(10)
    25.0
    >>> profit(0)
    -20.0
    >>> profit(25)
    92.5
    '''
    performance = 20
    custm_cost = 5
    start_prof = attendees * custm_cost
    show_cost = performance + (attendees * 0.5)
    net_profit = start_prof - show_cost
    return net_profit

print(doctest.testmod())
