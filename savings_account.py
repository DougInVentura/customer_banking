"""Import the Account class from the Account.py file."""
import Account as acc

class Savings_account(acc.Account):
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
    # end of create class Savings_account


# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    My_savings_account = Savings_account(balance,0)
    # Calculate interest earned
    int_earned = My_savings_account.interest_earned(balance, interest_rate, months)
    # Update the savings account balance by adding the interest earned
    new_balance = balance + int_earned
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    My_savings_account.set_balance(new_balance)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    My_savings_account.set_interest(int_earned)
    # Return the updated balance and interest earned.
    return  new_balance, int_earned
