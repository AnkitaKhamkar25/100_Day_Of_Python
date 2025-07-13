# Random Password generator
import random
import string

letter=list(string.ascii_letters)
numbers = list(string.digits)
symbols = list('!#$%&()*+')

nr_letters=int(input("How many letters would you like in your password: "))
nr_symbols=int(input("How many symbols would you like in your password: "))
nr_numbers=int(input("How many numbers would you like in your password: "))


# Easy level
# password=""
# for char in range(0,nr_letters):
#     password+=random.choice(letter)

# for char in range(0,nr_symbols):
#     password+=random.choice(symbols)

# for char in range(0,nr_numbers):
#     password+=random.choice(numbers)

# print(password)

# Hard level

password_list=[]
for char in range(0,nr_letters):
    password_list.append(random.choice(letter))

for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
# print(password_list)

password=""
for char in password_list:
    password+=char
print(f"Your password is:{password}")