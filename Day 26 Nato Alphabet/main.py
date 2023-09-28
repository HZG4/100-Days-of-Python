import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_frame = pandas.DataFrame(data)

nato_dict = {row.letter : row.code for (index, row) in data_frame.iterrows()}

output_array = []
user_input = input("Enter a name: ").upper()
input_array = list(user_input)
print(f"Name: {user_input}")

for i in range(len(input_array)):
    for (key, value) in nato_dict.items():
        if input_array[i] == key:
            output_array.append(value)
print(output_array)

