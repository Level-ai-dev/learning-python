# print('WELCOME TO MASH RIDE')
# option = input('1. SIGN-UP USER  2. LOGIN-USE: ')
# user_name = ''
# user_password = ''
# if option == '1':
#     print('SIGN UP TO CREATE ACCOUNT')
#     user_name = input('Enter User name: ')
#     user_password = input('Enter your password: ')
#     print('SIGN-UP SUCCESSFULLY')

# elif option == '2':
#     user_name2 = input('Enter User-name: ')
#     user_password2 = input('Enter user password: ')
#     if user_name == user_name2 and user_password == user_password2:
#         print('LOGIN SUCCESSFULLY')
#     else:
#         print('NOT LOGGIN')
# else:
#     print('INVALID INPUT')

# def nain():
#     x = int(input('Enter a number: '))
#     print('X squared is', x ** 2)
# Example of ITERABLES: string, list, set, tuple
# nain()

unordered_values = {'LAGOS','Rivers','Abuja', 'Kogi'}
unordered_values_1 = {'Delta','Oyo','Lagos','Kogi','Sokoto'}
check_value_in_set = 'Rivers' in unordered_values
unordered_values.add('Zamfara')
unordered_values.remove('Abuja')
unordered_values.update(['Adamawa','Akwa ibom'])
merge = unordered_values.union(unordered_values_1)

intersect = unordered_values.intersection(unordered_values_1)
print(intersect)
#set doesnt have duplicate values inside a set
