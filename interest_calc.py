# ----------------------------------------------------------------------
# Name:        interest_calc
# Purpose:     A simple accrued interest calculator
#
# Date:       2/5/2019
# ----------------------------------------------------------------------
"""
Print accrued amount after n years of interest

Prompt the user for principal amount
Prompt the user for interest rate
Print accrued amount every 5 years from 5-50 inclusive
"""

def accrued_amount(years, principal_amount, interest_rate):
    """
    Calculate the accrued amount of money
    :param years: (number) number of years
    :param principal_amount: (number) principal amount invested
    :param interest_rate: (number) interest rate
    :return: (number) amount accrued over years
    """
    return principal_amount * (1 + (interest_rate / 100)) ** years

def print_accrued(years, amount):
    """
    Print a formatted string
    :param years: (number) number of years
    :param amount: (number) amount to be printed
    """
    formatted_amt = f'${amount:,.2f}'
    print(f'Accrued amount after {years:>2} years: {formatted_amt:>15}')

def query_info():
    """
    Query user for principal amount and interest rate
    :return: (tuple) principal amount, interest rate entered
    """
    valid = False
    while not valid:
        principal = float(input('Please enter principal amount: $'))
        if (1000000 >= principal >= 0):
            valid = True
        else:
            print('Invalid amount. '
                  'Principal must be between $0 and $1,000,000.00')
    valid = False
    while not valid:
        interest_rate = float(input('Please enter interest rate: %'))
        if (100 >= interest_rate >= 0):
            valid = True
        else:
            print('Invalid rate. '
                  'Interest rate must be between 0 and 100')
    return (principal, interest_rate)

def main():
    while True:
        inputs_from_user = query_info()
        for each_year in range(5, 55, 5):
            print_accrued(each_year, accrued_amount(
                each_year, inputs_from_user[0], inputs_from_user[1]))

if __name__ == "__main__":
    main()
