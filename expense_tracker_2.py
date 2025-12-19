import json

expense_json = "expenses.json"

class Expense:
  def __init__(self, category, amount, note=""):
    self.category = category
    self.amount = amount
    self.note = note
  
  def to_dict(self):
    return {"Category": self.category, "Amount": self.amount, "Note": self.note}
    
    # This is the reverse of to_dict; converts the dictionary back to an Expense object.
  @classmethod
  def from_dict(cls, data):
    return cls(data['Category'], data['Amount'], data['Note'])
    

  # Format as human readable string
  def to_str(self):
    return f'Category: {self.category}\nAmount: {self.amount}\nNote: {self.note}'
  
  # Return price
  def get_price(self):
    return float(self.amount)  
  
class ExpenseTracker:
  def __init__(self):
    self.list_of_expenses = []
    self.collection = []
  
  #add expense to collection and dictionary
  def add_expense(self, expense):
    self.collection.append(expense)
    self.list_of_expenses.append(expense.to_dict())  # Save as dictionary
  
  #Calculate total  
  def calculate_totals(self):
    total = 0
    for expense in self.collection:
        total += expense.get_price()  # Get price using Expense object method
    return total
  
  #Save to JSON file expenses.json  
  def save_to_JSON(self):
    try:
      with open(expense_json, "w") as json_file:
        json.dump(self.list_of_expenses, json_file, indent=4)
      print(f'Sucessfully saved the expenses')
    except IOError as e:
      print(f"Error saving file: {e}")
  
  # Load JSON Object
  def load_JSON(self):
    try:
        with open(expense_json, 'r') as json_file:
            loaded_expenses = json.load(json_file)  # Should be a list of dictionaries
            self.list_of_expenses = loaded_expenses
            self.collection = [Expense.from_dict(expense) for expense in loaded_expenses]  # Convert dictionaries to objects
            print("Expenses Loaded")
    except FileNotFoundError:
        print("No previous data found, starting fresh.")
    except json.JSONDecodeError:
        print("Error decoding JSON data. Please check the file format.")
            
  def clear_tracker(self):
    self.list_of_expenses = []
    self.collection = []
  
  #Create Expense object using user input
  def create_expense(self):
    expense_category = self.define_category()
    expense_amount = self.define_amount()
    expense_note = input("Note (optional): ")
    created_expense = Expense(expense_category, expense_amount, expense_note)
    self.add_expense(created_expense)
  
  #Validate and define category 
  def define_category(self):
    while True:
      user_input = input("Category: ")
      if len(user_input) > 0:
        break
      else:
        print("Invalid input! Category is a required field.")
    return user_input
  
  #validate and define amount        
  def define_amount(self):
    while True:
      expense_input = input("Amount: ")
      try:
        expense_amount = float(expense_input)
        break
      except ValueError:
        print("Invalid Input. Please enter a valid number")
    return expense_input
   
  #Display expenses and Total  
  def display_expenses(self):
    for expense in self.collection:
      print(expense.to_str())
    print(f"Total: ${self.calculate_totals()}")
    
def main():
  tracker = ExpenseTracker()
  greeting()
  
  #Main loop
  while True:
    user_choice = display_menu()
    if user_choice == '1':
      tracker.create_expense()
    elif user_choice == '2':
      tracker.display_expenses()
    elif user_choice == '3':
      tracker.clear_tracker()
    elif user_choice == '4':
      tracker.save_to_JSON()
    elif user_choice == '5':
      tracker.clear_tracker()
      tracker.load_JSON()
    elif user_choice == "6":
      break

def greeting():
  print("Welcome to Expense Tracker")
  print("--------------------------")
  
def display_menu():
  # print("Make a Selection")
  print("Press 1. To Add Expense")
  print("Press 2. To Review Expenses")
  print("Press 3. To Clear Expenses")
  print("Press 4. Save Expenses")
  print("Press 5. To Load Expenses")
  print("Press 6. To Exit")
  user_choice = input("Make a Choice: ")
  return user_choice

main()


# Create Expense object which takes a category, a price, and an optional note
  #Methods
    #To JSON String
    #To Human Readable String
    #Return Price

# Create ExpenseTracker object which has methods:
  # Add Expense
  # Create Expense Object
    # Validate Name Input
    # Validate Number Input
  # Display Expenses
  # Calculate Total
  # Save to JSON
  # Load From JSON
  # Clear Tracker
  