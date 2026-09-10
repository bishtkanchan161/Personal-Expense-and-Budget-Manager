from expense import Expense
import numpy as np
import pandas as pd
class Budget:
    def __init__(self, income=0, budget=0):
        self.income=income
        self.budget=budget
        self.expenses=[]
    def set_income(self):
        income= float(input("enter your income:"))

        self.income=income
        print("Your income is:",self.income)

    def update_income(self):
            new_income= float(input("enter your  new monthly income:"))
            self.new_income=new_income
            print("Your new monthly income is:",self.new_income)
        
    def set_budget(self):
        budget=float(input("enter your budget: "))
        self.budget=budget
        print("Your total budget is:",self.budget)

    def update_budget(self):
            new_budget= float(input("enter your  new monthly budget:"))
            self.new_budget=new_budget
            print("Your new total budget is:",self.new_budget)
       
    def menu(self):
        while True:
            user_input=input('''
        1. Press 1 for set income
        2. Press 2 for set budget
        3. Press 3 for update monthly income
        4. Press 4 for update monthly budget
        5. Press 5 for add expenses
        6. Press 6 for show all expenses Details
        
       
        6. Press 7 for exist
        ''' )
            print("Your choice is:", user_input)
            if user_input=="1":
                self.set_income()
            elif user_input=="2":
                self.set_budget()

            elif user_input=="3":
                self.update_income()
            elif user_input=="4":
                self.update_budget()
            elif user_input=="5":
                date = input("Enter the Date: ")
                amount = float(input("Enter the Amount: "))
                category = input("Enter the Category: ")
                description = input("Enter the Description: ")

                exp = Expense(date, amount, category, description)
                
                self.expenses.append(exp)
                
                exp.display_expenses()
            elif user_input=="6":
                data=[]
                for exp in self.expenses:
                     data.append({
                     "Date":exp.date,
                     "Amount":exp.amount,
                     "Category":exp.category,
                     "Description":exp.description
                })
                df=pd.DataFrame(data)
            
                print(df)
               
            
           
            else:
                break

obj=Budget()
obj.menu()




