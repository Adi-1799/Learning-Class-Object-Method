from expense import ExpenseTracker

name = input("Enter your name: ")
user = ExpenseTracker(name)   # object created
# An object is a real instance created from a class


while True:
    print("\n1. Add expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Enter amount: ₹"))
        user.add_expense(amount)   # method call

    elif choice == "2":
        user.show_expenses()

    elif choice == "3":
        user.total()

    elif choice == "4":
        break

    else:
        print("Invalid Input!")
        continue
