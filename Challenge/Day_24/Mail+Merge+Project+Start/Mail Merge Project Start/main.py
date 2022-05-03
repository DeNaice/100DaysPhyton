# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", mode="r") as file:
    name_list = file.readlines()

with open("Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_text = letter.read()
    print(letter_text)

for name in name_list:
    stripped_name = name.strip()
    ready_letter = letter_text.replace("[name]", stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}", mode="w") as got_it:
        got_it.write(ready_letter)
