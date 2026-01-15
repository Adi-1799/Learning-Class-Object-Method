class ExpenseTracker:
    # A class is a blueprint that defines what data and actions an object will have

    """
    This class represents ONE person's expense tracker.
    """

    # Class variable → shared by all objects
    total_expenses_recorded = 0

    def __init__(self, name):
        # __init__ runs when an object is created and sets its initial values

        # Data stored inside object
        self.name = name  # 'self.name' is an instance variable
        self.expenses = []  # list of numbers  # 'self.expense' is an instance variable

    def add_expense(self, amount):
        # A method is a function that belongs to a class and works on the object's data

        if amount <= 0:
            print("Invalid amount of expense!")

        elif amount > 0:
            # Method changes object data
            self.expenses.append(amount)
            ExpenseTracker.total_expenses_recorded += 1  # shared count
            print("Expense added")

    def show_expenses(self):
        print(f"\n{self.name}'s Expenses:")
        for i in self.expenses:
            print("₹", round(i, 2))

    def total(self):
        # Method reads object data
        print("Total spent: ₹", round(sum(self.expenses), 2))

    @classmethod
    def show_app_stats(cls):
        # A class method works on class variables
        print("\n--- App Stats ---")
        print("Total expenses recorded:", cls.total_expenses_recorded)
