import csv
import os
from datetime import datetime

data_file = "expenses.csv"

def initialize_file():
    if not os.path.exists(data_file):
        with open(data_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Transport, Entertainment, etc.): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")
    
    with open(data_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    
    print("Expense added successfully!\n")

def view_expenses():
    print("\nYour Expenses:")
    with open(data_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))
    print("\n")

def expense_summary():
    categories = {}
    
    with open(data_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            category, amount = row[1], float(row[3])
            categories[category] = categories.get(category, 0) + amount
    
    print("\nExpense Summary:")
    for category, total in categories.items():
        print(f"{category}: ${total:.2f}")
    print("\n")

def main():
    initialize_file()
    
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()