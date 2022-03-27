def mycharct(s,c):
    cct = 0
    for char in s:
        if char == c:
            cct += 1
        return cct

def parity(bitrep):
    p = 0

    for bit in bitrep:
        #print(bit)
        if bit == '1':
            p += 1
            

    if p % 2 == 0:
        p = '0'
    else:
        p = '1'

    return p

#parity('1100011')


    
def q23(astr):
    countd = {}
    for item in astr:
        if item in countd:
            countd[item] += 1
        else:
            countd[item] = 1
    countli = countd.values()
    ct = max(countli)

    mli = [item for item in countd if countd[item] == ct]
    '''
    for item in countd:
        if countd[item] == ct:
            mli.append(item)
            print(mli)

'''
    print(mli)


teststr = 'aabbbc'
#q23(teststr)
'''
course1 = 'CIS 210'
course2 = course1
course1 = course1[:len(course1)-1] + '1'
print(id(course1) == id(course2))
print(course1 == course2)
print(course1)
'''

def findRange(salesli):
    salesli.sort()
    low = salesli[0]
    high = salesli[-1]
    return low, high

def salesReport(salesli):
    low, high = findRange(salesli)
    print(salesli)
    print(f'Weekly Range: ${low *100} - ${high *100}\n')

    fw = 12
    print(f"{'Mon':<{fw}} {'Tue':<{fw}} {'Wed':<{fw}} {'Thu':<{fw}} {'Fri':<{fw}}")

    for sales in salesli:
        print(f'${(sales * 100):<{fw}}', end='')

    return None

#salesReport([4, 2, 3, 1, 2])

import math

def pizza_calculator(diameter, cost):

    r = diameter / 2
    area = math.pi * r**2
    cost_per_inch = cost/area
    cost_per_inch = round(cost_per_inch, 3)

    return cost_per_inch

#print(pizza_calculator(10, 0.00))


from turtle import *

def drawGPS(gpstxtfile):
    '''
    (None) -> None

    Draws the route when given a file that contains gps coordinate data using
    the turtle module and returns None when finished.
    '''
    #Opens a gps file and creates a list that holds gps coordinates
    with open(gpstxtfile, 'r') as checkf:
        checkf.readline() #move past header
        turtleli = []
        for line in checkf:
            lineli = line.strip().split(',') #strip line
            lat_lon_tuple = (lineli[1], lineli[2])
            turtleli.append(lat_lon_tuple)
        #print(turtleli)

        speed(0) #set turtle speed
        penup()
        #set turtle starting position
        sety(float(turtleli[0][0])) #y values are lat
        setx(float(turtleli[0][1])) #x values are lon
        pendown()
        #draw gps coordinate movements with for loop
        for i in range(len(turtleli)):
            sety(float(turtleli[i][0]))
            setx(float(turtleli[i][1]))

    return None


#drawGPS('racetrack_gps.txt')

    


