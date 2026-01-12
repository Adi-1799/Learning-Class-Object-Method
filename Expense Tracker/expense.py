class ExpenseTracker:
    # A class is a blueprint that defines what data and actions an object will have

    """
    This class represents ONE person's expense tracker.
    """

    def __init__(self, name):
        # __init__ runs when an object is created and sets its initial values

        # Data stored inside object
        self.name = name
        self.expenses = []  # list of numbers

    def add_expense(self, amount):
        # A method is a function that belongs to a class and works on the object's data

        # Method changes object data
        self.expenses.append(amount)
        print("Expense added")

    def show_expenses(self):
        print("\nExpenses:")
        for i in self.expenses:
            print("₹", round(i, 2))

    def total(self):
        # Method reads object data
        print("Total spent: ₹", round(sum(self.expenses), 2))
