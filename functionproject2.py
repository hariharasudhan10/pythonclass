account = {"hari": 1000, "sridhar": 3000}

def deposit(name, amount):
    if name in account:
        if amount > 0:
            account[name] += amount
            balance=account[name]
            print("The remaining balance is",balance)
        else:
            print("Deposit amount should be greater than 0.")
    else:
        print("Account does not exist.")
def withdraw(name, amount):
    if name in account:
        if amount > 0:
            if amount > account[name]:
                print("Insufficient funds!")
            else:
                account[name] -= amount
                balance=account[name]
                print("The remaining balance is:",balance)
        else:
            print("Withdrawal amount should be greater than 0.")
    else:
        print("Account does not exist")
def balance(name):
    if name in account:
        print("The balance is:",account[name])
    else:
        print("Account does not exist.")
def getamount():
    name = input("Enter your name: ")
    if name not in account:
        print("Account does not exist!")
    else:    
        print("1. Deposit, 2. Withdraw, 3. Balance")
        choice = int(input("Enter your option: "))
    if choice == 1:
        amount = int(input("Enter your deposit amount: "))
        deposit(name, amount)
    elif choice == 2:
        amount = int(input("Enter your withdrawal amount: "))
        withdraw(name, amount)
    elif choice == 3:
        balance(name)
    else:
        print("Invalid choice!")
getamount()