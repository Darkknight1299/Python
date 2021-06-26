#if else statements
if a_number % 2 == 0:
    print('{} is divisible by 2'.format(a_number))
elif a_number % 3 == 0:
    print('{} is divisible by 3'.format(a_number))
elif a_number % 5 == 0:
    print('{} is divisible by 5'.format(a_number))
else:
    print('All checks failed!')
    print('{} is not divisible by 2, 3 or 5'.format(a_number))

if '':
    print('The condition evaluted to True')
else:
    print('The condition evaluted to False')

if { 'a': 34 }:
    print('The condition evaluted to True')
else:
    print('The condition evaluted to False')

if a_number % 2 == 0:
    print("{} is even".format(a_number))
    if a_number % 3 == 0:
        print("{} is also divisible by 3".format(a_number))
    else:
        print("{} is not divisibule by 3".format(a_number))
else:
    print("{} is odd".format(a_number))
    if a_number % 5 == 0:
        print("{} is also divisible by 5".format(a_number))
    else:
        print("{} is not divisibule by 5".format(a_number))

#while loop
result = 1
i = 1

while i <= 100:
    result = result * i
    i = i+1

print('The factorial of 100 is: {}'.format(result))

#for loop
for i in range(7):
    print(i)

for i in range(3, 10):
    print(i)

for i in range(3, 14, 4):
    print(i)

a_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for i in range(len(a_list)):
    print('The value at position {} is {}.'.format(i, a_list[i]))

# Looping over a dictionary
person = {
    'name': 'John Doe',
    'sex': 'Male',
    'age': 32,
    'married': True
}

for key in person:
    print("Key:", key, ",", "Value:", person[key])

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for day in days:
    print(day)


