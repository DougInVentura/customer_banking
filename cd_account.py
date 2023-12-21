""" Import the Account class from the Account.py file.
    create the CD_account class
    create the create_cd_account function that received the balance, interest and months and returns the interest earned.
"""
# ADD YOUR CODE HERE
import Account as acc

class CD_account(acc.Account):
    def __init__(self, balance, interest):
        super().__init__(balance, interest)

    def interest_earned(self, balance, interest_rate, months):
        '''
        Arg:
            balance (float): The initial savings account balance.
            interest_rate (float): The APR interest rate for the savings account.  This is as a percentage
            months (int): The length of months to determine the amount of interest.

        Returns:
            float: The updated savings account balance after adding the interest earned.
        '''
        int_earned = balance * interest_rate/100 * months/12.0
        return int_earned
        # end of def of class CD_account


def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    My_CD_account = CD_account(balance,0)
    
    # Calculate interest earned
    int_earned = My_CD_account.interest_earned(balance, interest_rate, months)

    # Update the CD account balance by adding the interest earned
    new_balance = balance + int_earned
    
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    My_CD_account.set_balance(new_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    My_CD_account.set_interest(int_earned)

    # Return the updated balance and interest earned.
    return  new_balance, int_earned
