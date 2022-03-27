'''
CIS 210 Week 8 Lab Winter 2021

Author: Jacob B.

Credits: N/A

Exercises for assert and try/except.
'''

days = ['Mo', 'Tu', 'We', 'Th']
temps = [55, 23, 42, 44]


def createTempD(days, temps):
    dd = {}
    countList = len(days)
    for i in range(countList):
        dd[days[i]] = temps[i]
    return dd

dd = createTempD(days, temps)
print(dd['We'])
dd['Fr'] = 32

tempList = []
for key in dd:
    tempList.append(dd[key])
tempList.sort()
print(tempList)
dd['Sa'] = 60
print(dd)
del dd['Sa']
print(dd)
dd['Sa'] = 60
dd['Su'] = dd['Sa'] + 10
print(dd)

def count(list):
    count = 0
    for obj in list:
        count += 1
    return count

print(count(days))

def index(li, i):
    for item in li:
        if item == i:
            return True
        else:
            return -1

print(index(days, 'Thur'))

print(days)
def reverse(li):
    licopy = li[:]
    listCount = len(li)
    for i in range(listCount):
        negi = (i+1) *-1
        li[i] = licopy[negi]
    return li

reverse(days)

print(days)
