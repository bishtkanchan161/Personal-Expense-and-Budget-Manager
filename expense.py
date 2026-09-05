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


date = input("Enter the Date: ")
amount = float(input("Enter the Amount: "))
category = input("Enter the Category: ")
description = input("Enter the Description: ")

exp = Expense(date, amount, category, description)

exp.display_expenses()