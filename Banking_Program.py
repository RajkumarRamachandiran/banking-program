# python Banking Program
def show_balance():
    print(f"Your Balance is ₹{balance:.2f}")
def deposit():
    amount = float(input("Enter an amount to be deposit: "))

    if amount < 0:
        print("That's not valid amount")
        return 0
    else:
        return amount
def withdraw():
    amount = float(input("Enter Your withdrawal amount:"))

    if amount > balance:
        print("Insufficient Funds")
    elif amount < 0:
        print("Amount must be greater than 0")
    else:
        return amount

balance = 0
is_running = True
while is_running:
    print("*************************************")
    print("*************************************")
    print("_____🤑 Banking Program 🤑_____")
    print("*************************************")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.withdraw")
    print("4.Exit")

    choice = input("Enter your choice  Eg(1-4):")
    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("That is not valid choice")

print("THANK YOU HAVE A NICE DAY !")