'''
CIS 210 Winter 2021 Project 7-4: File Concordance

Author: Jacob Burke

Credits: N/A

Python project to iterate through a text file and return a dictionary that
contains info on what line each word within the file can be found.
'''
def fconcordance(fname):
    '''
    (String) -> Dict

    Iterates through lines in a file, creating a dictionary that stores words
    and where they occur within the file, then returns the dictionary.
    '''
    with open(fname, 'r') as fileRef:
        lineCount = 0
        wordDict = {}
        for line in fileRef:
            lineCount += 1
            newLine = line.strip().rstrip(',.').lower()
            newList = newLine.split()
            for word in newList:
                dictFormat = "'" + word + "' occurs in lines:"
                if dictFormat in wordDict: #Create dictionary to hold keys and occurence values
                    wordDict[dictFormat] = wordDict[dictFormat] + [lineCount]
                else:
                    wordDict[dictFormat] = [lineCount]
    return wordDict

def main(fname):
    '''
    (String) -> None

    Calls: fconcordance
    Top level function for iterating through a file. Returns None
    '''
    wordDict = fconcordance(fname)
    for item in wordDict:
        print(item, wordDict[item])
    return None
main('medium.txt')
