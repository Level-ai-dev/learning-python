# Repeat a block of code untill a condition is meet

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for item in list:
#     print(item)
#     if item == 8:
#         print('8 is in here store the loop')
#         break

# menu = ['Beans','Plantain','Rice','Pasta','Macaroni','Mashed Potato','Afang Soup','Salad']
# order_food = input('Hello. What do you want to order: ')

# for dish in menu:
#     if order_food == dish:
#         print(f'Here is your {dish}, that would be 1,000 naira:')
#         break
#     else:
#         print('You have not made an order.')


# menu = ['Beans','Plantain','Rice','Pasta','Macaroni','Mashed Potato','Afang Soup','Salad']      
# new_menu = [
#     {
#         'name': 'Beans',
#         'price': 2000
#     },
#     {
#         'name': 'Rice',
#         'price': 5000
#     },
#     {
#         'name': 'Pasta',
#         'price': 3000
#     },
# ]

# order_food = input('Hello. What do you want to order: ')

# for dish in new_menu:
#     if order_food == dish['name']:
#         print(f'Here is your {dish["name"]}, that would be {dish['price']} naira')
#         break
#     else:
#         print('You have not made an order.')


# store = []

# for obj in store:
#     print(len(store))
#     if len(store) < 5: 
#         obj = input('What do you want to add: ')
#         store.append(obj)
#         print(store)
#     else:
#         print('You have reacted the maximum length of objects to add')
        # break


# num = 0

# while num < 10:
#     num = num + 1
#     print('Keep running', num)

# num = 20
# while True:
#     guess = int(input('Guess the number: '))
#     if guess > num and guess <= 25:
#         print('You are too close')
#     elif guess > num:
#         print('Number is greater than the guess number')
#     elif guess < num and guess >= 15:
#         print('Almost there. Dont give up')
#     elif guess == num:
#         print(f'Hurray, you have found the number. The number is {num}')
#         break
#     else:
#         print('Number is lesser than the guess number')

# expenses = [
#     ['Transportatio', 85000]
#     ['Food', 200000]
# ]



# while True:
#     option = input('1. Add expense \n 2View ')
#     if option == '1':
#         print('Option 1')
#     elif option == '2':
#         print('Option 2')
#     elif option == '3':
#         print('Leaving the expense tracker.')
#         break
#     else:
#         print('Invalid option. Write a number option above.')

# database = [
#     {
#         'name': 'Pasta',
#         'price': 3000
#     },
# ]


# while True:
#     option = input('1.Sign-up\n2.Login\n3.Exits' )
#     if option == '1':
#         username = input('Enter User name: ')
#         user_pin = int(input('Enter Ur Pin: '))
#         sign_up = username and user_pin
#         print(sign_up)
#     elif option == '2':
#         username_1 = username = input('Enter User name')
#         user_pin_1 = int(input('Enter Ur Pin'))
#         if username == username_1 and user_pin == user_pin_1:
#             print('LOGIN SUCCESSULLY')
#         else:
#             print('Invalid DETAILS')
#     elif option == '3':
#         print('Thanks for Banking With US')
#         break
#     else:
#         print('Invalid')
        

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

