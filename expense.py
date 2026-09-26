class Expense:
    def __init__(self, expense_id, date, amount, category, description):
        self.expense_id=expense_id
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def display_expenses(self):
        print("Expense ID:", self.expense_id)
        print("Date:", self.date)
        print("Amount:", self.amount)
        print("Category:", self.category)
        print("Description:", self.description)

    def update_expense(self, date=None, amount=None, category=None, description=None):

        if date is not None:
            self.date=date
        if amount is not None:
            self.amount=amount
        if category is not None:
            self.category=category
        if description is not None:
            self.description=description
        
       




