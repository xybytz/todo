from os.path import exists
lst = 'lst'

def read():
    if exists(lst):
        with open(lst, 'r') as file:
            lines = file.readlines()
            print(lines)

def add():
    with open(lst, 'a') as file:
        newitem = input("Enter what you would like to add")
        newitem = newitem + ", "
        file.write(newitem)

choice = input("Add to list [1] or see current list [2]?")
if choice == "1":
    add()

elif choice == "2":
    read()

else:
    quit()
        
