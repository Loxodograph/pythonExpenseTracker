import json

class Expense:
  def __init__(self, category, amount, note=""):
    self.category = category
    self.amount = amount
    self.note = note
  
  def __str__(self):
    dictionary = {"Category": self.category, "Amount": self.amount, "Note": self.note}
    return str(dictionary)
  
class ExpenseTracker:
  def __init__(self):
    self.listOfExpenses = []
    self.collection = []
    
  def add_expense(self, expense):
    self.collection.append(expense)
    self.listOfExpenses.append(expense.__str__()) 
    
  def calculate_totals(self):
    total = 0
    for i in range(len(self.collection)):
      total += int(self.collection[i].amount)
    return total
    
  def save_to_JSON(self):
    try:
      with open("expenses.json", "w") as json_file:
        json.dump(self.listOfExpenses, json_file, indent=4)
      print(f'Sucessfully saved the expenses')
    except IOError as e:
      print(f"Error saving file: {e}")
  
  def load_JSON(self):
    with open("expenses.json", 'r') as json_file:
      self.listOfExpenses = json.load(json_file)
  
  def create_expense(self):
    expense_category = input("Category: ")
    expense_amount = input("Amount: ")
    expense_note = input("Note (optional): ")
    created_expense = Expense(expense_category, expense_amount, expense_note)
    self.add_expense(created_expense)
    
  
new_expense = Expense("Food", 25.00, "Lunch")
new_expense_2 = Expense("Internet", 175, "ISP")

tracker = ExpenseTracker()

tracker.create_expense()
tracker.create_expense()

tracker.save_to_JSON()
total = tracker.calculate_totals()
print(f"total {total}")

# tracker.add_expense(new_expense)
# tracker.add_expense(new_expense_2)

# print(tracker.listOfExpenses)
# tracker.load_JSON()
# print("Loaded JSON")
# print(tracker.listOfExpenses)