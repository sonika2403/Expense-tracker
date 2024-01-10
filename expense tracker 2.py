from collections import defaultdict
from datetime import datetime

expenses = defaultdict(list)
#defining the input module for noting the expenses which consist of description and category
def add_expense():
    amount = float(input("Enter amount spent: "))
    description = input("Enter brief description: ")
    category = input("Enter expense category: ")
    date = datetime.now().strftime("%Y-%m-%d")
    expenses[date].append({'amount': amount, 'description': description, 'category': category})

#defining the module to return the monthly expenditure of that particular year
def sum_monthly_summary(expenses, year, month):
    total_expense = 0
    target_month = f"{year:04d}-{month:02d}"

    for date, expense_list in expenses.items():
        if date.startswith(target_month):
            for expense in expense_list:
                total_expense += expense['amount']
                print(total_expense)
  

# To get current year and month
current_date = datetime.now()
current_year = current_date.year
current_month = current_date.month

# Calculate and print total expenses for the current month
total_monthly_expense = sum_monthly_summary(expenses, current_year, current_month)
print(f"Total expenses for {current_year}-{current_month:02d}: ${total_monthly_expense}")

#defining the module which returns the values of expenses which regards to category
def category_summary():
    category_expenses = defaultdict(float)
    for date, expense_list in expenses.items():
        for expense in expense_list:
            category_expenses[expense['category']] += expense['amount']
    print("Category-wise expenditure:")
    for category, amount in category_expenses.items():
        print(f"{category}: ${amount}")

#the input modules with conditional statements
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Monthly Summary")
    print("3. Category-wise Summary")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        sum_monthly_summary(expenses, current_year, current_month)
    elif choice == '3':
        category_summary()
    elif choice == '4':
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose again.")
