'''
CIS 210 Winter 2021 Project 4-2: Bugs, bugs, bugs

Author: Jacob Burke

Credits: N/A

Testing and debugging code, while doumenting.
'''
import doctest

def ratsBug(weight, rate):
    '''(number, number) -> tuple

    Return number of weeks it will
    take for a rat to weigh 1.5 times
    as much as its original weight
    (weight > 0) if it gains at rate (rate > 0).

    >>> ratsBug(10, .1)     # normal
    (16.1, 5)
    >>> ratsBug(1, .5)      # edge - just one week
    (1.5, 1)
    >>> ratsBug(0, 0.1)     # edge - weight 0
    (0, 0)
    >>> ratsBug(10, 0)      #edge - rate 0
    (10, 0)
    >>> ratsBug(10, -1)     #edge - negative rate
    rate cannot be less than 0
    '''
    if rate == 0: #accounts for if a user puts in a rate of 0
        return (weight, rate)
    if rate < 0:
        return print("rate cannot be less than 0")
    weeks = 0
    orig_weight = weight #added variable to account for original weight
    while weight < (1.5 * orig_weight): #Missing semi-colon
        weight += weight * rate
        weeks = weeks + 1 #wks changed to weeks
        
    weight = round(weight, 1)
    return (weight, weeks)

def countSeqBug(astr):
    '''(str) -> int

    Returns the length of the longest recurring
    sequence in astr

    >>> countSeqBug('abccde')  # normal  	
    2
    >>> countSeqBug('')        # edge - empty string
    0
    >>> countSeqBug('ccccc')   # multiple normal characters 
    5
    >>> countSeqBug('!!!!!')   # edge - ! charachter
    5
    >>> countSeqBug('Test   meee') # multiple spaces to split string
    3
    '''
    if len(astr) != 0:
        prev_item = astr[0]
        dup_ct = 1
        high_ct = 1
    else:
        high_ct = 0
        dup_ct = 0
        
    for i in range(1, len(astr)): #Starting range value adjusted
        if astr[i] == prev_item:
            dup_ct += 1
        else:
            prev_item = astr[i]
            dup_ct = 1 #dup_ct reset moved in order to properly reset
			
        if dup_ct > high_ct: #wrong indentation
            high_ct = dup_ct

    return high_ct

def my_averageBug(dataset):
    '''(str) -> float

    Returns average of values in input string values,
    but zeros do not count at all.  Return 0 if there
    is no real data.
    
    >>> my_averageBug('23')    #normal, no zeros
    2.5
    >>> my_averageBug('203')   #normal, a zero
    2.5
    >>> my_averageBug('0000')  #all zeros
    0
    >>> my_averageBug('1')     #single item string
    1.0
    >>> my_averageBug('05050505')  
    5.0
    '''
    count = 0
    total = 0
    for value in dataset:
        if type(value) != int(value):
            print('Dataset must be a set of integers only')
            return
        if value != '0':
            total += int(value) # use int to change string to integer
            count += 1 #wrong indentation
    if count == 0: #Added if else statements to account for average being zero
        avg = 0
    else:
        avg = total / count
    return avg

print(doctest.testmod())
