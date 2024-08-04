# this is the main function of the code for this assignment.
# the tasks are all in the budget_category module and are to be imported

from budget_category import BudgetCategory

def main():
    categories = {}

    while True:
        print("\nPersonal Budget Management")
        print("1. Add Budget Category")
        print("2. Add Expense")
        print("3. Display Budget Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category_name = input("Enter category name: ")
            allocated_budget = float(input("Enter allocated budget: "))
            categories[category_name] = BudgetCategory(category_name, allocated_budget)
            print(f"Category '{category_name}' added with a budget of {allocated_budget}.")

        elif choice == '2':
            category_name = input("Enter category name: ")
            if category_name in categories:
                amount = float(input("Enter expense amount: "))
                try:
                    categories[category_name].add_expense(amount)
                    print(f"Expense of {amount} added to category '{category_name}'.")
                except ValueError as e:
                    print(e)
            else:
                print(f"Category '{category_name}' does not exist.")

        elif choice == '3':
            category_name = input("Enter category name: ")
            if category_name in categories:
                categories[category_name].display_category_summary()
            else:
                print(f"Category '{category_name}' does not exist.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()