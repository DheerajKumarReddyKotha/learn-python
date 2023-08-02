# Ask user what acronym they want to add
# Then ask the user for definition
# open the file
# Write the new acronym and definition


acronym = input("What is the acronym you want to add? \n")
definition = input("what is the definition?\n")
with open("acronym.txt", "a") as file:  # `w` mode overrides the file, `a` adds to end of file
    file.write(acronym + ":" + definition + "\n")
