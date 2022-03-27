'''
'''

import doctest
import os

def readFile(file):

    with open(file) as f:
        for line in f:
            print(f.readline())

