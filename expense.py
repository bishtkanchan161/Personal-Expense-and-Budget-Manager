class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def display_expenses(self):
        print("Date:", self.date)
        print("Amount:", self.amount)
        print("Category:", self.category)
        print("Description:", self.description)
       




