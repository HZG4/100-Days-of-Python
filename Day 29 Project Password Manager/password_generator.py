import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(5, 9)
    nr_symbols = random.randint(1,6)
    nr_numbers = random.randint(1,6)

    pw_letters = ''
    for i in range(0, nr_letters):
        n = random.choice(letters)
        pw_letters = pw_letters + n

    pw_symbols = ''
    for i in range(0, nr_symbols):
        n = random.choice(symbols)
        pw_symbols = pw_symbols + n

    pw_numbers = ''
    for i in range(0, nr_numbers):
        n = random.choice(numbers)
        pw_numbers = pw_numbers + n

    password = ''
    character = pw_letters + pw_numbers + pw_symbols
    character_list = list(character)
    random.shuffle(character_list)
    password = password.join(character_list)
    return password