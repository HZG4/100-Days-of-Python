import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print("Enter the desired number of characters in the following.")
nr_letters = int(input("Number of letters: "))
nr_symbols = int(input("Number of symbols: "))
nr_numbers = int(input("Number of numbers: "))

pw_letters = ''
for i in range(0, nr_letters):
    n = random.randint(0, len(letters) - 1)
    pw_letters = pw_letters + letters[n]

pw_symbols = ''
for i in range(0, nr_symbols):
    n = random.randint(0, len(symbols) - 1)
    pw_symbols = pw_symbols + symbols[n]

pw_numbers = ''
for i in range(0, nr_numbers):
    n = random.randint(0,len(numbers) - 1)
    pw_numbers = pw_numbers + numbers[n]

password = ''
character = pw_letters + pw_numbers + pw_symbols
character_list = list(character)
random.shuffle(character_list)
password = password.join(character_list)
print(f"Your generated password is: {password}")