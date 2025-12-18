expenses = {}
budget = None

# Function to add expenses to the dictionary
def add_expenses(dictionary):
    print("Add expense:")
    expense_name = input("Category: ")
    expense_amount = float(input("Amount: "))
    if dictionary.get(expense_name):
      dictionary[expense_name] += expense_amount
    else:
      dictionary[expense_name] = expense_amount

# Greeting function
def greeting():
    print("Welcome to Expense Tracker!")
    print("----------------------------")

# Function to set budget
def set_budget(): 
    global budget
    budget = float(input("Set your budget: "))
    print(f"Budget set to: {budget}")
  
# Function to calculate total expenses   
def calculate_total_expenses(dictionary):
    return sum(dictionary.values())
  
def display_expenses(dictionary):
    print("Current Expenses:")
    for category, amount in dictionary.items():
        print(f"{category}: {amount}")


greeting()
set_budget()
add_expenses(expenses)
print(expenses)
print(f"Budget: {budget}")
total_expenses = calculate_total_expenses(expenses)
display_expenses(expenses)
print(f"Total Expenses: {total_expenses}")
budget -= total_expenses
print(f"Remaining Budget: {budget}")