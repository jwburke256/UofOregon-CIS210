'''
CIS 210 Winter 2021 Project 5-1

Author: [Solution]

Credits: N/A

Calendar layout

Explore datetime module, formatted strings,
nested for loop, scenarios for start, middle, end cases.
'''
import datetime

def calendar(month, year):
    """(int, int) -> None

    prints calendar for input month, year
    returns None

    > calendar(11, 2019)
    [calendar for November 2019 - 30 days]
    > calendar(12, 2019)
    [calendar for December 2019 - 31 days]
    > calendar(2, 2018)
    [calendar for February 2018 - 28 days, different year]
    > calendar for [months that start and end on different days of the week]
    """
    assert 1 <= month <= 12
    '''
    MONTHS_DAYS = '31 28 31 30 31 30 31 31 30 31 30 31 '
    idx = (month - 1) * 3
    this_month_days = int(MONTHS_DAYS[idx:idx+2])

    MONTHS_NAMES = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'
    idx = (month - 1) * 4
    this_month_name = MONTHS_NAMES[idx:idx+3]
    '''
    '''
    MONTHS_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MONTHS_NAMES = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November',
                    'December']
    this_month_days = MONTHS_DAYS[month-1]
    this_month_name = MONTHS_NAMES[month-1]
    '''
    MONTHS_NAMES = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November',
                    'December']
    MONTHS_DAYS = {'January': 31, 'February': 28, 'March': 31, 'April': 30,
                   'May':31, 'June':30, 'July':31, 'August':31, 'September':30,
                   'October':31, 'November':30,'December':31}
    this_month_name = MONTHS_NAMES[month-1]
    this_month_days = MONTHS_DAYS[this_month_name]
    
    adate = datetime.date(year, month, 1)
    # Monday = 1 ... Sunday = 7
    startday = adate.isoweekday() % 7  # make Sunday the 0th day

    # print calendar header
    print(this_month_name, year)
    print('Su Mo Tu We Th Fr Sa')
    #print(f"{'Su':>2} {'Mo':>2} {'Tu':>2} {'We':>2} {'Th':>2} {'Fr':.2} {'Sa':.2}")

    date = 1

    # print 1st line of calendar
    # first date may be part way into the week
    leadspace = (startday * 3)
    print(f'{date:>{leadspace + 2}} ', end='')
    date += 1

    # now print the rest of the first line
    for i in range(7 - startday - 1):
        print(f'{date:>2} ', end='')
        date += 1
    print()
  
    # now print the middle lines
    midlines = (this_month_days - date) // 7
    for i in range(midlines):
        for i in range(7):
            print(f'{date:>2} ', end='')
            date += 1
        print()

    # now print the last line
    for i in range (this_month_days - date + 1):
        print(f'{date:>2} ', end='')
        date += 1
    print()
   
    return None
    
def main():
    calendar(11, 2019)
    print()
    calendar(12, 2019)
    return None

if __name__ == '__main__':
    main()
