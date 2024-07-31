Functions:
show_balance(balance):

Purpose: Displays the current balance.
Parameters: balance (the current balance to be displayed).
Functionality: Prints the balance formatted to two decimal places.
deposit():

Purpose: Allows the user to deposit money into their account.
Parameters: None.
Functionality: Prompts the user to enter an amount. It checks if the input is a valid number and greater than zero. If valid, returns the deposit amount; otherwise, it returns 0.
withdraw(balance):

Purpose: Allows the user to withdraw money from their account.
Parameters: balance (the current balance to check for sufficient funds).
Functionality: Prompts the user to enter a withdrawal amount. It checks if the input is a valid number, greater than zero, and if there are sufficient funds in the account. If valid, returns the withdrawal amount; otherwise, it returns 0.
Main Program Loop:
Initialization:

balance = 0: Initializes the balance to zero.
is_running = True: Sets the loop control variable to keep the program running.
Menu Display and User Input:

Displays the menu options to the user.
Prompts the user to enter a choice (1-4).
Choice Handling:

Choice '1': Calls show_balance(balance) to display the current balance.
Choice '2': Calls deposit() to get the deposit amount and adds it to balance.
Choice '3': Calls withdraw(balance) to get the withdrawal amount and subtracts it from balance.
Choice '4': Sets is_running to False to exit the loop and end the program.
Invalid Choice: Prints an error message for invalid menu choices.
Exit Message:

Prints a thank you message when the user exits the program.
Summary:
The program allows users to check their balance, deposit money, and withdraw money through a simple text-based interface.
Error handling ensures that invalid inputs (non-numeric values, negative amounts, insufficient funds) are managed gracefully.
The main loop keeps the program running until the user chooses to exit.
