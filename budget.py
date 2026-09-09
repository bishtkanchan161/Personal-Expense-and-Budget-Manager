from expense import Expense
import numpy as np
class Budget:
    def __init__(self, income=0, budget=0):
        self.income=income
        self.budget=budget
    def set_income(self):
        income= float(input("enter your income:"))

        self.income=income
        print("Your income is:",self.income)
        
    def set_budget(self):
        budget=float(input("enter your budget: "))
        self.budget=budget
        print("Your budget is:",self.budget)
       
    def menu(self):
        while True:
            user_input=input('''
        1. Press 1 for set income
        2. Press 2 for set budget
        3. Press 3 for expenses
        4. Press 4 for exist
        ''' )
            print("Your choice is:", user_input)
            if user_input=="1":
                self.set_income()
            elif user_input=="2":
                self.set_budget()
            elif user_input=="3":
                date = input("Enter the Date: ")
                amount = float(input("Enter the Amount: "))
                category = input("Enter the Category: ")
                description = input("Enter the Description: ")

                exp = Expense(date, amount, category, description)
                exp.display_expenses()
            else:
                break

obj=Budget()
obj.menu()




