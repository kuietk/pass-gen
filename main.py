#------------------#
#PASSWORD GENERATOR#
#------------------#

import random, os

#VARIABLES

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '*', '+']

password_list = []

password = ""
#----------------------------------------------#
os.system("clear")
print("--------------------")
print(" PASSWORD GENERATOR ")
print("--------------v0.06-")
print("")
print("a : quick gen 12")
print("b : quick gen 6")
print("c : custom")

print("")

grab = input(str("Please make a selection\n"))

if grab == "a":
	for char in range(1, 9):
		password_list.append(random.choice(letters))
	for char in range(1, 3):
		password_list.append(random.choice(numbers))
	for char in range(1, 2):
		password_list.append(random.choice(cap_letters))
	for char in range(1, 2):
		password_list.append(random.choice(symbols))

elif grab == "b":
	for char in range(1, 3):
		password_list.append(random.choice(letters))
	for char in range(1, 3):
		password_list.append(random.choice(numbers))
	for char in range(1, 2):
		password_list.append(random.choice(cap_letters))
	for char in range(1, 2):
		password_list.append(random.choice(symbols))

#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
elif grab == "c":

	letter_amount = int(input("How many letters?\n"))
	number_amount = int(input("Numbers?\n"))
	capital_amount = int(input("Any capitals?\n"))
	symbol_amount = int(input("What about symbols?\n"))

	for char in range(1, letter_amount + 1):
		password_list.append(random.choice(letters))
	for char in range(1, number_amount + 1):
		password_list += random.choice(numbers)
	for char in range(1, capital_amount + 1):
		password_list += random.choice(cap_letters)
	for char in range(1, symbol_amount + 1):
		password_list += random.choice(symbols)
else:
	os.system("clear")
	print("read the fuckin prompt")


random.shuffle(password_list)



for char in password_list:
	password += char

print(password)

print(boop)