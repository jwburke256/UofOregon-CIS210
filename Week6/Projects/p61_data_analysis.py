'''
CIS 210 Winter 2021 Project 6-1: Data Analysis

Author: Jacob Burke

Credits: Python Programming in Context- Chapter 4

Created a series of functions used to anaylze a list of numbers. The types of
data values returned are the mean, median, and mode. Also created a function
that returns a frequency table. Finally a main function was created to
demonstrate the other functions using a list of earthquake magnitude data.
'''
import doctest

def isEven(n):
    '''
    (Integer) -> Boolean

    Returns true if argument is an even number, false if odd

    >>> isEven(4)
    True
    >>> isEven(58)
    True
    >>> isEven(0)
    True
    '''
    if n %2 == 0:
        return True
    else:
        return False

def mean(aList):
    '''
    (List) -> Float

    Returns the mean of a list of numbers

    >>> mean([1, 2, 3, 3, 4, 5])
    3.0
    >>> mean([])
    List cannot be empty
    0
    >>> mean([0])
    0.0
    '''
    if len(aList) > 0:
        mean = sum(aList) / len(aList)
    else:
        print("List cannot be empty")
        mean = 0
    return mean

def median(aList):
    '''
    (List) -> Number

    Returns the median number from a list of numbers

    >>> median([1, 2, 3, 3, 4, 5, 5])
    3
    >>> median([1, 2, 3, 4, 5, 5])
    3.5
    >>> median([])
    List cannot be empty
    '''
    copyList = aList[:] #make a copy using slice operator
    copyList.sort() #sort copy
    if len(aList) == 0:
        print("List cannot be empty")
        return None
    if isEven(len(copyList)) == True: #even length determined by isEven function
        rightMid = len(copyList) // 2
        leftMid = rightMid - 1
        median = (copyList[leftMid] +copyList[rightMid]) / 2
    else: #odd length
        mid = len(copyList) // 2
        median = copyList[mid]
    return median

def mode(aList):
    '''
    (List) -> Number

    Returns the most often number from a list of numbers

    >>> mode([1, 2, 3, 3, 4, 5])
    [3]
    >>> mode([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> mode([])
    List cannot be empty
    '''
    if len(aList) == 0:
        print("List cannot be empty")
        return None

    countDict = genFrequencyTable(aList)

    #Old Code:
    '''
    countDict = {}
    
    for item in aList: #creates a dictionary that holds each list item and number of times the item appears
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1
    '''

    countList = countDict.values() #makes a list that only has the count number of items
    maxCount = max(countList) #finds out the highest number of occurences in the original list using countList

    modeList = [] #adds the items from countDict that have the highest occurence to  modeList
    for item in countDict:
        if countDict[item] == maxCount:
            modeList.append(item)

    return modeList

def frequencyTable(aList):
    '''
    (List) -> None

    Prints a table of the the occurence values of each item in the list using a
    dictionary, with each item in the list printed in alphabetical order.

    >>> frequencyTable([1, 3, 3, 2])
    ITEM FREQUENCY
    1        1
    2        1
    3        2
    >>> frequencyTable([])
    List cannot be empty
    >>> frequencyTable(['a', 'a', 'b', 'c', 'c', 'd', 'c'])
    ITEM FREQUENCY
    a        2
    b        1
    c        3
    d        1
    '''
    if len(aList) == 0:
        print("List cannot be empty")
        return None

    countDict = genFrequencyTable(aList)
    
    #Old Code:
    '''
    countDict = {}
    for item in aList:
        if item in countDict: #Create dictionary to hold keys and occurence values
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1
    '''

    itemList = list(countDict.keys()) #make a list of keys from countDict
    itemList.sort() #Sort the key list

    print("ITEM", "FREQUENCY") #table headers

    for item in itemList: #Prints a table of the the occurence values of each item in the list using a dictionary, with each item in the list printed in alphabetical order
        print(item, "      ", countDict[item])
    return None

def genFrequencyTable(aList):
    '''
    (List) -> Dictionary

    Returns a dictionary with the key being an item in the list and the value
    associated with the key being the number of occurences of the item in the
    argument list.

    >>> genFrequencyTable([1, 2, 3, 3, 1, 4, 5])
    {1: 2, 2: 1, 3: 2, 4: 1, 5: 1}
    >>> genFrequencyTable([0, 1, 2, 3, 4, 5, 0, 0, 1, 0, 0])
    {0: 5, 1: 2, 2: 1, 3: 1, 4: 1, 5: 1}
    >>> genFrequencyTable([])
    List cannot be empty
    '''
    countDict = {}

    if len(aList) == 0:
        print("List cannot be empty")
        return None
    
    for item in aList:
        if item in countDict: #Create dictionary to hold keys and occurence values
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] =1
            
    return  countDict

def main():
    '''
    (None) -> None

    Function that shows a frequency tabble, along with the mean, median, and
    mode from a list of earthquake magnitutes.
    '''
    quakeList = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3, 2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6, 4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1, 4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9, 2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7, 4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7, 3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1, 2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1, 2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3, 6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4, 2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0, 2.5,4.9, 4.9, 2.5, 4.8, 3.1, 4.9, 4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5, 4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6, 2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1, 2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1, 2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5, 4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1, 4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0, 2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2, 3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5, 2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5, 2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7, 2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6, 2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9, 2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1, 3.1, 4.6, 2.8, 3.1, 6.3]
    frequencyTable(quakeList)
    print("mean = " + str(mean(quakeList)))
    print("median = " + str(median(quakeList)))
    print("mode = " + str(mode(quakeList)[0]))
    return None

main()

#print(doctest.testmod())
