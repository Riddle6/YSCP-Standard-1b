'''
Step 1 - Input & Expense
'''
print("##############################")
print("#                            #")
print("# Welcome to Budget Tracker! #")
print("#                            #")
print("##############################\n")

# Ask the user if they are inputting an Expense or Income (1 For Income, 2 for Expense)
def income_or_expense():

    expense = 0
    income = 0
    amount = 0

    def processCash(income, expense):
        cash = income - expense
        print("Total Cash remaining: $","{:.2f}".format(cash))

    while True:
        category = int(input("\n\n\nAre you inputting an:\nIncome (1) or Expense (2)?\n\nTo quit, please enter (0): "))

        if category == 1:
            print("\nYou are inputting an income.")
            amount = float(input("Enter your income: "))
            
            income += amount


        elif category == 2:
            print("\nYou are inputting an expense.\n")
            amount = float(input("Enter your expense: "))
            expense += amount
            
            
        elif category == 0:
            
            
            processCash(income, expense)
            # Repeat the main menu
        
        else:
            print("\nInvalid Input. Perhaps you made a typo?\n")

    


income_or_expense()