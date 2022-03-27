''' 
CIS 210 Project 3-4 Python Strings/Counting

Author: Jacob Burke

Credits: N/A

Create functions that loop through string slices to search for a specific
substring.
'''
import doctest

def sscount0(needle, haystack):
    '''
    (String, String) -> Integer

    Returns the number of times that a substring occurs in another string.

    >>> sscount0('wood', 'woodchuckwoodchuckwood')
    3
    >>> sscount0('!!!', '!!!!!')
    3
    >>> sscount0('sses', 'assesses')
    2
    >>> sscount0("ss", "mississippiseriesses")
    3
    '''
    count = 0
    needle_len = len(needle)
    for i in range(0, len(haystack) + 1):
        slice_object = slice((i), (i + needle_len))
        new_str = haystack[slice_object]
        if new_str == needle:
            count += 1
    return count

def sscount1(needle, haystack):
    '''
    (String, String) -> Integer

    Returns the number of times that a substring occurs in another string.

    >>> sscount1('wood', 'woodchuckwoodchuckwood')
    3
    >>> sscount1('!!!', '!!!!!')
    3
    >>> sscount1('sses', 'assesses')
    2
    >>> sscount1("ss", "mississippiseriesses")
    3
    '''
    count = 0
    for i in range(0, len(haystack) + 1):
        if haystack.startswith(needle, i, i + len(needle)) == True:
            count += 1
    return count

print(doctest.testmod())
