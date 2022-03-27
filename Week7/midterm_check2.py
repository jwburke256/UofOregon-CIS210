def foo(x):
    x.pop()
    return

def bar(x):
    foo(x)
    y = foo(x); print(x, y)
    x = foo(x)
    return

#x = ['CIS 210', 'CIS 211', 'CIS 212']
#foo(x)
#bar(x)
#print(x)

def myD_to_li(myD):
    list1 = []
    list2 = []
    for key in myD:
        list1.append(key)
        list2.append(myD[key])

        return (list1, list2)
    
def who_is_winning(fname):
    '''
    '''
    with open(fname, 'r') as fileRef:
        for i in range(3):
            fileRef.readline()
        statesDict = {}
        for line in fileRef:
            newLine = line.strip()
            newList = newLine.split()
            state = newList[0]
            statePopulation = newlist[1]
            state_2Doses = newlist[5]
            statesDict[state] = [statePopulation, state_2doses]
        return statesDict

stateDict = who_is_winning('CDCData.txt')
