# ----------------------------------------------------------------------
# Name:        HW2
# Purpose:     Generate intrest
#
# Date:       2/5/2019
# ----------------------------------------------------------------------
"""
Print accrued amount after n years of interest

Prompt the user for principal amount
Prompt the user for interest rate
Print accrued amount every 5 years from 5-50 inclusive
"""

def accrued_amount(years,principal_amount,intrest_rate):
    """
    Calculate the accrued amount of money
    :param years: (number) number of years
    :param principal_amount: (number) principal amount invested
    :param intrest_rate: (number) intrest rate
    :return: (number) ammount accured over years
    """
    return principal_amount * (1+(intrest_rate/100))**years
def print_accrued(years,amount):
    """
    print a formatted string
    :param years: (number) number of years
    :param amount: (number) amount to be printed
    """
    formatted_amt = f'${amount:,.2f}'
    print("Accrued amount after " f'{years:>2}' " years: " f'{formatted_amt:>15}')
def query_info():
    """
    Query user for principal amount and interest rate
    :return: (touple) principal amount,interest rate
    """
    success = False
    while not success:
        principal_amount = float(input('Please enter principal amount: $'))  # Prompt user
        if(1000000 >= principal_amount >= 0):
            success = True
        else:
            print('Invalid amount. Principal must be between $0 and $1,000,000.00')
    success = False
    while not success:
        interest_rate = float(input('Please enter interest rate: %'))  # Prompt user
        if(100 >= interest_rate >= 0):
            success = True
        else:
            print("Invalid rate. Interest rate must be between 0 and 100")
    return (principal_amount,interest_rate)
def main():
    while True:
        inputs_from_user = query_info()
        for each_year in range(5,55,5):
            print_accrued(each_year,accrued_amount(each_year,inputs_from_user[0],inputs_from_user[1]))


if __name__ == "__main__":
    main()
