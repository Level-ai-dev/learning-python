
expenses = [
    ['Transportation', 85000.00],
    ['Food', 200000.00]
]

while True:
    option = input('1. Add an expense.\n2. View Expenses.\n3. Show total expense. \n4. Exit \n(choose 1 - 3)')
    if option == '1':
        expenses = input('Write Your expenses: ')
        amount = input('Write the amount of the expense: ')
        expenses.append([expenses, float(amount)])
        print('Expense is successfully added')
    elif option == '2':
        for exp in expenses:
            print(f'{'--' * 21}\nExpense: {exp[0]}, amount: {exp[1]}\n{'--' * 21}')
    elif option == '3':
        total_amount = 0
        for exp in expenses:
            total_amount = total_amount + exp[1]
        else:
            if total_amount == 0:
                print(f'{'--' * 21}\nYou are broke. You need to work smart. Make connection.\n{'--' * 21}')
            print(f'{'--' * 21}\n Your total amount is {total_amount}.\n{'--' * 21}')
    elif option == '4':
        dell = expenses.remove(expenses[0])
        print(expenses)
    elif option == '5':
        choice = input('Are You sure you want to exist?(Yes|No): ')
        if choice == 'Yes':
            print(f'{'--' * 21}\nLeave the expense tracker.\n{'--' * 21}')
            break
        elif choice == 'No':
            continue
    else:
        print('Invalid option. Write a number option above.')

