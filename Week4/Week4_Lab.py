'''
Author: Jacob Burke

Ciontributors: N/A

'''

def greeting(f, s):
    print('Calling ' + f.__name__)
    f(s)
    return None

def hello(s):
    ''' '''
    print('Hello, ' + s + '.')
    return None

def ciao(s):
    print('Ciao ' + s + '.')
    return None
