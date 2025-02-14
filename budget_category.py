# Task 1

# this is the module for for all tasks within the module with the private attributes (category name, allocated budget, remaining budget)


class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget


# Task 2 

     # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, category_name):
        self.__category_name = category_name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
            self.__remaining_budget = allocated_budget
        else:
            raise ValueError("Budget must be a positive number")
        


# Task 3  

 # Method to add an expense
    def add_expense(self, amount):
        if amount > 0 and amount <= self.__remaining_budget:
            self.__remaining_budget -= amount
        else:
            raise ValueError("Invalid expense amount")


# Task 4

# Display Budget Details


    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
        print(f"Remaining Budget: {self.__remaining_budget}")

