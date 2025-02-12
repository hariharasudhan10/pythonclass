def displayresult(c,result):
    print(f"the result of {c},{result}")
a=float(input("enter the a value"))
b=float(input("enter the b value "))
print("\n select the method of user:")
print("1.addition")
print("2.subraction")
print("3.multiplication")
print("4.division")
choice=input("enter the method")
if choice == "1":
    result = a + b
    displayresult("addition", result)
elif choice == "2":
    result = a - b
    displayresult("subtraction", result)
elif choice == "3":
    result = a * b
    displayresult("multiplication", result)
elif choice == "4":
    if b != 0:
        result  = a / b
        displayresult("division", result)
    else:
        print("Error:")
else:
    print("Invalid choice")
