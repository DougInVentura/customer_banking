# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
import cd_account as cd_account
import savings_account as sav_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    while True:
        try:
            savings_balance = float(input("Enter the balance to set up the savings account  "))
            break
        except ValueError:
            print("Try again! Enter the savings account balance as a (floating point) number.  Try again...")
    
    while True:
        try:
            savings_interest = float(input("Enter the annual interest rate as a (floating point) number to set up the savings account  "))
            break
        except ValueError:
            print("Try again! Enter the annual interest rate as a floating point number.  Try again...")

    while True:
        try:
            savings_maturity = int(input("Enter the number of months as a whole number to set up the savings account  "))
            break
        except ValueError:
            print("Try again! Enter the number of months as a whole number.  Try again...")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = sav_account.create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("")
    print(f"Your savings account interest earned is: ${savings_interest_earned:.2f}.")
    print(f"Your new savings account balance is ${updated_savings_balance:.2f}")
    print("")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    while True:
        try:
            cd_balance = float(input("Enter the balance to set up the CD account  "))
            break
        except ValueError:
            print("Try again! Enter the CD account balance as a (floating point) number.  Try again...")

    while True:
        try:
            cd_interest = float(input("Enter the annual CD interest rate as a (floating point) number to set up the CD account  "))
            break
        except ValueError:
            print("Try again! Enter the annual CD interest rate as a floating point number.  Try again...")

    while True:
        try:
            cd_maturity = int(input("Enter the number of months as a whole number to set up the CD account  "))
            break
        except ValueError:
            print("Try again! Enter the number of months as a whole number for your CD account.  Try again...")


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = cd_account.create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("")
    print(f"On your CD account, you have interest earned of: ${cd_interest_earned:.2f}.")
    print(f"and your new CD account balance is: ${updated_cd_balance:.2f}")
    print("")
    
if __name__ == "__main__":
    # Call the main function.
    main()