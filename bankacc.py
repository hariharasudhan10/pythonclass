accounts = {'hari': 5000,  'sridhar': 3000}
print("Choose an account:")
user_choice = input("Enter account : ")
if user_choice in accounts:
  
    print("\nChoose an action:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    choice = input("Enter the method : ")
    if choice == '1':  
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            accounts[user_choice] += amount
            balance=float(accounts[user_choice])
            print(" the avalaiable balance is", balance)
        else:
            print("The amount should be greater than 0.")
    
    elif choice == '2':  
        amount = int(input("Enter withdraw amount: "))
        if amount>0:
            
            if amount > accounts[user_choice]:
                print("Insufficient funds!")
            else:
                accounts[user_choice] -= amount
                balance=float(accounts[user_choice])
                print("the remainig balance is",balance)
           
        else:
            print("Withdrawal amount should be greater than 0.")
    
    elif choice == '3' : 
            print("your balance is",accounts[user_choice])
    
   
else:
    print("Invalid choice.")


    



