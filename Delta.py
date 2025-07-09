# print('Hello World')
# Variable
# print('JIGGY')
# full_name = input('Enter your fullname: ')
# age = int(input('How old are you: '))
# height = 5.6
# is_available = True
# print(f'I am {full_name}, I am {age} years old and I am {height} tall.')  

# print('Addition', a + b)
# print('Subtraction', a + b)
# print('Multiplication', a + b)
# print('Modulus', a % b)
# print('Exponentiation', a ** b)
# print('Floor Division', a // b)
# # COMPARISON
# print('EQUAL', a == b)
# print('Not Equal', a != b)
# print('Greater Than', a > b)
# print('Greater Than or equal', a >= b)
# print('less Than', a < b)

# Inbuilt features and keywords that cant be use to name variable = with, in, for, def, else, elif, or while,try,except, import,class, from,finally, and, return
# Inbuilt functions - print()
# inbuilt classes - int(),str(),float(),bool()

# a_string = input('What do you want to write: ')
# print('output: ',a_string)

# first_number = input('Give me the first whole number: ')
# second_number = input('Give me the second whole number: ')
# print('Add..........')
# addition = float (first_number) + float(second_number)
# print(f'The total sum is {addition}')

# '''== equal to 
# > greaterthan
# < lessthan
# >= greater than or equal to 
# <= less than or equal to 
# !=  not equal to '''

# num = 3
# num2 = 4
# compare = num <= num2
# print(compare)

# val = 1
# ano_val = 1

# compare = val and ano_val

# compare1 = (4 == 4) and (3 != 2) and ('Telma' == 'telma') # '''all of them must be true for it'''
# compare2 = (2 > 4) or (9 < 6) # '''just needs one true comparison to be true'''

# print(compare2)
# bool = 4 > 2
# compare = not bool  #look for what is false

# print(50 + 25 - 10)

# num = 7 >= 5
# print(num)

# name = 'BANKOLE'
# print(name[1])
# can_enter = False
# print(not can_enter)


# name = input('Enter your name: ').strip().title()
# print(name) 

# destination = ['Abuja','Lagos','Port Harcourt']
# option = input('1. Add a destination \n 2. Delete a Destination.\n3.')


# registeredflights = ['Abuja','Enugu','Asaba']
# print('Welcome to Ridadh Airways')
# options = input('Ente your state of preference: ')

# if options == 1:
#     yourways = input('Enter the preferred state: ')
#     print(yourways)
#     if yourways in registeredflights:
#         print(
#             'Yours flight is successful'
#         ) 
#     else:
#         print('Otilor')
# else:
#     print('No option was selected')




# while True:
#     x = int(input('What is x ? '))
#     if 90<= x >= 80 :
#         print('SCORED A')
#     elif 70<= x >= 60 :
#         print('Scored B')
#     elif 50<= x >= 40 :  
#         print('scored C') 
#     else:
#         print('U HAVE TO RESIT') 

# while True:
#     x = int(input('Enter a number: '))
#     op = input('Enter your operator: ')
#     y = int(input('Enter a number: '))
 
#     if op == '+' :
#         print(f'THE RESULT:{x+y} ')
#     elif op == '-':
#         print(f'THE RESULT:{x-y} ')
#     elif op == '*':
#         print(f'THE RESULT:{x*y} ')
#     elif op == '/' :
#         print(f'THE RESULT:{x/y} ')
#     elif op == '//' :
#         print(f'THE RESULT: {x//y} ')
#     else:
#         print('You have NOT ENTER A NUMBER')


# while True:
#     x = int(input('Enter a number: '))
#     if x % 2 == 0:
#         print('Its an even number')
#     else:
#         print('Its an odd number')

# i = int(input('Enter a number: '))
# while i != 0:
#     i = i - 1
#     print('MEOW')
    
# firstName = 'Miracle'
# lastName = 'King'
# user = firstName + lastName + '@gmail.com'
# sentence = 'I need the name Sarah Ade to be joined to sarahade@gmail.com'
# new_sentence=sentence.replace('Sarah',firstName).replace('Ade',lastName).replace('sarahade@gmail.com',user.lower())
# print(new_sentence)
# print(new_sentence[::-1])

# fruit = ['apple','banana','carrot','kiwi']
# for longest in fruit:
#     if len(longest) < len(fruit):
#         longest = fruit
#     else:
#         print(longest)
# longest_string = max(go,key=len)
# print(longest_string)


# sentence = 'I need the name Sarah Ade to be joined to sarahade@gmail.com'
# # print(sentence.count(' '))

# num = 0
# for char in sentence:
#     if char == ' ':
#         num += 1
#     else:
#         print(num)

# def greetings(name,age):
#     print(f'welcome {name} and U are {age} years old')

# name = input('Enter Ur name: ')
# age = int(input('How old are you: '))
# greetings(name,age)

def num(num1, num2):
    return num1 + num2


num1 = int(input('Enter a number: '))
num2 = int(input('Enter second number: '))
print(num(num1,num2  ))


