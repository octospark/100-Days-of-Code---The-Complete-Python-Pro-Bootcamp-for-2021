#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as letter:
    content_of_letter = letter.readlines()

with open("./Input/Names/invited_names.txt") as letter:
    list_of_names = letter.readlines()

for name in list_of_names:
    new_letter = ""

    with open("./Output/ReadyToSend/" + f"letter_to_{name.strip()}.txt", 'w') as file:
        for row in content_of_letter:
            if PLACEHOLDER in row:
                new_row = row.replace(PLACEHOLDER, name.strip())
                file.write(new_row)
            else:
                file.write(row)
