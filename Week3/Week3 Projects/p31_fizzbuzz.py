''' 
CIS 210 Project 3-1 Fizzbuzz

Author: Jacob Burke

Credits: N/A

Create a function that loops through a range of integers and returns fizz, buzz,
or fizzbuzz depending on if the integer is divisble by a certain number.
'''

def fb(n):
    '''
    (Integer) -> None

    Uses a for loop given n to act as a range that prints out "fizz" if a
    number in the range is divisible by 3, "buzz" if by 5, and "fizzbuzz" if
    both. Otherwise it will just print the number.
    
    >>> fb(15)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    Game over!
    '''
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
    print("Game over!")
    return None
