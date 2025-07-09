# test_score = float(input('Enter you test score: '))
# exam_score = float(input('Enter your exam score: '))
# total_score = test_score + exam_score

# if total_score > 70:
#     print('A')
# elif 60 <= total_score < 70:
#     print('B')
# elif 50 <= total_score < 60:
#     print('C')
# elif 45 <= total_score < 50:
#     print('E')
# else:
#     print('REPEAT CLASS') 

# person = {
#     'name' : 'Ola',
#     'age': 100,
#     'nationality' : 'Togo',
#     'gender': 'MALE',
#     'religion' : 'Islam',
#     'extra_details': {
#         'nin': 747957575,
#         'date_of_birth': '14 APRIL 1999',
#         'BVN': 56464488646
#     }

# }

# person['name'] = 'segun'
# person['height'] = 1.75
# print(person['age'])

# a ={}
# a['key'] = 1
# a['age'] = 20

# print('second: ',a)
# # deleting a key 
# del a['age']

# print('Third: ', a)

# # clear evey value
# a.clear()

# print('Fouth: ', a)

# collection = ['Abel','Kane',12, 114.3, True,[1, 'tame',14,['Tomi', 42]]]

# # print(collection[4:6])
# # collection.insert() #Add a value to a specifit index
# # collection.pop() # Takes out value by writing out the value
# # collection.remove() # take out a value by writting out the value
# # collection[0] = 'Liverpool' # update a value

# #membership
#in - boolean
# check = 'Arsenal' in collection

# #concatination
# concat_list = [1,2,3,4,5] + [6,7,8,9,0]
# print(concat_list)

# #Repitition
# item = ['hi']
# repeat_item = item * 4
# print(repeat_item)


# #length
# print(len(concat_list))

# numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# numbers.append(16)
# numbers.insert(3,17)
# print(numbers)
# # slice_items_in_list = numbers[-4:]

# # print(slice_items_in_list)


destinations = ["abuja", "lagos", "port harcourt"]

options = input("1. Add a destination\n2. Delete a destination.\n3. View destinations.\n4. Update a destination.")

if options == "1":
    choice = input("What destination do you want to add?: ")
    destinations.append(choice)
    print(destinations)
elif options == "2":
    choice = input("What destination do do you want to remove?: ")
    destinations.remove(choice)
    print(destinations)
elif options == "3":
    print(destinations)
elif options == "4":
    choice = input("What destination do do you want to update?(index destination): ")
    to_list = choice.split()
    destinations[int(to_list[0])] = to_list[1]
    print(destinations)
else:
    print("No option was added")