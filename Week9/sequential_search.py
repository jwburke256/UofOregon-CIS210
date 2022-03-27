import random
import time


def isin(seq, t): #sequential search
    '''
    '''
    for item in seq:
        if item == t:
            return True
        
    return False

def isIntest(f):
    tests = [((1, 2, 3), 3, True),
            ('hello', 'i', False)
             ((), 74, False)
        ]

    for test in tests:
        result = f(test[0], test[1]) == test[2]
        if result == True:
            print('Passed')
        else:
            print('Failed')
    return None



isIntest(isin)


'''
N = 10000 #length of list
seq = []



t = (random.randint(0, N))

repeats = 100 #number of times sequential search is done

start = time.time() #start time
for r in range(repeats):
    seq = []
    for i in range(N):
        seq.append(int(N*random.random()))
        
    t = (random.randint(0, N))
    result = isin(seq, t)
    
end = time.time() #end time

avg_time = (end-start)/repeats

'''
#print(avg_time)
