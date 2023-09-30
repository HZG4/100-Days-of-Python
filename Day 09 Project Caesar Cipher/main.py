from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    caesar_string = ""
    for letter in text:
        if letter == " ":
            caesar_string = caesar_string + " "
        elif direction == "encode":
            index_in_list = alphabet.index(letter)
            caesar_letter = alphabet[index_in_list + shift]
            caesar_string = caesar_string + caesar_letter
        elif direction == "decode":
            index_in_list = alphabet.index(letter)
            caesar_letter = alphabet[index_in_list - shift]
            caesar_string = caesar_string + caesar_letter
    print(caesar_string)


condition = True
print(logo + "\n" + "Welcome to Caesar Cipher")

while condition == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(text, shift, direction)

    query = input("Do you want to continue? Y or N: ").lower()
    if query == "n":
        condition = False



