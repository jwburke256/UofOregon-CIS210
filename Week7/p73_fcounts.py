'''
CIS 210 Winter 2021 Project 7-3: Inspecting Files

Author: Jacob Burke

Credits: N/A

Python project to iterate through a text file and return back the number of
lines, words, and characters found within it.
'''
from p61_data_analysis import frequencyTable

def fcounts(fname):
    '''
    (String) -> Tuple

    Iterates through lines in a file, returning a tuple that contains the number
    of lines, the number of characters, and a list of the words in the file.
    '''
    with open(fname, 'r') as fileRef:
        lineCount = 0
        characterCount = 0
        wordList = []
        for line in fileRef:
            lineCount += 1
            newLine = line.strip().rstrip(',.').lower()
            #print(newLine)
            for character in newLine:
                characterCount += 1
            newList = newLine.split()
            for item in newList:
                wordList.append(item)
        fcountsTuple = (lineCount, characterCount, wordList)
    return fcountsTuple
def main(fname):
    '''
    (String) -> None

    Calls: frequencyTable
    Top level function for iterating through a file. Returns None
    '''
    fcountsTuple = fcounts(fname)
    print('The number of lines in file ', fname, ' is: ', fcountsTuple[0])
    print('The number of characters in file ', fname, ' is: ', fcountsTuple[1])
    print('The number of words in file ', fname, ' is: ', len(fcountsTuple[2]))
    frequencyTable(fcountsTuple[2])
    
main('medium.txt')
