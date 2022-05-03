# with open("my_file.txt") as file:
#   contents = file.read()
#  print(contents)
# r für read w für ersetzend write a für append / nicht vorhandene datei bei w wird erstellt
with open("my_file.txt", mode="w") as file:
    file.write("\nNeuer text")
