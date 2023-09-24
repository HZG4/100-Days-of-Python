invited_names = []
starting_letter = ""
with open(r".\Input\Names\invited_names.txt") as file:
    invited_names = file.readlines()

with open(r".\Input\Letters\starting_letter.txt") as file:
    starting_letter = file.read()

for name in invited_names:
    name = name.strip()
    personalized_letter = starting_letter.replace("[name]", name)
    with open(f".\Output\ReadyToSend\letter_for_{name}", mode="w") as file:
        file.write(personalized_letter)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp