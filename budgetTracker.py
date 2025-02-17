
def add_expense(expenses, expenses_description, amount):
    expenses.append({'description': expenses_description, 
                    'amount':amount})

def get_total_expenses(expenses):
    total_expenses = 0
    for expense in expenses:
        total_expenses += expense['amount']
        return total_expenses
def remaining_budget(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"The total budget is: {budget}$")
    print("Expenses are: ") 
    for expense in expenses: 
        print(f"expense description: {expense['description']} \n Amount: {expense['amount']}") 
    print(f"Total sepnt: {get_total_expenses(expenses)}$")
    print(f"Remaining budget: {remaining_budget(budget,expenses)}")

def main():
    print('\nWelcome to the Budget Tracker!')
    initial_budget = float(input("Please enter your monthly Budget: "))

    budget = initial_budget
    expenses = []
    while True:
        print("What would you like to do? \n")
        print("1.Add an expense.\n2.Show budget details.\n3.Exit\n")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            expenses_description = input("Wnter expense Description:")
            amount = float(input("Enter expense amount: "))
            print(f"Added expense: {expenses_description}, Amount: {amount}$")
            add_expense(expenses, expenses_description, amount)

        elif choice =='2':
            print("Here are your budget details: \n")
            show_budget_details(budget, expenses)
        
        elif choice == '3':
            print("Exiting the Budget App. Thank you!\n")
            break

        else:
            print("Invalid choice, please enter  a valid choice (1/2/3): ")



if __name__ == '__main__':
    main()