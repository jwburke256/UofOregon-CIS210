def foo(x):
    x.pop()
    return

def bar(x):
    foo(x)
    y = foo(x); print(x, y)
    x = foo(x)
    return

x = ['CIS 210', 'CIS 211', 'CIS 212']
foo(x)
bar(x)
print(x)

def myD_to_li(myD):
    list1 = []
    list2 = []
    for key in myD:
        list1.append(key)
        list2.append(myD[key])

        return (list1, list2)
    
def who_is_winning(fname):
    '''
    (File) -> None

    Takes a file containing CDC vaccination data and print out the current state
    that has the largest percentage of it's population that has received 2
    vaccine doses.

    >>> who_is_winning('CDCData.txt')
    The current State winning the vacination race is Oregon
    '''
    with open(fname, 'r') as fileRef:
        for i in range(3):
            fileRef.readline()
        statesDict = {}
        for line in fileRef:
            newLine = line.strip()
            newList = newLine.split()
            state = newList[0]
            statePopulation = newList[1]
            state_2Doses = newList[5]
            statesDict[state] = [statePopulation, state_2Doses]
        winningState = ['', 0]
        for Key in statesDict:
            statePopData = statesDict[Key]
            statePercent = (int(statePopData[1]) / int(statePopData[0]) * 1000)
            if statePercent > int(winningState[1]):
                winningState[0] = Key
                winningState[1] = statePercent
        print('The current State winning the vacination race is', winningState[0])
        return None

            
#stateDict = who_is_winning('CDCData.txt')
