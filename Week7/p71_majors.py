'''
CIS 210 Winter 2021 Project 7-1: Who takes CIS 210?

Author: Jacob Burke

Credits: N/A

Python project to process a file of majors, analyze the data, then print off the
reusults of the data using created functions.
'''
#import doctest.testmod()
from p61_data_analysis import frequencyTable

def majors_readf(fname):
    '''
    (Str) -> List

    Reads a file of majors and returns a list of the majors contained
    within the file.

    
    '''
    with open(fname, 'r') as fileRef:
       #major_data = fileRef.read()
        majorsli = []
        fileRef.readline()
        fileRef.readline()
        for line in fileRef:
            majors = line.strip()
            majorsli.append(majors)
        return majorsli


def majors_analysis(majorsli):
    '''
    (List) -> Tuple

    Takes a list of majors and returns a tuple that has a list of the most
    common majors and the number of occurences in the list.
    
    >>> majors_analysis(['CIS', 'CIS', 'EXPL', 'COLT', 'EXPL'])
    (['CIS', 'EXPL'], 3)
    '''
    countDict = {}
    majorCount = 0

    
    for item in majorsli: #creates a dictionary that holds each list item and number of times the item appears
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1
            majorCount += 1
    countList = countDict.values() #makes a list that only has the count number of items
    maxCount = max(countList) #finds out the highest number of occurences in the original list using countList
    modeList = [] #adds the items from countDict that have the highest occurence to  modeList
    for item in countDict:
        if countDict[item] == maxCount:
            modeList.append(item)
    majorTuple = (modeList, majorCount)
    return majorTuple

            

def majors_report(majors_mode, majors_ct, majorsli):
    '''
    (Int, Int, List) -> None

    Function that prints a data analysis of majors.
    '''
    print(str(majors_ct) + ' majors are represented in CIS 210 this term.')
    print('The most represented major(s): ' + str(majors_mode) + '\n')
    frequencyTable(majorsli)
    
    return None

def main():
    '''
    () -> None
    Calls:  majors_readf, majors_analysis, majors_report
    Top level function for analysis of CIS 210 majors data.
    '''
    majorsli = majors_readf('p71-majors-cis210W20.txt')
    majorsTuple = majors_analysis(majorsli)
    majors_mode, majors_ct = majorsTuple
    majors_report(majors_mode, majors_ct, majorsli)
    return None
main()
