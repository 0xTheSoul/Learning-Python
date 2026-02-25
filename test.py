# Bank Account System

balance = 1000.50  # float
account_holder = "Soul"  # string
is_logged_in = True  # boolean
pin = 1234  # integer

print(f"Welcome to the Bank System")

# loop to give 3 attempts at pin
attempts = 0
while attempts < 3:
    entered_pin = int(input("Enter your PIN: "))
    
    if entered_pin == pin:
        is_logged_in = True
        print("Login successful!")
        break
    else:
        is_logged_in = False
        attempts += 1
        print(f"Wrong PIN. {3 - attempts} attempts remaining")

# only runs if logged in
if is_logged_in:
    print(f"\nHello {account_holder}!")
    print(f"Current balance: ${balance}")
    
    # loop through recent transactions
    transactions = [200.00, -50.75, -20.00, 500.00]  # list
    print("\nRecent transactions:")
    for transaction in transactions:
        if transaction > 0:
            print(f"  Deposit: ${transaction}")
        else:
            print(f"  Withdrawal: ${transaction}")
    
    # calculate new balance
    for transaction in transactions:
        balance += transaction
    
    print(f"\nUpdated balance: ${round(balance, 2)}")

else:
    print("Account locked. Too many wrong attempts.")
