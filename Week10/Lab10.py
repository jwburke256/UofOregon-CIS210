import doctest

def even(i):
    '''(int) -> Boolean
    return True if i is an even number
    >>> even(4)
    True
    >>> even(3)
    False
    '''
    return (i % 2) == 0


def median(alist):
    '''
    (list of numbers) -> number
    Return median of alist (for alist of len > 0).
    >>> median([5, 7, 1, 3]) # even number of items 
    4.0
    >>> median([1, 2, 2, 3, 99]) # odd number of items
    2
    >>> median([99]) # list with 1 item
    99
    >>> median([99, 101]) # list with 2 items
    100.0
    >>> median([0, 0, 0, 0]) # all items are the same
    0.0
    '''
    copyl = alist[:]
    copyl.sort()
    copylen = len(copyl)
    
    if even(copylen):
        rmid = (copylen // 2) - 1
        lmid = rmid + 1
        if rmid == 0:
            medi = ((copyl[0] + copyl[1]) / 2)
        else:
            medi = ((copyl[rmid] + copyl[lmid]) / 2)
    
    else:
        mid = copylen // 2
        medi = copyl[mid]
    
    return medi

print(doctest.testmod())
