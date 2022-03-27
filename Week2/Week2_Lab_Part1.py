def is_even(n):
    '''
    (int) -> Boolean

    Returns True if n
    is an even number.

    >>> is_even(100)
    True
    >>> is_even(101)
    False
    >>> is_even(0)
    True
    '''
    return (n % 2) == 0

# print(is_even(2))
# result = print(is_even(3))

def welcome():
    '''
    () -> ()

    Print welcome message.

    >>> welcome()
    Good morning CIS 210!
    '''
    print('Good morning, CIS 210!')
    return None

# welcome()

def est_tax(income, exemptions):
    '''(number, integer) -> float

    Generates an estimate for federal income tax.

    CALLS: taxable

    >>> est_tax(20000, 1)
    1870.0
    '''
    # Set values needed to generate estimate
    STD_EXEMPT = 4150
    STD_DEDUCT = 6500
    TAX_RATE = .20

    # Calculate federal tax by adjusting
    # repaorted income and applying tax rates
    taxable_income = taxable(income, exemptions, STD_EXEMPT, STD_DEDUCT)
    estimated_tax = taxable_income * TAX_RATE

    print('Estimated tax is: '+ str(estimated_tax))
    return None

def taxable(income, exemptions, STD_EXEMPT, STD_DEDUCT):
    '''(number int, number, number) -> None

    Adjust gross income (i) to taxable income
    by applying standard deduction and exemptions.

    CALLED BY: est_tax

    >>> taxable(20000, 1, 4150, 6500)
    9350
    '''
    taxable_income = income - STD_DEDUCT
    exempt_adjust = STD_EXEMPT * exemptions
    taxable_income = taxable_income - exempt_adjust

    return taxable_income

est_tax(20000, 1)
