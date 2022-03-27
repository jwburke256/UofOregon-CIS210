'''
More Automated Testing and Debugging
CIS 210 Project 6-2 Winter 2021

Author: Jacob Burke

Credits: N/A

Functions need to be tested and debugged;
write a function to automate testing of calendar function (project 5-1)
'''
import doctest
from p51_calendar_key_W21 import calendar

def bigSalesBug(sales_list):
    '''(list) -> number

    Returns sum of all sales for amounts at or over $40,000.
    sales_list has the record of all the sales.

    >>> bigSalesBug([40000, 45.67, 19000.0, 25000, 100000])
    140000.0
    >>> bigSalesBug([40000, 40000, 40000])
    120000.0
    >>> bigSalesBug([45.67, 19000.0, 25000])
    0.0
    >>> bigSalesBug([])
    0.0

    First test case is checking for only 40000 values
    Second test case is checking for no values above 40000
    Third test case is checking for an empty list
    '''
    
    # Fixed test case by removing _
    total = 0.00
    for sales in sales_list:
        if sales >= 40000: #changed sign from > to >=, changed 40_000 to 40000
            total = total + sales #fixed total as it was spelled tottal
    return total #fixed indentation

############

def findRangeBug(salesli):
    '''(list) -> tuple

    Returns largest and smallest number in non-empty salesli.
    (Note that Python has built in funcs max and min
    to do this, but not using them here, so we can
    work with the list directly.)

    >>> findRangeBug([40000, 45.67, 19000.0, 25000, 100000])
    (45.67, 100000.0)
    >>> findRangeBug([1, 1])
    (1.0, 1.0)
    >>> findRangeBug([0])
    (0.0, 0.0)
    >>> findRangeBug([])
    Traceback (most recent call last):
      File "<pyshell#48>", line 1, in <module>
        findRangeBug([])
      File "C:/Users/Jacob/Documents/University of Oregon Winter 2021/CIS 210/Week6/Projects/p62_fixed.py", line 45, in findRangeBug
        low = float(salescopy[0])
    IndexError: list index out of range

    First test case checks for a range of only 1 value
    Second test case check for a list with only 1 value being 0
    Third test case shows that the function does not work with an empty list
    '''
    salescopy = sorted(salesli) #Copy of sorted list
    low = float(salescopy[0])
    high = float(salescopy[-1])
    return low, high

def salesReportBug(salesli):
    '''(list) --> None

    Prints report of sales totals for each day of week (salesli)
    and range of per-day sales. salesli is non-empty - 0 sales
    for any day are reported as 0.

    >>> salesReportBug([40000, 45.67, 19000.0, 25000, 100000])
    Weekly Range: $45.67 - $100,000.00
    <BLANKLINE>
    Mon          Tue          Wed          Thu          Fri         
    $40,000.00   $45.67       $19,000.00   $25,000.00   $100,000.00  
    >>> salesReportBug([40000, 45.67, 19000.0])
    Weekly Range: $45.67 - $40,000.00
    <BLANKLINE>
    Mon          Tue          Wed          Thu          Fri         
    $40,000.00   $45.67       $19,000.00   
    >>> salesReportBug([0])
    Weekly Range: $0.00 - $0.00
    <BLANKLINE>
    Mon          Tue          Wed          Thu          Fri         
    $0.00        
    >>> salesReportBug([])
    Traceback (most recent call last):
      File "<pyshell#52>", line 1, in <module>
        salesReportBug([])
      File "C:/Users/Jacob/Documents/University of Oregon Winter 2021/CIS 210/Week6/Projects/p62_fixed.py", line 85, in salesReportBug
        low, high = findRangeBug(salesli)
      File "C:/Users/Jacob/Documents/University of Oregon Winter 2021/CIS 210/Week6/Projects/p62_fixed.py", line 67, in findRangeBug
        low = float(salescopy[0])
    IndexError: list index out of range

    First test case checks for a list missing some days
    Second test case checks a list with only 1 days value
    Third test case demonstrates that an empty list does not work
    '''
    #calculate and report low and high sales
    low, high = findRangeBug(salesli)
    print(f'Weekly Range: ${low:,.2f} - ${high:,.2f}\n')

    #print daily report header
    fw = 12
    print(f"{'Mon':<{fw}} {'Tue':<{fw}} {'Wed':<{fw}} {'Thu':<{fw}} {'Fri':<{fw}}")

    #report on sales per day from list data
    for sales in salesli:
        print(f'${float(sales):<{fw},.2f}', end='')
        
    return None

def test_calendar():
    '''
    (None) -> None

    
    August 2020
    Su Mo Tu We Th Fr Sa
                       1 
     2  3  4  5  6  7  8 
     9 10 11 12 13 14 15 
    16 17 18 19 20 21 22 
    23 24 25 26 27 28 29 
    30 31 
    February 2023
    Su Mo Tu We Th Fr Sa
              1  2  3  4 
     5  6  7  8  9 10 11 
    12 13 14 15 16 17 18 
    19 20 21 22 23 24 25 
    26 27 28 
    February 2024
    Su Mo Tu We Th Fr Sa
                 1  2  3 
     4  5  6  7  8  9 10 
    11 12 13 14 15 16 17 
    18 19 20 21 22 23 24 
    25 26 27 28 
    January 1
    Su Mo Tu We Th Fr Sa
        1  2  3  4  5  6 
     7  8  9 10 11 12 13 
    14 15 16 17 18 19 20 
    21 22 23 24 25 26 27 
    28 29 30 31 
    December 9999
    Su Mo Tu We Th Fr Sa
              1  2  3  4 
     5  6  7  8  9 10 11 
    12 13 14 15 16 17 18 
    19 20 21 22 23 24 25 
    26 27 28 29 30 31 
    Traceback (most recent call last):
      File "C:/Users/Jacob/Documents/University of Oregon Winter 2021/CIS 210/Week6/Projects/p62_fixed.py", line 95, in <module>
        test_calendar()
      File "C:/Users/Jacob/Documents/University of Oregon Winter 2021/CIS 210/Week6/Projects/p62_fixed.py", line 90, in test_calendar
        calendar(testTuple[0], testTuple[1])
      File "C:/Users/Jacob/Documents/University of Oregon Winter 2021/CIS 210/Week6/Projects\p51_calendar_key_W21.py", line 29, in calendar
        assert 1 <= month <= 12
    AssertionError
    '''
    testCases = [(8, 2020), (2, 2023), (2, 2024), (1, 1), (12, 9999), (0, 0)]
    '''
    First test case of (8, 2020) is a normal year
    Second test case of (2, 2023) is a month of february non leap year
    Thid test case of (2, 2024) is a month of febryary in a leap year. It only
    has 28 days so it is showing that the function does not account for leap
    years.
    Fourth test case of (1, 1) is showing it starts at the beggining of the
    possible calendars
    Fifth test case of (12, 9999) demonstrates the last possible calendar month
    Sixth test case of (0, 0) shows that it the function does not account for 0 as
    an integer option
    '''
    for testTuple in testCases:
        calendar(testTuple[0], testTuple[1])
    return None


print(doctest.testmod())
#test_calendar()
