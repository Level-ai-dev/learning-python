
transactions = []
balance = 0
pin = 1234
print(f'{'--' * 5}WELCOME TO MASH BANK {'--' * 5}')
user_pin = int(input('ENTER YOUR FOUR DIGIT PIN NUMBER: '))

while True:
    if user_pin == pin:
        print('LOGGED IN SUCCESSFULLY')
    else:
        print('INVALID PIN')
        break
    option = input(
        """1. Check Balance
2. Deposit
3. Withdraw
4. Check History
5. Exit
MAKE A SELECTION: """)
    if option == '1':
        print(f'YOUR CURRENT BALANCE IS ${balance}')
    elif option == '2':
        deposit = float(input('HOW MUCH WILL YOU LIKE TO DEPOSIT: '))
        balance = balance + deposit
        message = f'YOU HAVE DEPOSITED ${deposit} SUCCESSFULLY'
        transactions.append(message)
        print(message)
    elif option == '3':
        withdraw = float(input('HOW MUCH WILL YOU LIKE TO WITHDRAW: '))      
        if balance < withdraw:
            print('INSUFFICIENT BALANCE')
        else:
            balance = balance - withdraw
            message = f'${withdraw} WITHDRAWAL SUCCESSFUL\nNEW BALANCE IS ${balance}'
            transactions.append(message)
            print(message)
    elif option == '4':
        print('\n'.join(transactions))
    elif option == '5':
        print('THANKS FOR BANKING WITH US!')
        break
    else:
        print('INVALID INPUT')





