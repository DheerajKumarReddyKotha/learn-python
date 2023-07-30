def find_acronym():
    look_up = input("What Software accronym would you like to view ?\n")
    found = False
    with open("acronym.txt") as file:
        for line in file:
            if look_up in line:
                print(line)
                found = True
                break
    if not found:
        print("Accronym does not exist")

def add_acronym():
    acronym = input("What is the acronym you want to add? \n")
    definition = input("what is the definition?\n")
    with open("acronym.txt","a") as file: #`w` mode overrides the file, `a` adds to end of file
        file.write(acronym+":"+definition+"\n")


def main():
    choice = input("Do you want to find(F) or Add(A) acronym ? \n")
    if choice == "F":
        find_acronym()
    elif choice == "A":
        add_acronym()

main()