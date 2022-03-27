def count(obj_list, obj):
    count = 0
    for i in obj_list:
        if i == obj:
            count += 1
    return count

def my_in(li, i):
    '''
    '''
    for item in li:
        if item == i:
            return True
    else:
        return li.reverse()
        #return item == i

days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
temps = [55, 23, 42, 44, 32, 60]

def createTempD(days, temps):
    '''
    '''
    dd = dict()
    for i in range(len(days)):
        dd[days[i]] = temps[i]
    return dd
    
x = createTempD(days, temps)

def temp_list(diction):
    '''
    '''
    tempList = []
    for i in diction:
        tempList.append(diction[i])
    tempList.sort()
    return tempList

tempList = temp_list(x)
