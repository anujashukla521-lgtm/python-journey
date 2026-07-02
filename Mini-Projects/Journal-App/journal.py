# Day 35- Journal Manager 
# Python-based Journal Application with add, view, and search functionality using file handling and input validation.

def add_journal():
    '''Add a journal entry to a file'''
    entry = input("Write a journal: ").strip()
    with open('journal.txt','a') as file:
        if not entry:
            print("Input cannot be empty")
            return 

        file.write(entry+"\n")


def view_journal():
    try:
        with open('journal.txt','r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File does not exist")


def search_journal():
    found = False
    keyword = input("Enter a keyword: ").strip()
    if not keyword:
        print("Input cannot be empty")
        return 

    try:
        with open('journal.txt','r') as file:
            for line in file:
                if keyword.lower() in line.lower():
                    found = True
                    print(line.strip())
            if not found:
                print("No journal found")
    except FileNotFoundError:
        print("File does not exist")
        return
        

            

def main():
    while True:
        try:
            choice = int(input("""Enter your choice:\n
            1-Add Journal\n
            2-View Journal\n
            3-Search Journal\n
            4-Exit\n"""))
        except ValueError:
            print("Non-numeric value entered")
            continue
            

        match choice:
            case 1:
                add_journal()

            case 2:
                view_journal()

            case 3:
                search_journal()

            case 4:
                print("Exit")
                break

            case _:
                print("Wrong choice")

main()
