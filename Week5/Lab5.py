#if __name__ == '__main__':
def letterhead(string):
    
    print(('*' * 6) + ('*' * len(string)) + ('*' * 6))
    print('*     ' + string + '     *')
    print(('*' * 6) + ('*' * len(string)) + ('*' * 6))
    return None

def moneyformat(Num):
    print(f'${Num:,.2f}')

def columns(List1, List2):
    
