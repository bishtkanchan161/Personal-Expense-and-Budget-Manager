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
        while True:

            try:
                income = float(input("Enter your income: "))

                if income <= 0:
                    print("Income must be greater than zero.")
                    continue

                self.income = income

                print("Your income is:", self.income)

                break

            except ValueError:

                print("Invalid income! Please enter a number.") 
       
    def update_income(self):
        while True:
            try:
                income= float(input("enter your income:"))
                if income<=0:
                    print("Income must be greater than Zero.")
                    continue
                self.income=income
                print("Your income is:",self.income)
                break
            except ValueError:
                print("Invalid income! Please enter a number.")
           
    def set_budget(self):
       
        while True:

            try:
                budget = float(input("Enter your budget: "))

                if budget <= 0:
                    print("Budget must be greater than zero.")
                    continue
                if budget>self.income:
                    print("Budget cannot be greater than your income.")
                    print("Your income is:", self.income)
                    continue 

                self.budget = budget
                self.remaining_budget = budget

                print(
                    "Your total budget is:",
                    self.budget
                )

                break

            except ValueError:

                print("Invalid budget! Please enter a number.")
    
    def get_total_expenses(self):
        df = self.create_dataframe()
        total_expenses = df["Amount"].sum()
        return total_expenses
    
    def update_budget(self):
        print("A. Add amount in remaining budget")
        print("B. Increase total budget")
        choice= input("Enter your choice:")
        if choice == "A":
             while True:
                try:
                    add_amount = float(input("Enter amount to add in remaining budget: "))
                    if add_amount <= 0:
                        print( "Amount must be greater than zero.")
                        continue

                    self.remaining_budget += add_amount

                    print("Amount added:",add_amount)
                    
                    print("Your updated remaining budget is:",self.remaining_budget)
                    break

                except ValueError:

                    print("Invalid amount! Please enter a number.")
                    
        elif choice == "B":
            while True:
                try:
                    add_amount = float(input("Enter amount to increase in budget: "))
                        
                    if add_amount <= 0:
                        print(
                            "Amount must be greater than zero.")
                        continue
                    new_budget=self.budget + add_amount
                    if new_budget > self.income:
                        print("Budget cannot be greater than your income.")
                        print("Your current income is:", self.income)
                        print("Your current budget is:", self.budget)
                        continue

                    self.budget=new_budget
                    self.remaining_budget += add_amount

                    print("Amount added:",add_amount)
                    print("Your updated total budget is:",self.budget)
                    print("Your updated remaining budget is:",self.remaining_budget)
                    break

                except ValueError:

                    print("Invalid amount! Please enter a number.")
        else:

            print("Invalid Choice.")          
            
                
    def create_dataframe(self):
        data=[]
        for exp in self.expenses:
            data.append({
                "Expenses_ID":exp.expense_id,
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
    def validate_amount(self):

        while True:

            amount = input( "Enter the Amount: ")

            try:
                amount = float(amount)

                if amount <= 0:

                    print("Amount must be greater than zero.")
                    continue

                return amount

            except ValueError:

                print("Invalid amount!")
                

                print("Please enter a valid number.")

    def validate_text(self, message):

        while True:

            value = input(message).strip()

            if value:

                return value

            print("This field cannot be empty.")
                       
         
       
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
                expense_id = len(self.expenses) + 1
                date = self.validate_date()
                amount = self.validate_amount()
                category = self.validate_text("Enter the Category:")
                description = self.validate_text("Enter the Description: ")

                while True:

                    print("\n========== EXPENSE DETAILS ==========")
                    print("Expense ID:", expense_id)
                    print("Date:", date)
                    print("Amount:", amount)
                    print("Category:", category)
                    print("Description:", description)
                    print("=====================================")

                    print("\n1. Save Expense")
                    print("2. Edit Expense")
                    print("3. Cancel")

                    choice = input("Enter your choice: ")

                    if choice == "1":

                        exp = Expense(expense_id,date,amount,category,description)
                        self.expenses.append(exp)

                        self.remaining_budget -= amount

                        print("\nExpense added successfully!")
                        exp.display_expenses()

                        break

                    elif choice == "2":

                        while True:

                            print("\nWhat do you want to edit?")
                            print("1. Date")
                            print("2. Amount")
                            print("3. Category")
                            print("4. Description")
                            print("5. Back")

                            edit_choice = input("Enter your choice: ")

                            if edit_choice == "1":
                                date = self.validate_date()
                            elif edit_choice == "2":
                                amount = self.validate_amount()

                            elif edit_choice == "3":
                                category = self.validate_text("Enter the new Category: ")

                            elif edit_choice == "4":
                                description = self.validate_text("Enter the new Description: ")

                            elif edit_choice == "5":
                                break

                            else:
                                print("Invalid choice!")

                    elif choice == "3":

                        print("Expense cancelled.")
                        break

                    else:
                        print("Invalid choice!")

            elif user_input == "6":

                df =self.create_dataframe()

                if df.empty:
                    print("No expenses available.")
                else:
                    print("\n========== ALL EXPENSES ==========")
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




