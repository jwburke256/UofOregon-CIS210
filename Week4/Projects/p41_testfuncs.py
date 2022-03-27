'''
CIS 210 Winter 2021 Project 4-1: Testing

Author: Jacob Burke

Credits: N/A

Created a test_sscount function to act as a doctest.testmod function
specifically for those functions.
'''
import p34_sscount_sol_W21 as p34

def test_sscount(f, args, expected_result):
    '''
    (Function, String, Integer) -> None

    Tests the sscount functions expected results against the actual results
    output by the functions.
    '''
    print('testing ' + f.__name__)
    print('Checking ' + args)
    string_list = str.split(args)
    arg1 = string_list[0]
    arg2 = string_list[1]
    test_result = f(arg1, arg2)
    if test_result == expected_result:
        print("its value " + str(test_result) + " is correct!")
    else:
        print("its value " + str(test_result) + " is incorrect.")
    return None

def main():
    test_sscount(p34.sscount0, 'sses assesses', 2)
    test_sscount(p34.sscount1, 'sses assesses', 2)
    test_sscount(p34.sscount0, 'an trans-Panamanian banana', 6) #Does not work as the function splits up the args parameter using whitespace
    test_sscount(p34.sscount1, 'an trans-Panamanian banana', 6) #Does not work as the function splits up the args parameter using whitespace
    test_sscount(p34.sscount0, 'needle haystack', 0)
    test_sscount(p34.sscount1, 'needle haystack', 0)
    test_sscount(p34.sscount0, '!!! !!!!!', 3 )
    test_sscount(p34.sscount1, '!!! !!!!!', 3 )
    test_sscount(p34.sscount0, 'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)
    test_sscount(p34.sscount1, 'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)
    #test_sscount(p34.sscount0, '', 0) #Does not work as there is no argument to pass to the function
    #test_sscount(p34.sscount1, '', 0) #Does not work as there is no argument to pass to the function
    #test_sscount(p34.sscount0, 'a ', 0) #Does not work as there is only 1 argument to pass to the function
    #test_sscount(p34.sscount1, 'a ', 0) #Does not work as there is only 1 argument to pass to the function
    #test_sscount(p34.sscount0, ' abc', 0) #Does not work as there is only 1 argument to pass to the function
    #test_sscount(p34.sscount1, ' abc', 0) #Does not work as there is only 1 argument to pass to the function
    test_sscount(p34.sscount0, 'a a', 1)
    test_sscount(p34.sscount1, 'a a', 1)
    
    
    return None




main()
    
