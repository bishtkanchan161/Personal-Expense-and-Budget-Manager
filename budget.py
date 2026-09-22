from expense import Expense

import pandas as pd
from datetime import datetime
class Budget:
    def __init__(self, income=0, budget=0):
        self.income=income
        self.budget=budget
        self.remaining_budget=budget
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
        self.remaining_budget=budget
        print("Your total budget is:",self.budget)

    
    def get_total_expenses(self):
        df = self.create_dataframe()
        total_expenses = df["Amount"].sum()
        return total_expenses
    
    def update_budget(self):
        print("A. Add amount in remaining budget")
        print("B. Increase total budget")
        choice= input("Enter your choice:")
        if choice == "A":
            add_amount=float(input("Enter amount to add in remaining budget:"))
            self.remaining_budget= self.remaining_budget+add_amount
            print("Amount added:",add_amount)
            print("Your updated remaining budget is:", self.remaining_budget)

        elif choice=="B":
            add_amount=float(input("Enter amount to increase in budget:"))
            self.budget=self.budget+add_amount
            self.remaining_budget=self.remaining_budget+add_amount
            print("Amount added:",add_amount)
            print("Your updated total budget is:", self.budget)
            print("Your updated remaining budget is:", self.remaining_budget)
        else:
            print("Invalid Choice.")
            
                
    def create_dataframe(self):
        data=[]
        for exp in self.expenses:
            data.append({
                "Date":exp.date,
                "Amount":exp.amount,
                "Category":exp.category,
                "Description":exp.description
            })
        df=pd.DataFrame(data)
        return df
    def validate_date(self):

        while True:
            date = input("Enter the Date (DD/MM/YYYY): ")

            try:
                datetime.strptime(date, "%d/%m/%Y")
                return date

            except ValueError:
                print("Invalid date. Please enter date in DD/MM/YYYY format.")
    
         
       
    def menu(self):
        while True:
            user_input=input('''
        1. Press 1 for set income
        2. Press 2 for set budget
        3. Press 3 for update monthly income
        4. Press 4 for update monthly budget
        5. Press 5 for add expenses
        6. Press 6 for show all expenses Details
        7. Press 7 for show expenses analysis
        8. Press 8 for show remainig budget
        
       
        9. Press 9 for exist
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
                if self.income<=0 or self.budget<=0:
                    print("Please set your income and budget first.")
                    continue
                date = self.validate_date()
                amount = float(input("Enter the Amount: "))
                category = input("Enter the Category: ")
                description = input("Enter the Description: ")

                exp = Expense(date, amount, category, description)
                
                self.expenses.append(exp)
                self.remaining_budget=self.remaining_budget-amount
                
                exp.display_expenses()
            elif user_input=="6":
                df=self.create_dataframe()
                print(df)
            
            elif user_input=="7":
                df=self.create_dataframe()
                total_expenses=self.get_total_expenses()
                print("Total Expenses is:",total_expenses)

                average_expenses=df["Amount"].mean()
                print("Average of Expenses is:",average_expenses)

                max_expense=df["Amount"].max()
                print("Maximum Expense is:",max_expense)

                min_expense=df["Amount"].min()
                print("Minimum Expense is:",min_expense)


            elif user_input=="8":
                print("Remaining Budget is:", self.remaining_budget)
               
            elif user_input=="9":
                print("program exited")
                break
           
            else:
                print("Invalid choice.")
               

obj=Budget()
obj.menu()




