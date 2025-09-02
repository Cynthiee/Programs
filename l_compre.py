# new_list = [expression for item in iterable if condition]

cars = ['Audi', 'Benz', 'BMW', 'Lexus', 'Venza', 'Cybertruck', 'Range Rover']

for i in cars:
    if 'R' in i:
        print(i)

new_cars = [i for i in cars if 'R' in i]
print(new_cars)

new_numbers = [i**2 for i in range(10) if i %2 == 0]
print(new_numbers)





age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are old!')
# else:
#     print('You are young!')
msg = 'Done'
new_age = ['You are old!' if age >= 18 else 'You are young!' for i in age]
send_message = [new_age for i in new_age if 'old' in new_age]
print(new_age)
print(send_message)