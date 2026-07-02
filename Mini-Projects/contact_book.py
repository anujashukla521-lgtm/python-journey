# Python-based Contact Book application with CRUD operations (Create, Read, Update, Delete), contact search, input validation, and menu-driven interaction.

contact_book = []

def add_contact(contacts):
    name = input("Enter name: ").strip()
    if not name:
        print("Name can't be empty")
        return
    try:
        phone = int(input("Enter mobile no.: "))
    except ValueError:
        print("Invalid phone number")
        return
    email = input("Enter email: ")
    if "@" not in email:
        print("Invalid email")
        return
    
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            print("Contact already exists")
            return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    print("Contact added successfully!")

def display_contact(contacts):
    print(f"Name {contacts['name']}")
    print(f"Phone {contacts['phone']}")
    print(f"Email {contacts['email']}")

def find_contact(contacts,name):
    for contact in contacts:
        if contact['name'].lower()==name.lower():
            return contact

    return None

def view_contact(contacts):
    if not contacts:
        print("No contacts found")
        return 

    for index,contact in enumerate(contacts,start=1):
        print(f"\nContact {index}")
        display_contact(contact)
       

def search_contact(contacts):
    name = input("Enter name: ")
    
    contact = find_contact(contacts,name)
    if not contact:
        print("Contact not found")
        return

    print("\nContact found")
    display_contact(contact)
    

def delete_contact(contacts):
    name = input("Enter contact to delete: ")
    
    contact = find_contact(contacts,name)
    if not contact:
        print("Contact not found")
        return

    contacts.remove(contact)
    print("Contact deleted successfully")
            
def update_contact(contacts):
    name = input("Enter name to update: ")

    
    contact = find_contact(contacts, name)

    if not contact:
        print("Contact not found")
        return

    print("What do you want to update?")
    print("1. Name")
    print("2. Phone")
    print("3. Email")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input")
        return
    match choice:
        case 1:
            new_name = input("Enter new name: ").strip()
            if not new_name:
                print("Name can't be empty")
                return 

            for c in contacts:
                if c["name"].lower()==new_name.lower():
                    print("Contact already exists")
                    return

            contact["name"]=new_name
        case 2:
            try:
                contact["phone"] = int(input("Enter new phone:"))
            except ValueError:
                print("Invalid phone number")
                return
        
        case 3:
            email = input("Enter new email: ")
            if "@" not in email:
                print("Invalid email")
                return

            contact["email"] = email
        case _:
            print("Invalid choice")
            return

    print("Contact updated successfully!")
    return

while True:
    try:

        choice = int(input("Enter your choice\n1- Add contact\n2- Display contacts\n3- Search contacts\n4- Delete contact\n5- Update Contact\n6- Exit\n"))
    except ValueError:
        print("Invalid input")
        continue

    match choice:
        case 1:
            add_contact(contact_book)
        case 2:
            view_contact(contact_book)
        case 3:
            search_contact(contact_book)
        case 4:
            delete_contact(contact_book)
        case 5:
            update_contact(contact_book)
        case 6:
            print("Exit")
            break
        case _:
            print("Wrong choice")

