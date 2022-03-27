'''
CIS 210 Winter 2021 Project 7-2: Earthquake Watch?

Author: Jacob Burke

Credits: N/A

Python project to analyze earthquake csv files and report back magnitude data.
'''
import csv
from p61_data_analysis import *
def equake_readf(fname):
    '''
    (Str) -> List

    Reads a file of earthquake data and returns a list of the earthquake
    magnitudes
    '''
    with open(fname, 'r') as fileRef:
        csvReader = csv.reader(fileRef) #feed file to csv reader
        magnitudesList = []
        titles = next(csvReader) #read first line with titles
        #print(titles)
        colNum = 0 #prime the condition
        while titles[colNum] != 'mag':
            colNum += 1 #update the condition
        #print('The magnitude is found in column', colNum)
        for line in csvReader:
            magnitudesList.append(float(line[colNum]))
        #print(magnitudesList)
        return magnitudesList

def equake_analysis(magnitudes):
    '''
    (List) -> Tuple
    
    Calls: mean, median, mode
    Calculates the mean, median and mode from a list of earthquake magnitudes,
    then returns the data as a Tuple.
    '''
    magnitudesMean = mean(magnitudes)
    magnitudesMedian = median(magnitudes)
    magnitudesMode = mode(magnitudes)
    magnitudesTuple = (magnitudesMean, magnitudesMedian, magnitudesMode)
    return magnitudesTuple
    
def equake_report(magnitudes, mmm, minmag):
    '''
    (List, Tuple, Num) -> None

    Calls: frequencyTable
    Reports back the number of magnitudes, mean, median and mode from a list
    of earthquake magnitudes. Then displays a frequency table.
    '''
    print('Number of earthquakes: ', len(magnitudes))
    print('Mean magnitude is ', mmm[0])
    print('Median magnitude is: ', mmm[1])
    print('Mode(s) of magnitude is: ', mmm[2], '\n')
    frequencyTable(magnitudes)
    return None
    
def main():
    '''
    () -> None

    Calls: equake_readf, equake_analysis, equake_report
    Top level function for earthquake data analysis. Returns None
    '''
    magnitudesList = equake_readf('p72-equakes-25f-2019.csv')
    magnitudesTuple = equake_analysis(magnitudesList)
    equake_report(magnitudesList, magnitudesTuple, 2.5)
    print('\n')
    magnitudesList = equake_readf('p72-equakes-50f-2019.csv')
    magnitudesTuple = equake_analysis(magnitudesList)
    equake_report(magnitudesList, magnitudesTuple, 5.0)
    return None
main()
